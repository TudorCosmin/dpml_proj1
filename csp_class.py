import random
import time

class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        # variables: list of possible variables [var1, var2, var3, ...]

        self.domains = domains
        # domains = dictionary of pairs var : list of possible values
        # {
        #   var1: [1, 2, 3, ...],
        #   var2: [1, 2, 3, ...],
        #   ...
        # } 

        self.constraints = constraints
        # constraints = list of functions (each ones checks a constraint based on the variables and their values)

        self.BKT_TIME_LIMIT = 10

    def is_complete(self, state):
        # Check if all variables have been assigned a value
        return all(str(var) in state for var in self.variables)

    def select_unassigned_variable(self, state):
        # Choose an unassigned variable
        for var in self.variables:
            if str(var) not in state:
                return var
        return None
    
    # -------------------------------------------------- BKT
    
    def check_constraints(self, state):
        # Check if all the constraints are satisfied
        for constraint in self.constraints:
            if not constraint(state):
                return False
        return True

    def backtracking_solution(self, state={}, start_time=None):
        if start_time is None:
            start_time = time.time()  # Initialize the start time if not already set

        # Check if the time limit has been exceeded
        if time.time() - start_time > self.BKT_TIME_LIMIT:
            return None

        # If assignment is complete, return the state as a solution
        if self.is_complete(state):
            # Check if the complete state satisfies all constraints
            if self.check_constraints(state):
                return state
            else:
                return None

        # Select the next variable to assign
        for var in self.variables:
            if var not in state:
                break

        # Try each value in the domain for the selected variable
        for value in self.domains[var]:
            # Create a new assignment for the variable
            new_state = state.copy()
            new_state[var] = value

            # Proceed with backtracking
            result = self.backtracking_solution(new_state, start_time)
            if result:
                return result

        # If no value leads to a solution, backtrack
        return None
    
    # -------------------------------------------------- chronological BKT

    def check_chronological_constraints(self, state):
        # Check if all the constraints are satisfied
        for constraint in self.constraints:
            try:
                if not constraint(state):
                    return False
            except KeyError:
                # Allow partial assignments to pass by returning True
                continue
        return True

    def chronological_backtracking_solution(self, state={}):
        # If assignment is complete, return the state as a solution
        if self.is_complete(state):
            return state
        
        # Select an unassigned variable
        var = self.select_unassigned_variable(state)

        # Try each value in the domain for the selected variable
        for value in self.domains[str(var)]:
            # Create a new assignment for the variable
            new_state = state.copy()
            new_state[str(var)] = value

            # Check if the current assignment satisfies all constraints
            if self.check_chronological_constraints(new_state):
                result = self.chronological_backtracking_solution(new_state)
                if result:
                    return result

        # If no value leads to a solution, backtrack
        return None
    
    # -------------------------------------------------- Hill-Climbing

    def conflict_score(self, state):
        # Count the number of violated constraints
        score = 0
        for constraint in self.constraints:
            try:
                if not constraint(state):
                    score += 1
            except KeyError:
                # Ignore partial assignments
                continue
        return score

    def generate_initial_state(self):
        return {var: random.choice(self.domains[var]) for var in self.variables}

    def hill_climbing_solution(self, max_restarts=10000):
        for restart in range(max_restarts):
            # Generate a random initial state
            current_state = self.generate_initial_state()
            current_score = self.conflict_score(current_state)

            while True:
                if current_score == 0:
                    # Found a solution
                    return current_state

                # Try to improve the state by modifying one variable
                best_neighbor = None
                best_score = float('inf')

                # Search for the best option in adjacent neighbors
                for var in self.variables:
                    for value in self.domains[var]:
                        if value != current_state[var]:
                            # Create a new state with the updated variable
                            neighbor = current_state.copy()
                            neighbor[var] = value

                            # Evaluate the neighbor's conflict score
                            neighbor_score = self.conflict_score(neighbor)

                            # Keep track of the best neighbor
                            if neighbor_score < best_score:
                                best_neighbor = neighbor
                                best_score = neighbor_score

                # Update the current state if a better neighbor was found
                if best_score < current_score:
                    current_state = best_neighbor
                    current_score = best_score
                else:
                    # No improvement possible, terminate this hill-climbing attempt
                    break

            # Restart if no solution was found in this run
            # print(f"Restarting... (attempt {restart + 1})")

        # If all restarts fail, return None (shouldn't happen if the problem is solvable)
        return None
    
    # -------------------------------------------------- Arc Consistency
    # Arc-consistency in a Constraint Satisfaction Problem ensures that
    # every value in the domain of one variable is consistent with
    # at least one value in the domain of another variable it is constrained with.
    def revise_domain(self, x, y):
        # Revise the domain of variable x to ensure arc-consistency with variable y.
        # Removes values from the domain of x that have no compatible value in the domain of y.
        # Returns True if a value is removed; otherwise, False.
        revised = False
        x_domain = self.domains[x]
        y_domain = self.domains[y]

        # Iterate over initial x_domain (and make changes to the real domain in real time)
        for value_x in list(x_domain):
            consistent = False

            # Check all values in y's domain for compatibility with value_x
            for value_y in y_domain:
                if self.satisfies_constraints(x, value_x, y, value_y):
                    consistent = True
                    break  # At least one valid value_y is found

            # If no consistent value_y exists, remove value_x from x_domain
            if not consistent:
                x_domain.remove(value_x)
                revised = True

        return revised

    def satisfies_constraints(self, x, value_x, y, value_y):
        # Checks if the pair (x=value_x, y=value_y) satisfies all constraints between x and y.

        # Dummy state to check the constraints
        dummy_state = {x: value_x, y: value_y}
        for constraint in self.constraints:
            try:
                if not constraint(dummy_state):
                    return False
            except KeyError:
                # Ignore constraints that require more variables
                continue
        return True

    def arc_consistency(self):
        # Implements the arc consistency algorithm.

        # Step 1: Initialize the queue with all arcs
        queue = [(x, y) for x in self.variables for y in self.variables if x != y]
        # print(queue)

        # Step 2: Process the queue until no changes
        while queue:
            x, y = queue.pop(0)  # Dequeue an arc
            if self.revise_domain(x, y):  # Revise the domain of x
                if not self.domains[x]:  # If the domain of x is empty, CSP is unsolvable
                    return False
                # If x's domain is reduced, add all related arcs back to the queue
                for z in self.variables:
                    if z != x and z != y:
                        queue.append((z, x))

        return True

    # -------------------------------------------------- Path Consistency
    def revise_path_domain(self, x, y, z):
        # Revise the domain of variable x to ensure path-consistency with y and z.
        # Uses relation composition to remove values from x's domain that cannot participate
        # in valid triplets with y and z.
        # Returns True if the domain of x is modified; otherwise, False.
        revised = False  # Track if x's domain is modified
        x_domain = self.domains[x]
        y_domain = self.domains[y]
        z_domain = self.domains[z]

        # Iterate over a copy of x's domain to allow safe modification
        for value_x in list(x_domain):
            valid = False  # Track if value_x is consistent in any triplet

            # Check all combinations of y and z values
            for value_y in y_domain:
                for value_z in z_domain:
                    # Check if (x=value_x, y=value_y, z=value_z) satisfies all relevant constraints
                    if self.satisfies_path_constraints(x, value_x, y, value_y, z, value_z):
                        valid = True
                        break  # Stop checking further if a valid triplet is found
                if valid:
                    break

            # If no valid triplet exists, remove value_x from x's domain
            if not valid:
                x_domain.remove(value_x)
                revised = True

        return revised

    def satisfies_path_constraints(self, x, value_x, y, value_y, z, value_z):
        # Checks if the triplet (x=value_x, y=value_y, z=value_z) satisfies all constraints between x, y, and z.

        # Create a partial state with the current values
        state = {x: value_x, y: value_y, z: value_z}

        # Check all constraints in the CSP
        for constraint in self.constraints:
            try:
                # If any constraint is violated, the triplet is invalid
                if not constraint(state):
                    return False
            except KeyError:
                # Ignore constraints that require more variables than provided in the state
                continue

        # If all relevant constraints are satisfied, return True
        return True
    
    def path_consistency(self):
        # Implements the naive path consistency algorithm
        # Ensures that for every triplet of variables (X, Y, Z), their constraints are consistent.
        # Returns True if the CSP is path-consistent, False if an empty domain is encountered.
        
        # Get the list of variables
        variables = self.variables

        # Iterate until no changes occur
        while True:
            changes = False  # Track if any domain or constraint is modified

            # Iterate over all triplets of variables (X, Y, Z)
            for x in variables:
                for y in variables:
                    for z in variables:
                        # Skip triplets where variables are not distinct
                        if x == y or y == z or x == z:
                            continue

                        # Perform relation composition and update the domain of X
                        if self.revise_path_domain(x, y, z):
                            changes = True

                            # If a domain becomes empty, the CSP is unsolvable
                            if not self.domains[x]:
                                return False

            # If no changes occurred, stop
            if not changes:
                break

        return True
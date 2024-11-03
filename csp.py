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

    def check_constraints(self, state):
        # Check if all the constraints are satisfied
        for constraint in self.constraints:
            try:
                if not constraint(state):
                    return False
            except KeyError:
                # Allow partial assignments to pass by returning True
                continue
        return True

    def is_complete(self, state):
        # Check if all variables have been assigned a value
        return all(str(var) in state for var in self.variables)

    def select_unassigned_variable(self, state):
        # Choose an unassigned variable
        for var in self.variables:
            if str(var) not in state:
                return var
        return None

    def backtracking_solution(self, state={}):
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
            if self.check_constraints(new_state):
                result = self.backtracking_solution(new_state)
                if result:
                    return result

        # If no value leads to a solution, backtrack
        return None
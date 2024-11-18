from csp_class import CSP
from eq_constraints_generator import generate_csp_definition
from comparison import compare_csp_algorithms

# Size of the square / number of variables
n = 9

generate_csp_definition(n)

from csp_definition import variables, domains, constraints

# Equations contraints
def constraint_eq1(state):
    return state["B"] + state["D"] == 11
def constraint_eq2(state):
    return state["E"] + state["F"] == 13
def constraint_eq3(state):
    return state["B"] + state["C"] + state["I"] == 7
def constraint_eq4(state):
    return state["C"] + state["D"] + state["G"] == 19
def constraint_eq5(state):
    return state["C"] + state["F"] + state["G"] == 18
def constraint_eq6(state):
    return state["A"] + state["C"] + state["I"] == 8

constraints.extend([
    constraint_eq1,
    constraint_eq2,
    constraint_eq3,
    constraint_eq4,
    constraint_eq5,
    constraint_eq6
])



# Create a CSP instance and solve it
csp = CSP(variables, domains, constraints)
compare_csp_algorithms(csp)


# solution = csp.chronological_backtracking_solution()
# solution = csp.backtracking_solution()
# solution = csp.hill_climbing_solution()

# if solution:
#     print("Solution found:", solution)
# else:
#     print("No solution exists.")

# print()
# if csp.arc_consistency():
#     print("Arc-consistency achieved.")
#     print("Updated domains:", csp.domains)
# else:
#     print("CSP is unsolvable.")

# print()
# if csp.path_consistency():
#     print("Path-consistency achieved.")
#     print("Updated domains:", csp.domains)
# else:
#     print("CSP is unsolvable.")

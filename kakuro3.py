from csp_class import CSP
from comparison import compare_csp_algorithms

# Variables for the CSP (annotated positions in the grid)
variables = [f"var{i}" for i in range(1,4+1)]

# Domains for each variable
domains = {
    "var1": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var3": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var4": [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# state = {
#    "var1": value set for variable 1,
#    "var2": value set for variable 2,
#    "var3": value set for variable 3,
#    "var4": value set for variable 4,
# }

# Constraints based on the grid rules
def constraint1(state):
    return state["var1"] + state["var2"] == 17

def constraint2(state):
    return state["var3"] + state["var4"] == 6

def constraint3(state):
    return state["var1"] + state["var3"] == 12

def constraint4(state):
    return state["var2"] + state["var4"] == 11

def constraint5(state):
    return state["var1"] != state["var2"]

def constraint6(state):
    return state["var3"] != state["var4"]

def constraint7(state):
    return state["var1"] != state["var3"]

def constraint8(state):
    return state["var2"] != state["var4"]

constraints = [
    constraint1,
    constraint2,
    constraint3,
    constraint4,
    constraint5,
    constraint6,
    constraint7,
    constraint8,
]

# Create a CSP instance and solve it
csp = CSP(variables, domains, constraints)
compare_csp_algorithms(csp)


# # solution = csp.chronological_backtracking_solution()
# # solution = csp.backtracking_solution()
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
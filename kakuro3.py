from csp import CSP

# Variables for the CSP (annotated positions in the grid)
variables = [f"var{i}" for i in range(1,5)]

# Domains for each variable
domains = {
    "var1": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var3": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var4": [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# state = {
#    "1": value set for variable 1,
#    "2": value set for variable 2,
#    "3": value set for variable 3,
#    "4": value set for variable 4,
# }

# Constraints based on the grid rules
def constraint1(state):
    return state["var1"] + state["var2"] == 10

def constraint2(state):
    return state["var3"] + state["var4"] == 3

def constraint3(state):
    return state["var1"] + state["var3"] == 7

def constraint4(state):
    return state["var2"] + state["var4"] == 6

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
solution = csp.backtracking_solution()

if solution:
    print("Solution found:", solution)
else:
    print("No solution exists.")

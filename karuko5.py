from csp import CSP

# Variables for the CSP (annotated positions in the grid)
variables = [f"var{i}" for i in range(1,13)]

# Domains for each variable
domains = {
    "var1": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var2": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var3": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var4": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var5": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var6": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var7": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var8": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var9": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var10": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var11": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "var12": [1, 2, 3, 4, 5, 6, 7, 8, 9]
}

# state = {
#    "1": value set for variable 1,
#    "2": value set for variable 2,
#    "3": value set for variable 3,
#    "4": value set for variable 4,
# }

# Horizontal sum constraints
def horizontal_constraint1(state):
    return state["var1"] + state["var2"] + state["var3"] == 7

def horizontal_constraint2(state):
    return state["var4"] + state["var5"] + state["var6"] == 20

def horizontal_constraint3(state):
    return state["var7"] + state["var8"] + state["var9"] == 9

def horizontal_constraint4(state):
    return state["var10"] + state["var11"] + state["var12"] == 15

# Vertical sum constraints
def vertical_constraint1(state):
    return state["var1"] + state["var4"] == 5

def vertical_constraint2(state):
    return state["var2"] + state["var5"] + state["var7"] + state["var10"] == 13

def vertical_constraint3(state):
    return state["var3"] + state["var6"] + state["var8"] + state["var11"] == 25

def vertical_constraint4(state):
    return state["var9"] + state["var12"] == 8

# Uniqueness constraints for rows
def uniqueness_constraint_row1(state):
    values = [state["var1"], state["var2"], state["var3"]]
    return len(values) == len(set(values))

def uniqueness_constraint_row2(state):
    values = [state["var4"], state["var5"], state["var6"]]
    return len(values) == len(set(values))

def uniqueness_constraint_row3(state):
    values = [state["var7"], state["var8"], state["var9"]]
    return len(values) == len(set(values))

def uniqueness_constraint_row4(state):
    values = [state["var10"], state["var11"], state["var12"]]
    return len(values) == len(set(values))

# Uniqueness constraints for columns
def uniqueness_constraint_col1(state):
    values = [state["var1"], state["var4"]]
    return len(values) == len(set(values))

def uniqueness_constraint_col2(state):
    values = [state["var2"], state["var5"], state["var7"], state["var10"]]
    return len(values) == len(set(values))

def uniqueness_constraint_col3(state):
    values = [state["var3"], state["var6"], state["var8"], state["var11"]]
    return len(values) == len(set(values))

def uniqueness_constraint_col4(state):
    values = [state["var9"], state["var12"]]
    return len(values) == len(set(values))

# Add all constraints to the list
constraints = [
    horizontal_constraint1, horizontal_constraint2, horizontal_constraint3, horizontal_constraint4,
    vertical_constraint1, vertical_constraint2, vertical_constraint3, vertical_constraint4,
    uniqueness_constraint_row1, uniqueness_constraint_row2, uniqueness_constraint_row3, uniqueness_constraint_row4,
    uniqueness_constraint_col1, uniqueness_constraint_col2, uniqueness_constraint_col3, uniqueness_constraint_col4
]


# Create a CSP instance and solve it
csp = CSP(variables, domains, constraints)
solution = csp.backtracking_solution()

if solution:
    print("Solution found:")
    for key, value in solution.items():
        print(f"{key}: {value}")
else:
    print("No solution exists.")


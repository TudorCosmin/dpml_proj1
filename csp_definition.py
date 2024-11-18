# This code is automated generated. It defines the input model to a logical expression problem.
# Please see eq_constraints_generator.py file for details about how this code is generated

# Variables for the CSP
variables = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
]

# Domains for the CSP
domains = {
    "A": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "B": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "C": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "D": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "E": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "F": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "G": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "H": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "I": [1, 2, 3, 4, 5, 6, 7, 8, 9],
}

# Unicity constraints
def constraint1(state):
    return state["A"] != state["B"]

def constraint2(state):
    return state["A"] != state["C"]

def constraint3(state):
    return state["A"] != state["D"]

def constraint4(state):
    return state["A"] != state["E"]

def constraint5(state):
    return state["A"] != state["F"]

def constraint6(state):
    return state["A"] != state["G"]

def constraint7(state):
    return state["A"] != state["H"]

def constraint8(state):
    return state["A"] != state["I"]

def constraint9(state):
    return state["B"] != state["C"]

def constraint10(state):
    return state["B"] != state["D"]

def constraint11(state):
    return state["B"] != state["E"]

def constraint12(state):
    return state["B"] != state["F"]

def constraint13(state):
    return state["B"] != state["G"]

def constraint14(state):
    return state["B"] != state["H"]

def constraint15(state):
    return state["B"] != state["I"]

def constraint16(state):
    return state["C"] != state["D"]

def constraint17(state):
    return state["C"] != state["E"]

def constraint18(state):
    return state["C"] != state["F"]

def constraint19(state):
    return state["C"] != state["G"]

def constraint20(state):
    return state["C"] != state["H"]

def constraint21(state):
    return state["C"] != state["I"]

def constraint22(state):
    return state["D"] != state["E"]

def constraint23(state):
    return state["D"] != state["F"]

def constraint24(state):
    return state["D"] != state["G"]

def constraint25(state):
    return state["D"] != state["H"]

def constraint26(state):
    return state["D"] != state["I"]

def constraint27(state):
    return state["E"] != state["F"]

def constraint28(state):
    return state["E"] != state["G"]

def constraint29(state):
    return state["E"] != state["H"]

def constraint30(state):
    return state["E"] != state["I"]

def constraint31(state):
    return state["F"] != state["G"]

def constraint32(state):
    return state["F"] != state["H"]

def constraint33(state):
    return state["F"] != state["I"]

def constraint34(state):
    return state["G"] != state["H"]

def constraint35(state):
    return state["G"] != state["I"]

def constraint36(state):
    return state["H"] != state["I"]

constraints = [
    constraint1,
    constraint2,
    constraint3,
    constraint4,
    constraint5,
    constraint6,
    constraint7,
    constraint8,
    constraint9,
    constraint10,
    constraint11,
    constraint12,
    constraint13,
    constraint14,
    constraint15,
    constraint16,
    constraint17,
    constraint18,
    constraint19,
    constraint20,
    constraint21,
    constraint22,
    constraint23,
    constraint24,
    constraint25,
    constraint26,
    constraint27,
    constraint28,
    constraint29,
    constraint30,
    constraint31,
    constraint32,
    constraint33,
    constraint34,
    constraint35,
    constraint36,
]

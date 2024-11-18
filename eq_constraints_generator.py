def generate_csp_definition(n, file_name="csp_definition.py"):
    # Generates CSP code (variables, domains, and unicity constraints declaration) for a grid of size n x n

    with open(file_name, "w") as file:
        file.write("# This code is automated generated. It defines the input model to a logical expression problem.\n")
        file.write("# Please see eq_constraints_generator.py file for details about how this code is generated\n\n")


        # Variable naming: A, B, C, D, ...
        variables = [chr(65 + i) for i in range(n)]

        # Write the variable declarations
        file.write("# Variables for the CSP\n")
        file.write("variables = [\n")
        for var in variables:
            file.write(f"    \"{var}\",\n")
        file.write("]\n\n")

        # Write the domains declaration
        file.write("# Domains for the CSP\n")
        file.write("domains = {\n")
        for var in variables:
            file.write(f"    \"{var}\": {[i for i in range(1, n+1)]},\n")
        file.write("}\n\n")

        # Write the unicity constraints header
        file.write("# Unicity constraints\n")
        
        # Write all unique pairs of variables (combinations)
        constraint_count = 1
        for i in range(len(variables)):
            for j in range(i + 1, len(variables)):
                var1 = variables[i]
                var2 = variables[j]
                
                file.write(f"def constraint{constraint_count}(state):\n")
                file.write(f"    return state[\"{var1}\"] != state[\"{var2}\"]\n")
                file.write("\n")
                constraint_count += 1

        # Write the constraints list
        file.write("constraints = [\n")
        for i in range(1, constraint_count):
            file.write(f"    constraint{i},\n")
        file.write("]\n")
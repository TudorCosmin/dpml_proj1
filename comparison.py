import time
import pandas as pd
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from csp_class import CSP

def compare_csp_algorithms(csp):
    results = []
    TIME_LIMIT = 9

    # Helper function to run a CSP-solving method with a timeout
    def time_method(csp_instance, method_name):
        print(f"Running {method_name}...")
        with ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(getattr(csp_instance, method_name))
            try:
                start_time = time.time()
                solution = future.result(timeout=TIME_LIMIT)
                elapsed_time = round(time.time() - start_time, 5)
                return elapsed_time, solution
            except TimeoutError:
                print(f"{method_name} exceeded time limit!")
                return "TLE", None
            except Exception as e:
                print(f"Error running {method_name}: {e}")
                return "ERROR", None

    # Run algorithms on initial input
    print("Running algorithms on the initial CSP input...")
    for method in ['chronological_backtracking_solution', 'backtracking_solution', 'hill_climbing_solution']:
        elapsed_time, solution = time_method(csp, method)
        results.append({
            'Preprocessing': 'None',
            'Method': method,
            'Time (s)': "TLE" if elapsed_time == "TLE" else elapsed_time,
            'Solution Found': False if elapsed_time == "TLE" else bool(solution)
        })
    print("Finished running algorithms on the initial input.\n")

    # Apply arc consistency preprocessing
    print("Applying arc consistency preprocessing...")
    start_arc = time.time()  # Start timing arc consistency
    arc_result = csp.arc_consistency()  # Apply arc consistency
    arc_time = round(time.time() - start_arc, 5)  # Time taken for arc consistency
    print(f"Arc consistency completed in {arc_time:.5f} seconds. Running algorithms with updated domains...")

    # Run algorithms after arc consistency
    for method in ['chronological_backtracking_solution', 'backtracking_solution', 'hill_climbing_solution']:
        csp_copy = CSP(csp.variables, csp.domains.copy(), csp.constraints)
        elapsed_time, solution = time_method(csp_copy, method)
        results.append({
            'Preprocessing': 'Arc Consistency',
            'Method': method,
            'Time (s)': "TLE" if elapsed_time == "TLE" else elapsed_time,
            'Solution Found': False if elapsed_time == "TLE" else bool(solution)
        })
    print("Finished running algorithms with arc consistency preprocessing.\n")

    # Apply path consistency preprocessing
    print("Applying path consistency preprocessing...")
    start_path = time.time()
    path_result = csp.path_consistency()
    path_time = round(time.time() - start_path, 5)
    print(f"Path consistency completed in {path_time:.5f} seconds. Running algorithms with updated domains...")

    # Run algorithms after path consistency
    for method in ['chronological_backtracking_solution', 'backtracking_solution', 'hill_climbing_solution']:
        csp_copy = CSP(csp.variables, csp.domains.copy(), csp.constraints)
        elapsed_time, solution = time_method(csp_copy, method)
        results.append({
            'Preprocessing': 'Path Consistency',
            'Method': method,
            'Time (s)': "TLE" if elapsed_time == "TLE" else elapsed_time,
            'Solution Found': False if elapsed_time == "TLE" else bool(solution)
        })
    print("Finished running algorithms with path consistency preprocessing.\n")

    # Plot the table of results
    print("Plotting the results as a table...")
    df = pd.DataFrame(results)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(
        cellText=df.values,  # Table content
        colLabels=df.columns,  # Column headers
        cellLoc='center',  # Align cells
        loc='center'  # Position the table at the center
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(df.columns))))  # Adjust column widths

    # Show the table
    plt.title("CSP Algorithm Comparison", fontsize=14, fontweight="bold")  # Add a title
    plt.show()

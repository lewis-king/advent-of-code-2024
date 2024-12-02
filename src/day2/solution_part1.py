# We will use the `itertools` module to group the levels by whether they are increasing or decreasing
import itertools

# Define a function to check whether a report is safe
def is_safe(report: str) -> bool:
    # Split the report into a list of integers
    levels = list(map(int, report.split()))
    # Calculate the differences between adjacent levels
    differences = [b - a for a, b in zip(levels, levels[1:])]
    # Check whether all differences are between 1 and 3
    if not all(1 <= abs(d) <= 3 for d in differences):
        return False
    # Group the differences by whether they are positive or negative
    groups = [list(g) for k, g in itertools.groupby(differences, key=lambda x: x > 0)]
    # Check whether all differences are in the same group (i.e., all increasing or all decreasing)
    return len(groups) == 1

# Define a function to read the reports from a file and count the number of safe reports
def count_safe_reports(filename: str) -> int:
    safe_reports = 0
    try:
        with open(filename, 'r') as file:
            # Read the reports line by line
            for report in file:
                # Check whether the report is safe and increment the counter if it is
                if is_safe(report):
                    safe_reports += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1
    # Return the number of safe reports
    return safe_reports

# Use the function to count the number of safe reports in the input file
print(count_safe_reports("input/input.txt"))
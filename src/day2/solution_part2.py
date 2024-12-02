#This solution reads the input file line by line, splitting each line into a list of integer levels. It then checks if each report is safe by calling the `is_safe` function. If a report is not safe, it checks if removing any single level makes the report safe. If it does, the report is counted as safe. The function finally returns the total count of safe reports. The error handling code ensures that a helpful error message is printed if the input file is not found or if any other error occurs while processing the file.
def is_safe(report: list) -> bool:
    """
    Function to check if a report is safe.
    """
    # Check if the report is increasing or decreasing
    if report[0] < report[1]:
        increasing = True
    else:
        increasing = False

    # Check each pair of levels in the report
    for i in range(len(report) - 1):
        # If the report is increasing
        if increasing:
            # If the next level is less than or more than 3 than the current level, return False
            if not (1 <= report[i+1] - report[i] <= 3):
                return False
        # If the report is decreasing
        else:
            # If the next level is greater than or less than 3 than the current level, return False
            if not (1 <= report[i] - report[i+1] <= 3):
                return False

    # If no issues are found, return True
    return True


def count_safe_reports(filename: str) -> int:
    """
    Function to count the number of safe reports in a file.
    """
    safe_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert the report to a list of integers
                report = list(map(int, line.split()))
                if is_safe(report):
                    safe_count += 1
                else:
                    # Check if removing any single level makes the report safe
                    for i in range(len(report)):
                        if is_safe(report[:i] + report[i+1:]):
                            safe_count += 1
                            break
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return safe_count


print(count_safe_reports('input/input.txt'))
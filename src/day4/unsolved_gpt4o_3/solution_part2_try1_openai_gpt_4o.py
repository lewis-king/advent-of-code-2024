#This code defines a solution to count the number of X-MAS patterns in a given word search grid, as described in the puzzle. It reads the input from a file, processes it to count the patterns, and prints the result. The solution includes error handling for file operations and uses Python best practices for readability and efficiency.
def count_x_mas(pattern: list[list[str]]) -> int:
    """
    Count the number of 'X-MAS' patterns in the given word search.

    An 'X-MAS' pattern is defined by:
      M.S
      .A.
      M.S
    """
    rows = len(pattern)
    cols = len(pattern[0])
    count = 0

    # Iterate over each possible center of the 'X'
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Check for the X-MAS pattern in all 8 possible orientations
            if ((pattern[row-1][col-1] == 'M' and pattern[row+1][col+1] == 'M' and
                 pattern[row][col] == 'A' and pattern[row-1][col+1] == 'S' and pattern[row+1][col-1] == 'S') or
                (pattern[row-1][col+1] == 'M' and pattern[row+1][col-1] == 'M' and
                 pattern[row][col] == 'A' and pattern[row-1][col-1] == 'S' and pattern[row+1][col+1] == 'S') or
                (pattern[row+1][col-1] == 'M' and pattern[row-1][col+1] == 'M' and
                 pattern[row][col] == 'A' and pattern[row+1][col+1] == 'S' and pattern[row-1][col-1] == 'S') or
                (pattern[row+1][col+1] == 'M' and pattern[row-1][col-1] == 'M' and
                 pattern[row][col] == 'A' and pattern[row+1][col-1] == 'S' and pattern[row-1][col+1] == 'S')):
                count += 1

    return count

def read_input(file_path: str) -> list[list[str]]:
    """
    Read the input file and return a list of lists representing the word search grid.
    """
    try:
        with open(file_path, 'r') as file:
            return [list(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return []

def main():
    input_file_path = '../input/input.txt'
    pattern = read_input(input_file_path)

    if not pattern:
        return

    result = count_x_mas(pattern)
    print(f"The number of X-MAS patterns is: {result}")

if __name__ == "__main__":
    main()
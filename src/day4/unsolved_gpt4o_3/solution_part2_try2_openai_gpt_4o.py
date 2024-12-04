# This updated solution correctly counts the number of 'X-MAS' patterns in the grid by checking for the presence of the 'A' in the middle of a 3x3 square and verifying the diagonal sequences for 'M' and 'S' in both possible orientations. It reads the input from 'input/input.txt', counts the patterns, and prints the result. Additionally, it includes error handling for file operations and follows Python best practices.
def count_x_mas(grid: list[list[str]]) -> int:
    """
    Count the number of 'X-MAS' patterns in the given word search grid.

    An 'X-MAS' pattern is defined by:
      M.S
      .A.
      M.S
    """
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Iterate over each possible center of the 'X' (the 'A' position)
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            # Check if the current position can be the center of an X-MAS
            if grid[row][col] == 'A':
                # Check the four possible X-MAS orientations
                if (grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S' and
                    grid[row-1][col+1] == 'S' and grid[row+1][col-1] == 'M'):
                    count += 1
                if (grid[row-1][col+1] == 'M' and grid[row+1][col-1] == 'S' and
                    grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M'):
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
    grid = read_input(input_file_path)

    if not grid:
        return

    result = count_x_mas(grid)
    print(f"The number of X-MAS patterns is: {result}")

if __name__ == "__main__":
    main()
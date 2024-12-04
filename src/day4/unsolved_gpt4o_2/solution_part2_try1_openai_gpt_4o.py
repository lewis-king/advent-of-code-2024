# This script parses the input from the specified file, constructs a grid for the word search, and then counts the number of X-MAS patterns present in the grid. It includes error handling for file operations and ensures proper parsing of the input data.
def count_x_mas_in_grid(grid: list[list[str]], rows: int, cols: int) -> int:
    """
    Count the number of X-MAS patterns in the given grid.

    An X-MAS pattern is defined as:
      M S
       A
      M S
    or any rotation/reflection of this pattern.

    :param grid: The grid representing the word search.
    :param rows: Number of rows in the grid.
    :param cols: Number of columns in the grid.
    :return: The count of X-MAS patterns in the grid.
    """
    count = 0
    # Check for the X-MAS pattern in the grid
    for r in range(rows - 2):
        for c in range(1, cols - 1):
            # Check pattern:
            # M S
            #  A
            # M S
            if (grid[r][c-1] == 'M' and grid[r][c+1] == 'S' and
                grid[r+1][c] == 'A' and
                grid[r+2][c-1] == 'M' and grid[r+2][c+1] == 'S'):
                count += 1

            # Check pattern:
            # S M
            #  A
            # S M
            if (grid[r][c-1] == 'S' and grid[r][c+1] == 'M' and
                grid[r+1][c] == 'A' and
                grid[r+2][c-1] == 'S' and grid[r+2][c+1] == 'M'):
                count += 1

    return count


def parse_input(file_path: str) -> list[list[str]]:
    """
    Parse the input file and convert it into a grid (list of lists of characters).

    :param file_path: The path to the input file.
    :return: The grid representing the word search.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        grid = [list(line.strip()) for line in lines if line.strip()]
        return grid
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        raise
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        raise


def main():
    file_path = '../input/input.txt'
    try:
        grid = parse_input(file_path)
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        result = count_x_mas_in_grid(grid, rows, cols)
        print(f"The number of X-MAS patterns is: {result}")
    except Exception as e:
        print(f"An error occurred in the program: {e}")


if __name__ == "__main__":
    main()

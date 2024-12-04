# This updated solution enhances the pattern checking logic to account for various orientations and reflections of the X-MAS pattern. It reads the grid from the specified input file and processes the grid to count all possible X-MAS patterns, including rotated and flipped versions. The error handling ensures any issues with file reading or processing are reported.
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

            # Check pattern:
            # M
            # A S
            # M
            #  S
            if (grid[r][c] == 'M' and grid[r+1][c-1] == 'A' and
                grid[r+1][c+1] == 'S' and
                grid[r+2][c] == 'M' and c+2 < cols and grid[r+2][c+2] == 'S'):
                count += 1

            # Check pattern:
            # S
            # A M
            # S
            #  M
            if (grid[r][c] == 'S' and grid[r+1][c-1] == 'A' and
                grid[r+1][c+1] == 'M' and
                grid[r+2][c] == 'S' and c+2 < cols and grid[r+2][c+2] == 'M'):
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
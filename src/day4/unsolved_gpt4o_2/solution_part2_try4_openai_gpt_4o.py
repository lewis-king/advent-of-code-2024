# This code attempts to find the "X-MAS" patterns by checking all potential formations of the pattern in the given grid. It includes checks for both standard and mirrored orientations of the pattern. Additionally, the solution is equipped with error handling for file operations to ensure any issues with reading the input are properly reported.
def count_x_mas_in_grid(grid: list[list[str]]) -> int:
    """
    Count the number of X-MAS patterns in the given grid.

    An X-MAS pattern is defined as:
      M S
       A
      M S

    The pattern can be rotated or mirrored.

    :param grid: The grid representing the word search.
    :return: The count of X-MAS patterns in the grid.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    count = 0

    # Check for the X-MAS pattern in the grid
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check the X-MAS pattern in its standard orientation
            if (grid[r-1][c-1] == 'M' and grid[r-1][c+1] == 'S' and
                grid[r][c] == 'A' and
                grid[r+1][c-1] == 'M' and grid[r+1][c+1] == 'S'):
                count += 1

            # Check the X-MAS pattern rotated 180 degrees
            if (grid[r-1][c-1] == 'S' and grid[r-1][c+1] == 'M' and
                grid[r][c] == 'A' and
                grid[r+1][c-1] == 'S' and grid[r+1][c+1] == 'M'):
                count += 1

            # Check the X-MAS pattern mirrored vertically
            if (grid[r-1][c] == 'M' and grid[r][c-1] == 'A' and
                grid[r][c+1] == 'S' and
                grid[r+1][c] == 'M'):
                count += 1

            # Check the X-MAS pattern mirrored horizontally
            if (grid[r-1][c] == 'S' and grid[r][c-1] == 'A' and
                grid[r][c+1] == 'M' and
                grid[r+1][c] == 'S'):
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
        result = count_x_mas_in_grid(grid)
        print(f"The number of X-MAS patterns is: {result}")
    except Exception as e:
        print(f"An error occurred in the program: {e}")


if __name__ == "__main__":
    main()

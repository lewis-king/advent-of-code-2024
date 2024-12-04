# This solution counts X-MAS patterns in the grid considering all orientations: standard, 180-degree rotation, horizontal mirror, and vertical mirror. The grid is read from the input file specified in the script, and error handling is included to manage potential file access issues.
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

    # Check for the X-MAS pattern in all rotations and mirrors
    for r in range(rows):
        for c in range(cols):
            # Check if the pattern can fit inside the grid
            if r + 2 < rows and c + 2 < cols:
                # Check the X-MAS pattern in its standard orientation
                if (grid[r][c] == 'M' and grid[r][c+2] == 'S' and
                    grid[r+1][c+1] == 'A' and
                    grid[r+2][c] == 'M' and grid[r+2][c+2] == 'S'):
                    count += 1

                # Check the X-MAS pattern rotated 180 degrees (flipped)
                if (grid[r][c] == 'S' and grid[r][c+2] == 'M' and
                    grid[r+1][c+1] == 'A' and
                    grid[r+2][c] == 'S' and grid[r+2][c+2] == 'M'):
                    count += 1

            if r + 2 < rows and c - 2 >= 0:
                # Check the X-MAS pattern mirrored horizontally
                if (grid[r][c] == 'M' and grid[r][c-2] == 'S' and
                    grid[r+1][c-1] == 'A' and
                    grid[r+2][c] == 'M' and grid[r+2][c-2] == 'S'):
                    count += 1

                # Check the X-MAS pattern mirrored vertically
                if (grid[r][c] == 'S' and grid[r][c-2] == 'M' and
                    grid[r+1][c-1] == 'A' and
                    grid[r+2][c] == 'S' and grid[r+2][c-2] == 'M'):
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
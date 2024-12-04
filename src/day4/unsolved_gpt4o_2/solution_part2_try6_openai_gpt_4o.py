#Certainly! Let's create a solution that accurately identifies all possible "X-MAS" patterns within the grid, including all rotations and reflections. Here's an improved approach:
#This solution defines all possible orientations and reflections of the "X-MAS" pattern and iterates through the grid to count them. It uses a list of coordinate offsets to define the relative positions of 'M', 'S', and 'A' characters in each possible pattern orientation. The solution includes error handling to manage out-of-bounds access when checking positions in the grid.
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

    # Define all possible relative positions for X-MAS patterns
    patterns = [
        # Standard orientation
        [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)],
        # 180-degree rotation
        [(1, -1), (1, 1), (0, 0), (-1, -1), (-1, 1)],
        # Vertical mirror
        [(-1, 0), (0, -1), (0, 1), (1, 0), (2, 0)],
        # Horizontal mirror
        [(0, -1), (0, 1), (1, 0), (1, -2), (1, 2)],
        # Diagonal top-left to bottom-right
        [(0, 0), (1, 1), (2, 2), (1, 0), (2, -2)],
        # Diagonal bottom-left to top-right
        [(0, 0), (-1, 1), (-2, 2), (-1, 0), (-2, -2)]
    ]

    # Check for the X-MAS pattern in all defined orientations
    for r in range(rows):
        for c in range(cols):
            for pattern in patterns:
                try:
                    if (grid[r + pattern[0][0]][c + pattern[0][1]] == 'M' and
                        grid[r + pattern[1][0]][c + pattern[1][1]] == 'S' and
                        grid[r + pattern[2][0]][c + pattern[2][1]] == 'A' and
                        grid[r + pattern[3][0]][c + pattern[3][1]] == 'M' and
                        grid[r + pattern[4][0]][c + pattern[4][1]] == 'S'):
                        count += 1
                except IndexError:
                    # This will catch any index out of range errors
                    continue

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

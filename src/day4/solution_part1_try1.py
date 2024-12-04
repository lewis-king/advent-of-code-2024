# This script reads a word search puzzle from an input file and counts how many times the word "XMAS" appears in all possible directions. The code is well-commented, follows Python best practices, and includes error handling for file reading. It should be saved in the same directory as the `input/input.txt` file containing the puzzle input.

def read_input(file_path: str) -> list[str]:
    """Reads the input file and returns a list of strings, each representing a line in the word search."""
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found at path: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while reading the input file: {e}")


def search_word(grid: list[str], word: str) -> int:
    """Searches for all occurrences of the word in the grid in all possible directions."""
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    # Helper function to search in a direction
    def search_direction(r: int, c: int, dr: int, dc: int) -> int:
        """Searches in a specific direction and returns the count of occurrences."""
        if (0 <= r + (word_len - 1) * dr < rows) and (0 <= c + (word_len - 1) * dc < cols):
            for i in range(word_len):
                if grid[r + i * dr][c + i * dc] != word[i]:
                    return 0
            return 1
        return 0

    # Search in all 8 possible directions
    for r in range(rows):
        for c in range(cols):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                count += search_direction(r, c, dr, dc)

    return count


def main():
    # Define the path to the input file
    input_file_path = 'input/input.txt'

    # Read the input from the file
    grid = read_input(input_file_path)

    # Define the word to search for
    word_to_search = "XMAS"

    # Count the occurrences of the word in the grid
    occurrences = search_word(grid, word_to_search)

    # Print the result
    print(f"The word '{word_to_search}' appears {occurrences} times in the word search.")


if __name__ == '__main__':
    main()
from typing import List, Set, Tuple
from pathlib import Path

def read_input() -> List[str]:
    """Read and parse the input file into a list of strings."""
    try:
        input_path = Path(__file__).parent / "input" / "input.txt"
        with open(input_path) as f:
            return [line.strip() for line in f.readlines()]
    except Exception as e:
        print(f"Error reading input file: {e}")
        return []

def find_xmas_patterns(grid: List[str]) -> int:
    """
    Find all X-MAS patterns in the grid where two MAS strings form an X shape.
    MAS can be written forwards or backwards.
    """
    height = len(grid)
    width = len(grid[0])
    count = 0

    # Helper function to check if a position contains 'MAS' or 'SAM' 
    def check_mas(row: int, col: int, dr: int, dc: int) -> bool:
        if not (0 <= row < height and 0 <= col < width):
            return False
        
        chars = ""
        for i in range(3):  # MAS is 3 characters
            r, c = row + i*dr, col + i*dc
            if not (0 <= r < height and 0 <= c < width):
                return False
            chars += grid[r][c]
        
        return chars in ("MAS", "SAM")

    # Check each position as potential center of X
    for row in range(1, height-1):  # Skip edges as X needs space
        for col in range(1, width-1):
            # Check all possible combinations of MAS/SAM in X shape
            # Top-left to bottom-right and top-right to bottom-left
            directions = [
                # (top_row, top_col, bottom_row, bottom_col)
                ((-1,-1,1,1), (-1,1,1,-1)),  # Normal orientation
                ((-1,-1,1,1), (1,-1,-1,1)),  # Flip bottom
                ((1,-1,-1,1), (-1,1,1,-1)),  # Flip top
                ((1,-1,-1,1), (1,-1,-1,1))   # Flip both
            ]

            for (dr1,dc1,dr2,dc2), (dr3,dc3,dr4,dc4) in directions:
                # Check first diagonal
                if check_mas(row+dr1, col+dc1, dr2-dr1, dc2-dc1):
                    # Check second diagonal
                    if check_mas(row+dr3, col+dc3, dr4-dr3, dc4-dc3):
                        count += 1

    return count

def solve_puzzle() -> int:
    """Main function to solve the puzzle."""
    grid = read_input()
    if not grid:
        return 0
    
    return find_xmas_patterns(grid)

if __name__ == "__main__":
    result = solve_puzzle()
    print(f"Number of X-MAS patterns: {result}")
#Here's an improved solution that should correctly count X-MAS patterns:

from typing import List, Tuple
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

def is_mas(s: str) -> bool:
    """Check if string is 'MAS' or 'SAM'"""
    return s in ('MAS', 'SAM')

def check_pattern(grid: List[str], row: int, col: int, size: int) -> bool:
    """
    Check if position (row, col) is the center of an X-MAS pattern.
    Size parameter determines how far to check in each direction.
    """
    height, width = len(grid), len(grid[0])
    
    # Check boundaries
    if (row - size < 0 or row + size >= height or 
        col - size < 0 or col + size >= width):
        return False

    # Get all possible MAS strings in X pattern
    diagonals = [
        # Top-left to bottom-right
        ''.join(grid[row + i][col + i] for i in range(-size, size+1)),
        # Top-right to bottom-left
        ''.join(grid[row + i][col - i] for i in range(-size, size+1))
    ]

    # Check all possible combinations of MAS/SAM in the diagonals
    for i in range(len(diagonals[0]) - 2):
        for j in range(len(diagonals[1]) - 2):
            # Get potential MAS strings from both diagonals
            mas1 = diagonals[0][i:i+3]
            mas2 = diagonals[1][j:j+3]
            
            # Check if both strings form valid MAS/SAM
            if is_mas(mas1) and is_mas(mas2):
                # Calculate center positions of both MAS strings
                center1_row = row + (i - size + 1)
                center1_col = col + (i - size + 1)
                center2_row = row + (j - size + 1)
                center2_col = col - (j - size + 1)
                
                # Check if they form an X pattern (intersect at the middle)
                if abs(center1_row - row) == 1 and abs(center2_row - row) == 1:
                    return True
    
    return False

def count_xmas_patterns(grid: List[str]) -> int:
    """Count all valid X-MAS patterns in the grid."""
    if not grid or not grid[0]:
        return 0
    
    height, width = len(grid), len(grid[0])
    count = 0
    
    # Check each position as potential center of X
    for row in range(2, height-2):  # Skip edges as X needs space
        for col in range(2, width-2):
            if check_pattern(grid, row, col, 2):
                count += 1
    
    return count

def solve_puzzle() -> int:
    """Main function to solve the puzzle."""
    grid = read_input()
    if not grid:
        return 0
    
    return count_xmas_patterns(grid)

if __name__ == "__main__":
    result = solve_puzzle()
    print(f"Number of X-MAS patterns: {result}")

#This improved solution:

#1. Uses a more systematic approach to check for X-MAS patterns
#2. Properly checks for both MAS and SAM in both directions
#3. Ensures the pattern forms a proper X shape by verifying the center positions
#4. Handles the grid boundaries correctly
#5. Checks all possible positions where MAS/SAM strings could intersect to form an X

#The solution should now correctly count all valid X-MAS patterns where
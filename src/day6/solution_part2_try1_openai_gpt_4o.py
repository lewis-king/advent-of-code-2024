#The solution for Part 2 extends the logic of Part 1 by checking each possible position on the map to see if placing an obstacle there would cause the guard to get stuck in a loop. This involves simulating the guard's movements with the potential new obstacle in place and checking if the guard revisits the same position and direction, indicating a loop.
from typing import List, Tuple, Set

def read_input(file_path: str) -> List[str]:
    """Reads the input file and returns a list of strings representing the map."""
    try:
        with open(file_path, 'r') as file:
            return [line.rstrip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def find_guard_and_obstacles(map_data: List[str]) -> Tuple[int, int, str, Set[Tuple[int, int]]]:
    """Finds the initial position and direction of the guard and the set of obstacles."""
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    guard_pos = None
    guard_dir = None
    obstacles = set()

    for y, line in enumerate(map_data):
        for x, char in enumerate(line):
            if char in directions:
                guard_pos = (x, y)
                guard_dir = char
            elif char == '#':
                obstacles.add((x, y))

    if guard_pos is None or guard_dir is None:
        raise ValueError("Guard's initial position or direction not found in the map.")

    return guard_pos[0], guard_pos[1], guard_dir, obstacles

def simulate_guard(map_data: List[str], obstacles: Set[Tuple[int, int]]) -> int:
    """Simulates the guard's movement and returns the number of distinct positions visited."""
    guard_x, guard_y, guard_dir, _ = find_guard_and_obstacles(map_data)
    visited_positions = set()
    visited_positions.add((guard_x, guard_y))
    directions = ['^', '>', 'v', '<']
    move_offsets = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    while True:
        # Calculate the new position if the guard moves forward
        dx, dy = move_offsets[guard_dir]
        new_x, new_y = guard_x + dx, guard_y + dy

        # Check if the new position is within the map bounds
        if new_x < 0 or new_y < 0 or new_x >= len(map_data[0]) or new_y >= len(map_data):
            break

        # If there is an obstacle, turn right
        if (new_x, new_y) in obstacles:
            curr_dir_index = directions.index(guard_dir)
            guard_dir = directions[(curr_dir_index + 1) % 4]
        else:
            # Move forward and mark the new position as visited
            guard_x, guard_y = new_x, new_y
            visited_positions.add((guard_x, guard_y))

    return len(visited_positions)

def find_loop_positions(map_data: List[str]) -> int:
    """Finds all positions where placing an obstacle would cause the guard to loop."""
    guard_x, guard_y, guard_dir, obstacles = find_guard_and_obstacles(map_data)
    move_offsets = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    possible_obstacle_positions = set()

    for y in range(len(map_data)):
        for x in range(len(map_data[0])):
            if (x, y) not in obstacles and (x, y) != (guard_x, guard_y):
                # Temporarily add an obstacle
                temp_obstacles = obstacles.copy()
                temp_obstacles.add((x, y))
                
                # Check if this causes a loop
                if would_cause_loop(map_data, temp_obstacles):
                    possible_obstacle_positions.add((x, y))

    return len(possible_obstacle_positions)

def would_cause_loop(map_data: List[str], obstacles: Set[Tuple[int, int]]) -> bool:
    """Determines if the guard would get stuck in a loop with the given obstacles."""
    guard_x, guard_y, guard_dir, _ = find_guard_and_obstacles(map_data)
    visited_positions = set()
    directions = ['^', '>', 'v', '<']
    move_offsets = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

    while True:
        # Calculate the new position if the guard moves forward
        dx, dy = move_offsets[guard_dir]
        new_x, new_y = guard_x + dx, guard_y + dy

        # Check if the new position is within the map bounds
        if new_x < 0 or new_y < 0 or new_x >= len(map_data[0]) or new_y >= len(map_data):
            return False

        # If there is an obstacle, turn right
        if (new_x, new_y) in obstacles:
            curr_dir_index = directions.index(guard_dir)
            guard_dir = directions[(curr_dir_index + 1) % 4]
        else:
            # Move forward
            guard_x, guard_y = new_x, new_y

        # If we've visited this position and direction before, it's a loop
        if (guard_x, guard_y, guard_dir) in visited_positions:
            return True

        visited_positions.add((guard_x, guard_y, guard_dir))

def main():
    file_path = 'input/input.txt'
    map_data = read_input(file_path)
    if not map_data:
        return

    try:
        # Part 1
        part1_result = simulate_guard(map_data, set())
        print(f"Part 1: The guard visits {part1_result} distinct positions before leaving the mapped area.")

        # Part 2
        part2_result = find_loop_positions(map_data)
        print(f"Part 2: There are {part2_result} different positions where a new obstruction would cause the guard to get stuck in a loop.")
    except ValueError as ve:
        print(f"Error in processing map data: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
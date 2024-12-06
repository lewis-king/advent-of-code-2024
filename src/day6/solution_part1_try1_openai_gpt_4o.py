# This solution reads the map from the input file, identifies the guard's initial position and direction, and simulates the guard's movement according to the given rules. It keeps track of all distinct positions visited by the guard before exiting the boundary of the map, then prints the count of these positions.
def read_input(file_path: str) -> list[str]:
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

def find_guard_and_obstacles(map_data: list[str]) -> tuple[int, int, str, set[tuple[int, int]]]:
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

def simulate_guard(map_data: list[str]) -> int:
    """Simulates the guard's movement and returns the number of distinct positions visited."""
    guard_x, guard_y, guard_dir, obstacles = find_guard_and_obstacles(map_data)
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

def main():
    file_path = 'input/input.txt'
    map_data = read_input(file_path)
    if not map_data:
        return

    try:
        result = simulate_guard(map_data)
        print(f"The guard visits {result} distinct positions before leaving the mapped area.")
    except ValueError as ve:
        print(f"Error in processing map data: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
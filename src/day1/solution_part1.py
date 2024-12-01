def calculate_distance(filename: str) -> int:
    try:
        with open(filename, 'r') as file:
            # Separate the two lists and convert them to integers
            left_list = []
            right_list = []
            for line in file:
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)

            # Sort the lists
            left_list.sort()
            right_list.sort()

            # Calculate the total distance by summing up the absolute difference of corresponding elements
            total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))

            return total_distance

    except FileNotFoundError:
        print(f"The file {filename} does not exist!")
        return 0

    except ValueError:
        print(f"The file {filename} contains invalid data!")
        return 0

if __name__ == "__main__":
    distance = calculate_distance("input/input.txt")
    print(f"Total distance: {distance}")



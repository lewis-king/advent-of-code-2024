#To solve the problem of compacting the disk where file blocks are moved one at a time to the leftmost free space, we must ensure that only blocks from the rightmost side are moved to the leftmost free space. Here's an improved solution:

def read_input(file_path: str) -> str:
    """
    Reads the input file and returns the disk map as a string.
    """
    try:
        with open(file_path, 'r') as file:
            return file.readline().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise Exception(f"An error occurred while reading the file: {e}")

def parse_disk_map(disk_map: str) -> str:
    """
    Transforms the disk_map string into a detailed representation.
    """
    result = []
    file_id = 0
    is_file = True
    for length in map(int, disk_map):
        if is_file:
            result.append(str(file_id) * length)
            file_id += 1
        else:
            result.append('.' * length)
        is_file = not is_file
    return ''.join(result)

def compact_disk(disk: str) -> str:
    """
    Compacts the disk representation by moving file blocks one at a time to the leftmost free space.
    """
    disk_list = list(disk)
    length = len(disk_list)
    
    # Find the first free space from the left
    for leftmost_free in range(length):
        if disk_list[leftmost_free] == '.':
            break
    
    # Move blocks from right to the leftmost free space
    for i in range(length):
        rightmost_block = length - 1 - i
        if disk_list[rightmost_block] != '.':
            # Move the block to the leftmost free space
            disk_list[leftmost_free] = disk_list[rightmost_block]
            disk_list[rightmost_block] = '.'
            
            # Update the leftmost free space index
            leftmost_free += 1
            
            # Find the next free space
            while leftmost_free < length and disk_list[leftmost_free] != '.':
                leftmost_free += 1
    
    return ''.join(disk_list)

def calculate_checksum(compacted_disk: str) -> int:
    """
    Calculates the checksum of the compacted disk.
    """
    checksum = 0
    for position, char in enumerate(compacted_disk):
        if char != '.':
            checksum += position * int(char)
    return checksum

def main():
    try:
        # Read and parse the input
        disk_map = read_input('input/input.txt')
        
        # Transform the disk map into a detailed representation
        detailed_disk = parse_disk_map(disk_map)
        print(f"Detailed Disk before compaction:\n{detailed_disk}")
        
        # Compact the disk
        compacted_disk = compact_disk(detailed_disk)
        print(f"Compacted Disk:\n{compacted_disk}")
        
        # Calculate the checksum
        checksum = calculate_checksum(compacted_disk)
        
        # Print the result
        print(f"The resulting filesystem checksum is: {checksum}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

### Explanation

#1. **Reading Input**: The `read_input` function reads the disk map from the input file.

#2. **Parsing the Disk Map**: The `parse_disk_map` function converts the compact representation into a detailed disk layout using file IDs and free space.

#3. **Compacting the Disk**:
#   - The `compact_disk` function identifies the first free space from the left.
#   - It iterates from right to left, moving each file block to this free space.
#   - After each move, it updates the next leftmost free space dynamically.

#4. **Calculating the Checksum**: The `calculate_checksum` function computes the checksum by multiplying each file block's position by its ID and summing them up.

#This solution should correctly compact the disk, ensuring that blocks only move to the leftmost free space, and calculate the checksum accurately.
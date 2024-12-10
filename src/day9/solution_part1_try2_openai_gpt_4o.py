# This solution includes a step that prints both the detailed disk representation before and after compaction. By comparing the compacted disk with the expected result, you can verify whether the compacting logic is working correctly before calculating the checksum. This should help identify where any discrepancies might be occurring.
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
    Compacts the disk representation by moving file blocks to the leftmost free space.
    """
    disk_list = list(disk)
    read_pos = 0
    write_pos = 0
    
    # Shift files to the left
    while read_pos < len(disk_list):
        if disk_list[read_pos] != '.':
            disk_list[write_pos] = disk_list[read_pos]
            write_pos += 1
        read_pos += 1
    
    # Fill remaining spaces with '.'
    for i in range(write_pos, len(disk_list)):
        disk_list[i] = '.'
    
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
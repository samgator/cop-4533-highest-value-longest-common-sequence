import sys

def longest_common_sequence(data):
    # Read K
    data = data.split()
    k = int(data[0])

    # Read character values
    value = {}
    index = 1
    for _ in range(k):
        char = data[index]
        val = int(data[index + 1])
        value[char] = val
        index += 2

    # Debug reads
    print(f"K: {k}")
    print(f"Character values: {value}")

    
if __name__ == "__main__":
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        data = file.read()

    longest_common_sequence(data)
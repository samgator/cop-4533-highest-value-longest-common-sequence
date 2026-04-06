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

    # Read strings
    A = data[index]
    B = data[index + 1]

    n = len(A)
    m = len(B)

    # Initialize OPT: 2D array
    OPT = [[0] * (m + 1) for _ in range(n + 1)]

    # Debug reads
    print(f"K: {k}")
    print(f"Character values: {value}")
    print(f"A: {A}")
    print(f"B: {B}")

    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        with open(filename, 'r') as file:
            data = file.read()
    else:
        print("Provide input file as an argument")
        sys.exit(1)

    longest_common_sequence(data)
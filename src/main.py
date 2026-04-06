import sys

def longest_common_sequence(data, outputPath):
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

    # Build OPT
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Case 1: characters match
            if A[i - 1] == B[j - 1]:
                OPT[i][j] = max(
                    OPT[i - 1][j],
                    OPT[i][j - 1],
                    OPT[i - 1][j - 1] + value[A[i - 1]]
                )
            # Case 2: characters do not match
            else:
                OPT[i][j] = max(OPT[i-1][j], OPT[i][j-1])
    
    # backtracking
    hvlcs = ""
    i = n
    j = m

    while i > 0 and j > 0:
        #Match gets put at the front of the string
        if A[i-1] == B[j-1]:
            hvlcs = A[i-1] + hvlcs
            i -=1 
            j -= 1
        # no match so find the neighbor with a higher value
        elif OPT[i-1][j] >= OPT[i][j-1]:
            i-=1
        else:
            j-=1



    # Debug reads
    print(f"K: {k}")
    print(f"Character values: {value}")
    print(f"A: {A}")
    print(f"B: {B}")

    print(OPT[n][m])
    print(hvlcs)

    with open(outputPath, 'w') as f:
        f.write(str(OPT[n][m]) + "\n")
        f.write(hvlcs)

    
if __name__ == "__main__":
    if len(sys.argv) > 2:
        filename = sys.argv[1]
        outputFile = sys.argv[2]
        with open(filename, 'r') as file:
            data = file.read()

        
    else:
        print("Provide input file as an argument")
        sys.exit(1)

    longest_common_sequence(data, outputFile)
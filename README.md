# COP4533 Programming Assignment 3
## Names and IDs
- Sam Morsics - 85201061
- Jayden Ollis - 61598910

## Instructions
Our code does not need to be compiled or built.

To run the code, navigate to the /src/ directory and run: 

`python main.py [input file] [output file]`

For example, we ran the worked example from the PDF using:

`python main.py ..\input\example.in ..\output\example.out`

## Assumptions
We assume that two arguments are provided to run our program
- First argument: input file path
- Second argument: output file path

Further, we assume that input is in the format specified by the PDF:
```
K
x1 v1
x2 v2
...
xK vK
A
B
```
Where: 
- K is the number of characters in the alphabet.
- Each of the next K lines contains a character and its value.
- A is the first string.
- B is the second string.

And our program generates output in the format:
```
n
str
```
Where:
- n is an integer: the maximum value of a common subsequence of A and B.
- str is one optimal common subsequence that achieves the value of n.

## Written Component
### Question 1: Empirical Comparison
Our runtime graph is located in the `/test/` directory.

The input files used to generate the graph are located in the the `/input/` directory and were created using `generate_input.py` in the `/test/` directory.

The script used to generate our runtime graph is also located in the `/test/` directory, named `runtime_plot.py`.
### Question 2: Recurrence Equation
Let OPT[i][j] be the highest value of a common subsequence of A and B, where string A has 1 to i characters and string B has 1 to j characters. Let 1 <= i <= n and 1 <= j <= m where A has length n and B has length m. 

Base Cases: Any common subsequence with an empty string will have 0 value

OPT[i][0] = 0  for all i

OPT[0][j] = 0 for all j

Recurrence:

If the characters i and j do not match then we must find the highest value common subsequence that exists before A[i] or before B[j]

If the characters i and j match then we consider including them in the subsequence depending on what yields the highest total value. The value of the added character is added to the current best result for A[1…i-1] and B[1…j-1]. 

Mathematically put,

If A[i] != B[j] then

OPT[i][j] = {MAX(OPT[i-1][j], OPT[i][j-1])}

If A[i] = B[j] then

OPT[i][j] = {MAX(OPT[i-1][j], OPT[i][j-1], OPT[i-1][j-1] + val(A[i]))}

### Question 3: Big-Oh

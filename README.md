# COP4533 Programming Assignment 3
## Names and IDs
- Sam Morsics - 85201061
- Jayden Ollis -

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
### Question 3: Big-Oh

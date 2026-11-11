
Description
This program reads mathematical expressions from a text file (input.txt), evaluates each expression using a stack-based approach, and writes the results to output.txt.
It implements a custom Stack class and uses two stacks (one for operands and one for operators) to correctly handle operator precedence and parentheses.



How to Run the Program
Requirements
Python 3.6 or higher (no external libraries required)

Steps
Make sure the following files are in the same folder:

stack_expression_evaluator.py (the main program)
input.txt
Open a terminal / command prompt in that folder and run:
python stack_expression_evaluator.py
After execution, the results will be written to output.txt.



File Format

Input File (input.txt)

Contains one or more mathematical expressions.
Each expression is written on a single line.
Expressions are separated by a line containing only ----.

Example:

3 + 5 * 2
----
(8 / 4) + 7 * 2
----
10 - (2 + 3) * 4
----

Output File (output.txt)

Contains the results of each expression.
Results appear in the same order as the input.
Separator lines (----) are preserved.

Example corresponding output:

13
----
16
----
-10
----



Supported Operations

Operator

+
-
*
/
( )

Meaning

Addition
Subtraction
Multiplication
Division
Parentheses

Precedence

1
1
2
2
Highest


Standard operator precedence is followed (multiplication and division before addition and subtraction).

Parentheses can be used to change the order of evaluation.

Nested parentheses are supported.



Assumptions

All numbers in the expressions are non-negative integers.
Expressions are well-formed (balanced parentheses, valid operators).
Operators are binary (no unary minus such as -5 at the beginning of an expression).
Spaces around numbers and operators are allowed and ignored.
Division is performed using floating-point arithmetic, but whole-number results are displayed as integers.


Limitations

Unary negative numbers (e.g., -5 + 3) are not supported.
Decimal numbers (e.g., 3.5) are not supported.
Only the four basic arithmetic operators (+, -, *, /) are supported.
Very deeply nested parentheses may be limited by Python’s recursion/stack limits (although this implementation is iterative).
Invalid expressions or division by zero will produce an error message in the output for that expression.



Project Structure

├── stack_expression_evaluator.py   # Main program
├── input.txt                       # Sample input expressions
├── output.txt                      # Generated results
└── README.md                       # This file

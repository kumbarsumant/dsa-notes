"""
Evaluate the value of an arithmetic expression given in Reverse Polish Notation
(postfix). Each token is either an integer or one of the operators +, -, *, /.
Return the final result.

Examples:

Input: ["2", "1", "+", "3", "*"]
Output: 9

Input: ["4", "13", "5", "/", "+"]
Output: 6
"""


def compute(a, b, operator):
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a // b


def evalutate(expression):
    stack = []
    operators = {"+", "-", "*", "/"}

    for char in expression:
        if char in operators:
            operand2 = stack.pop()  # first poped element is second number
            operand1 = stack.pop()

            result = compute(operand1, operand2, char)
            stack.append(result)  # add answer to stack
        else:
            stack.append(int(char))

    if len(stack) != 0:
        return stack.pop()
    return 0


expression = ["4", "13", "5", "/", "+"]
result = evalutate(expression)
print(result)

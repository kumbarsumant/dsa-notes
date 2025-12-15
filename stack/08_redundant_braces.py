"""
Problem Statement
-----------------
Given a mathematical expression as a string, determine whether it contains
any redundant (unnecessary) braces.

A pair of braces is considered redundant if removing them does not change
the meaning of the expression. This happens when the braces do not enclose
any operator.

Return 1 if redundant braces exist, otherwise return 0.

Examples
--------
Example 1:
    Input:  expression = "(a)"
    Output: 1

Example 2:
    Input:  expression = "(a+(b*c))"
    Output: 0

Explanation:
    In Example 1, the braces around 'a' do not contain any operator, so they
    are redundant.
    In Example 2, the braces around 'b*c' contain the operator '*', so they
    are required and not redundant.
"""

# Intuition
# ---------
# Braces only matter if they enclose an operator.
# When we see a closing brace ')', we want to check if any operators exist
# inside its matching opening brace '('. A stack naturally lets us track
# the characters inside the current pair of braces.
# If we find an operator, the braces are necessary; if not, they are redundant.


def has_redundant_braces(expression):
    stack = []
    operators = "+-*/"

    for char in expression:
        if char == ")":
            has_operator = False

            while stack and stack[-1] != "(":
                popped_item = stack.pop()
                if popped_item in operators:
                    has_operator = True

            stack.pop()  # remove '('

            if not has_operator:
                return 1
        else:
            stack.append(char)

    return 0


if __name__ == "__main__":
    expression = "((a+b)+c)"
    result = has_redundant_braces(expression)
    print(result)

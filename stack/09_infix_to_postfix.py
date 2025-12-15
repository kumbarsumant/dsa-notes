"""
Problem Statement
-----------------
Convert a given infix expression (standard arithmetic notation) into its
equivalent postfix expression (Reverse Polish Notation).

The expression contains:
- Operands: lowercase letters (a-z)
- Operators: +, -, *, /, ^
- Parentheses: '(' and ')'

Postfix expression rules:
- Operands appear in the same order as in the infix expression.
- Operators appear after their operands.
- Operator precedence: ^ > * / > + -

Examples
--------
Example 1:
    Input:  expression = "a*(b+c)"
    Output: "abc+*"

Example 2:
    Input:  expression = "a+b*c"
    Output: "abc*+"
"""

# Intuition
# ---------
# - Operators with higher precedence “sit on top” of the stack.
#   When pushing a new operator, pop all operators with higher or equal
#   precedence first, then push the current one.
# - We can think of '(expression)' — a pair of parentheses and everything inside —
#   as a “special operator” with effectively the highest precedence:
#       * When pushing '(', we do not compare precedence — we just push it.
#       * When popping for ')', we pop everything inside until the matching '('.
# - Operands go directly to the result.
# - This ensures the postfix expression respects both operator precedence
#   and parentheses correctly.


def infix_to_postfix(expression):
    stack = []
    result = ""
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    for char in expression:
        if char.isalpha():  # operand
            result += char
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                result += stack.pop()
            stack.pop()  # remove '('
        else:  # operator
            while (
                stack and stack[-1] != "(" and precedence[stack[-1]] >= precedence[char]
            ):
                result += stack.pop()
            stack.append(char)

    while stack:
        result += stack.pop()

    return result


if __name__ == "__main__":
    print(infix_to_postfix("a*(b+c)"))
    print(infix_to_postfix("a+b*c"))
    print(infix_to_postfix("a^b^c"))

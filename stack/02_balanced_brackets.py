"""
Given an expression string A, check whether the pairs and the orders of
“{“,”}”, ”(“,”)”, ”[“,”]” are correct in a given input string.

Refer to the examples for more clarity.

Exmaples:

input: "{([])}"
output: 1

input: "(){"
output: 0
"""


def is_balanced(string):
    brace_dict = {"{": "}", "(": ")", "[": "]"}
    stack = []

    for brace in string:
        is_opening_brace = brace in brace_dict.keys()
        if is_opening_brace:
            stack.append(brace_dict[brace])
        else:
            if len(stack) == 0:  # example: "}"
                return 0
            if brace != stack.pop():
                return 0

    if len(stack) != 0:  # example: "{"
        return 0

    return 1


string = "{()}[][(){}]"
result = is_balanced(string)
print(result)

"""
Problem Statement
-----------------
Given a string, repeatedly remove consecutive duplicate characters.
Each time you remove a duplicate, you only remove **adjacent characters** and continue
until no more duplicates exist.

Examples
--------
Example 1:
    Input:  string = "aaabbccd"
    Output: "ad"

Example 2:
    Input:  string = "abccba"
    Output: ""
"""

# Intuition
# ---------
# - We have to check if the previous character is the same as the current.
# - That means we are going back and removing (not considering) the previous one.
# - Going back and processing previous characters is naturally handled by a stack.
# - Before pushing a character, we check if the top of the stack is the same
#   as the current:
#     - If yes, pop the top
#     - Otherwise, push the current character
# - This ensures that at the end, the stack contains exactly the characters of the
#   resulting string.


def remove_adjacent_duplicates(string):
    stack = []
    for char in string:
        if stack and char == stack[-1]:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)


if __name__ == "__main__":
    print(remove_adjacent_duplicates("aaabbccd"))
    print(remove_adjacent_duplicates("abccba"))
    print(remove_adjacent_duplicates("aabbcc"))

"""
Given an array A, for each element A[i], find the nearest greater element to its right.
If no greater element exists, return -1 for that position.

Examples:

Input: [4, 5, 2, 10, 8]
Output: [5, 10, 10, -1, -1]

Input: [3, 2, 1]
Output: [-1, -1, -1]
"""


def next_greater(arr):
    n = len(arr)
    stack = []
    result = [-1] * n  # pre-allocate -1 in all position

    for i in range(n - 1, -1, -1):
        num = arr[i]
        while stack and stack[-1] <= num:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        # if stack is empty then we have to add -1 but this is already added.

        stack.append(num)

    return result


arr = [4, 5, 2, 10, 8]
result = next_greater(arr)
print(result)

"""
Given an array A, for each element A[i], find the nearest smaller element to its
left. If no smaller element exists, return -1 for that position.

Examples:
Input: [4, 5, 2, 10, 8]
Output: [ -1, 4, -1, 2, 2 ]

Input: [3, 2, 1]
Output: [ -1, -1, -1 ]

"""


def nearest_left_small_number(arr):
    stack = []
    result = []

    for num in arr:
        # pop elements until we get strictly smaller element
        while len(stack) != 0 and stack[-1] >= num:
            stack.pop()
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(num)

    return result


arr = [4, 5, 2, 10, 8]
result = nearest_left_small_number(arr)
print(result)

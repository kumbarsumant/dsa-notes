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
    result = [-1] * len(arr)

    for i in range(len(arr)):
        num = arr[i]
        while stack and stack[-1] >= num:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        # if stack is empty, -1 has to be added this is already there

        stack.append(num)
    return result


arr = [4, 5, 2, 10, 8]
result = nearest_left_small_number(arr)
print(result)

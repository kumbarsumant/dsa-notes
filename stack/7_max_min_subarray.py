"""
Problem Statement
-----------------
Given an integer array `arr`, the value of a subarray is defined as:

    value = max(subarray) - min(subarray)

Your task is to calculate and return the sum of values of all possible
subarrays of `arr`.

Brute force would require checking all subarrays and finding max/min each time,
which is inefficient. This solution computes the result in O(n) time using
monotonic stacks.

Examples
--------
Example 1:
    Input:  arr = [4, 7, 3, 8]
    Output: 26

Explanation:
    All subarrays and their (max - min):

    [4]       -> 0
    [4,7]     -> 7 - 4 = 3
    [4,7,3]   -> 7 - 3 = 4
    [4,7,3,8] -> 8 - 3 = 5
    [7]       -> 0
    [7,3]     -> 7 - 3 = 4
    [7,3,8]   -> 8 - 3 = 5
    [3]       -> 0
    [3,8]     -> 8 - 3 = 5
    [8]       -> 0

    Sum = 26

Example 2:
    Input:  arr = [1, 2, 3]
    Output: 4
"""


# Intuition
# ---------
# Instead of calculating (max - min) for every subarray:
#
# 1. Count how many subarrays consider arr[i] as the MAX element
# 2. Count how many subarrays consider arr[i] as the MIN element
#
# Contribution of arr[i]:
#     arr[i] * counts_as_max - arr[i] * counts_as_min
#     arr[i] * (counts_as_max - counts_as_min)
#
# How do we count subarrays efficiently?
# - Use monotonic stacks to find:
#     * nearest greater element on left & right (for MAX)
#     * nearest smaller element on left & right (for MIN)
#
# Once boundaries are known:
#     subarray_count = (i - left) * (right - i)
#
# Final answer:
#     sum(max contributions) - sum(min contributions)
#
# This reduces the complexity from O(n²) to O(n).


def left_smaller(arr):
    n = len(arr)
    stack = []
    res = [-1] * n

    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res


def right_smaller(arr):
    n = len(arr)
    stack = []
    res = [n] * n

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res


def left_greater(arr):
    n = len(arr)
    stack = []
    res = [-1] * n

    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res


def right_greater(arr):
    n = len(arr)
    stack = []
    res = [n] * n

    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(i)
    return res


def subarray_count(i, left, right):
    # elements between index a, b = b - a + 1
    # use the above formula to find the subarray_count
    return (i - left) * (right - i)


def solve(arr):
    n = len(arr)

    ls = left_smaller(arr)
    rs = right_smaller(arr)
    lg = left_greater(arr)
    rg = right_greater(arr)

    max_sum = 0
    min_sum = 0

    for i in range(n):
        max_sum += arr[i] * subarray_count(i, lg[i], rg[i])
        min_sum += arr[i] * subarray_count(i, ls[i], rs[i])

    return max_sum - min_sum


if __name__ == "__main__":
    arr = [4, 7, 3, 8]
    print(solve(arr))

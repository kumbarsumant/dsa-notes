"""
Given an array of integers A.

A represents a histogram i.e A[i] denotes the height of the ith histogram's bar.
Width of each bar is 1. Find the area of the largest rectangle formed by the histogram.

Input: [2, 1, 5, 6, 1, 3]

      █
    █ █
    █ █
    █ █   █
█   █ █   █
█ █ █ █ █ █
--------------
2 1 5 6 1 3

Output: 10 (two bars 5 and 6 => min height is 5 hence 5 * 2 = 10)
"""

# Intuition:
#
# For any bar i, assume it is the smallest bar in the rectangle.
# The rectangle with height = A[i] can only extend left and right
# until we encounter a bar smaller than A[i].
#
# So for each bar, we need:
#   - the nearest smaller bar on the left
#   - the nearest smaller bar on the right
#
# These two bars act as boundaries where extension must stop.
#
# Width calculation:
#   width = right_smaller_index - left_smaller_index - 1
#
# We use:
#   -1 as the virtual index before the array (no smaller bar on the left)
#    n  as the virtual index after the array  (no smaller bar on the right)
#
# The rectangle spans only the bars strictly between these two indices.
#
# Area for bar i:
#   area = A[i] * width
#
# Using a monotonic increasing stack lets us find nearest smaller
# elements on both sides in O(n), since each bar is pushed and popped once.


def _left_nearest_small(arr):
    n = len(arr)
    result = [-1] * n  # default is -1
    stack = []

    for i in range(n):
        num = arr[i]
        while stack and arr[stack[-1]] >= num:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(i)

    return result


def _right_nearest_small(arr):
    n = len(arr)
    result = [n] * n  # default is last index (that is length)
    stack = []

    for i in range(n - 1, -1, -1):
        num = arr[i]
        while stack and arr[stack[-1]] >= num:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(i)

    return result


def max_histogram_area(arr):
    left_smaller = _left_nearest_small(arr)
    right_smaller = _right_nearest_small(arr)

    max_area = 0
    n = len(arr)

    for i in range(n):
        height = arr[i]
        width = right_smaller[i] - left_smaller[i] - 1
        area = height * width
        max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    arr = [2, 1, 5, 6, 1, 3]
    # left_smaller = [-1, -1, 1, 2, -1, 4]
    # right_smaller = [1, 6, 4, 4, 6, 6]
    result = max_histogram_area(arr)
    print(result)

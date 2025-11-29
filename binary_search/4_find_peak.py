"""
Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its neighbors.
For corner elements, we need to consider only one neighbor.

NOTE: It is guaranteed that the array contains only a single peak element.
"""

"""
Given a list of integers, find and return the peak element.
A peak element is defined as an element that is not smaller than its neighbors.
- For the first and last elements, consider only the one adjacent neighbor.
- It is guaranteed that there is exactly one peak element in the array.

Examples:
1. arr = [1, 3, 20, 4, 1]  -> peak is 20
2. arr = [10, 5, 2]        -> peak is 10
"""


def find_peak(arr):
    n = len(arr)

    # If the array has only one element, it's the peak
    if n == 1:
        return arr[0]

    # Check if the first element is a peak
    if arr[0] >= arr[1]:
        return arr[0]

    # Check if the last element is a peak
    if arr[n - 1] >= arr[n - 2]:
        return arr[n - 1]

    start = 1
    end = n - 2

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
            return arr[mid]
        elif arr[mid - 1] >= arr[mid]:
            end = mid - 1  # peak is in the left half
        else:
            start = mid + 1  # peak is in the right half

    return -1


# Example usage
arr = [1, 3, 20, 4, 1]
result = find_peak(arr)

print(result)

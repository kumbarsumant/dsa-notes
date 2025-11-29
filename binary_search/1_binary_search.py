"""
Binary Search Problem:

You are given a list of sorted and distinct integers.
Your task is to check whether a target integer exists in the list.

Requirements:
1. If the target exists, return its index.
2. If it does not exist, return -1.

Example 1 (found):
List: [1, 2, 5, 6, 7, 10, 15, 19]
Target: 10
Output: 5

Example 2 (not found):
List: [1, 2, 5, 6, 7, 10, 15, 19]
Target: 9
Output: -1
"""


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


arr = [1, 2, 5, 6, 7, 10, 15, 19]
target = 7
result = binary_search(arr, target)

print(result)

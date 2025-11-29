"""
Given a sorted list of integers that may contain duplicates, find the index of the
first occurrence of the target value. If the target is not present, return -1.

Example 1:
List: [1, 2, 2, 2, 3, 3, 4, 4, 5]
Target: 4
Output: 6

Example 2:
List: [1, 2, 2, 2, 3]
Target: 5
Output: -1
"""


def find_first_occurrence(arr, target):
    start = 0
    end = len(arr) - 1
    result = -1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            result = mid
            end = mid - 1  # still moving to left
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return result


arr = [1, 2, 2, 2, 3, 3, 4, 4, 5]
target = 4
result = find_first_occurrence(arr, target)

print(result)

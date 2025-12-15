"""
You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal
to B.
If the target value is not found and least number greater than equal to target is also
not present, return the length of array (i.e. the position where target can be placed)
"""


def sorted_insert_position(arr, target):
    n = len(arr)
    start = 0
    end = n - 1
    result = n  # assuming no element lesser than target is found

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            result = mid
            break
        elif arr[mid] > target:
            result = mid  # store the number as it can be answer when no target is found
            end = mid - 1
        else:
            start = mid + 1

    return result


arr = [2, 3, 4, 5, 7]
target = 6
result = sorted_insert_position(arr, target)
print(result)

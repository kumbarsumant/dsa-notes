"""
Given a sorted array of integers A of size N and an integer B,
where array A is rotated at some pivot unknown beforehand.

For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].

Your task is to search for the target value B in the array. If found, return its index;
otherwise, return -1.

You can assume that no duplicates exist in the array.
"""


# Algorithm:
# 1. Compute mid. If arr[mid] equals the target, return mid.
#
# 2. Otherwise, the target must lie either to the left or right of mid.
#
# 3. Determine which half of the current range is sorted.
#       Note: In a rotated array, at least one half is always sorted.
#       Reason: Only in a sorted half can we reliably check whether the
#               target falls within that numeric interval.
#
# 4. Once we identify the sorted half:
#       - If the target lies within its bounds, search that half.
#       - Otherwise, search the other half.


def search(arr, target):
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return mid

        # Check which side is sorted
        if arr[start] < arr[mid]:
            # Left half is sorted
            if arr[start] <= target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            # Right half is sorted
            if arr[mid] < target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


arr = [9, 10, 3, 5, 6, 8]
target = 5
result = search(arr, target)
print(result)

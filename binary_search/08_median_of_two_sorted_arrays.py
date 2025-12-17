"""
PROBLEM: Median of Two Sorted Arrays
------------------------------------
Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
Note: The output should be an integer (using integer division).

Examples:
1. Input: nums1 = [1, 3], nums2 = [2]
   Output: 2
   Explanation: Combined array = [1, 2, 3], median is 2.

2. Input: nums1 = [1, 2], nums2 = [3, 4]
   Output: 2
   Explanation: Combined array = [1, 2, 3, 4], median is (2 + 3) // 2 = 2.
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
The median effectively splits a dataset into two equal-sized halves.
If we can partition both arrays into a "Left Set" and a "Right Set" such that:
1. The total number of elements in the Left Set is equal to (or one greater than)
   the Right Set.
2. Every element in the Left Set is smaller than or equal to every element in the
   Right Set.

Then, we have found the correct split. We do not need to merge the arrays.
Since the arrays are sorted, we can binary search on the smaller array to find the
correct cut index. The cut for the second array is mathematically derived from the first
cut.
"""


def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> int:
    # Run binary search on the smaller array to minimize complexity O(log(min(n1, n2)))
    if len(nums1) > len(nums2):
        return find_median_sorted_arrays(nums2, nums1)  # way of switcing to smaller one

    n1, n2 = len(nums1), len(nums2)
    start, end = 0, n1

    while start <= end:
        # partition1: number of elements taken from nums1 (left side)
        partition1 = (start + end) // 2

        # partition2: number of remaining elements needed from nums2 for the left side
        # (n1 + n2 + 1) handles both odd and even lengths correctly
        partition2 = (n1 + n2 + 1) // 2 - partition1

        # If partition is 0, left side is empty -> use -infinity.
        # If partition is length, right side is empty -> use +infinity.
        max_left1 = float("-inf") if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float("inf") if partition1 == n1 else nums1[partition1]

        max_left2 = float("-inf") if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float("inf") if partition2 == n2 else nums2[partition2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (n1 + n2) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) // 2
            else:
                return int(max(max_left1, max_left2))

        elif max_left1 > min_right2:
            end = partition1 - 1
        else:
            start = partition1 + 1


if __name__ == "__main__":
    num1 = [1, 3, 8, 9, 15]
    # Fixed num2 to be strictly sorted
    num2 = [7, 11, 18, 19, 21, 25]

    # Sorted combined: [1, 3, 7, 8, 9, 11, 15, 18, 19, 21, 25]
    # Total 11 elements -> Median is 6th element (value: 11)
    result = find_median_sorted_arrays(num1, num2)
    print(f"Median: {result}")

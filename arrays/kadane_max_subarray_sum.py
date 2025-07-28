"""
Problem: Maximum Subarray Sum (Kadane's Algorithm)
Leetcode: https://leetcode.com/problems/maximum-subarray/

Statement:
Given a non empty integer array `arr`, find the contiguous subarray
(containing at least one number) which has the largest sum and return its sum.

Example:
Input: arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6.

--------------------------------------------------

Approach: Kadane's Algorithm (O(n) time, O(1) space)

1. Initialize two variables:
   - `current`: running sum ending at current index
   - `result`: max sum seen so far

2. Traverse the array:
   - At each index `i`, decide:
     Either start a new subarray at `arr[i]`, or continue the previous one:
     current = max(arr[i], current + arr[i])

   - Update the max result:
     result = max(result, current)

3. Return `result`

Edge Cases:
- Input array can have all negative numbers
- Input array can have only one element
"""


def kadane_max_subarray_sum(arr):
    n = len(arr)
    result = arr[0]
    current = arr[0]

    for i in range(1, n):
        current = max(current + arr[i], arr[i])
        result = max(result, current)
    return result


arr = [-3, 4, 1, 2, 4, -10, 11]
result = kadane_max_subarray_sum(arr)
print("result:", result)

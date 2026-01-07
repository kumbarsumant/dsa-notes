"""
Problem Statement:
Given an array 'nums' and an integer 'k', calculate the sum of the maximum
and minimum elements in every sliding window of size 'k'.

Example 1:
Input: nums = [2, 5, -1, 7, -3, -1, -2], k = 4
Output: 18
Explanation:
Window 1: [2, 5, -1, 7] -> Min: -1, Max: 7 (Sum: 6)
Window 2: [5, -1, 7, -3] -> Min: -3, Max: 7 (Sum: 4)
Window 3: [-1, 7, -3, -1] -> Min: -3, Max: 7 (Sum: 4)
Window 4: [7, -3, -1, -2] -> Min: -3, Max: 7 (Sum: 4)
Total = 6 + 4 + 4 + 4 = 18.
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
We use two monotonic deques to track the minimum and maximum of the current
window.

In the min_queue:
If the incoming element is smaller than the last element in the queue, then
that last element can never be the minimum in the current or any future
window. Therefore, we remove elements from the back until we find someone
smaller or the queue becomes empty. We keep equal elements to handle
duplicates correctly.

In the max_queue:
If the incoming element is larger than the last element in the queue, that
last element can never be the maximum. We remove from the back until we find
someone larger or equal.

Example (min_queue only): nums = [2, 5, 2], k = 3
1. [2] -> Queue: [2]
2. [2, 5] -> 5 > 2, so keep both: [2, 5]
3. [2, 5, 2] -> Incoming 2 is smaller than 5.
   5 can never be a smaller element in that window. Remove 5.
   Incoming 2 is equal to 2. Keep it. Queue: [2, 2]
The front of the queue always gives the answer for the current window.

Complexity:
- Time:  O(N)
  Each element is added and removed from the deques exactly once.
- Space: O(k)
  Deques store at most k elements.
"""

from collections import deque


def solve(nums, k):
    n = len(nums)
    min_q = deque()
    max_q = deque()

    # 1. Process the Initial Window
    for i in range(k):
        val = nums[i]
        while min_q and val < min_q[-1]:
            min_q.pop()
        min_q.append(val)

        while max_q and val > max_q[-1]:
            max_q.pop()
        max_q.append(val)

    left = 0
    right = k - 1
    total_result = 0

    # 2. Slide the window through the rest of the array
    while right < n:
        # Add min and max of current window to result
        total_result += min_q[0] + max_q[0]

        out_val = nums[left]
        left += 1
        right += 1

        if right >= n:
            break

        in_val = nums[right]

        # Remove the exiting element if it was the current min or max
        if min_q and min_q[0] == out_val:
            min_q.popleft()
        if max_q and max_q[0] == out_val:
            max_q.popleft()

        while min_q and in_val < min_q[-1]:
            min_q.pop()
        min_q.append(in_val)

        while max_q and in_val > max_q[-1]:
            max_q.pop()
        max_q.append(in_val)

    return total_result


if __name__ == "__main__":
    nums_list = [2, 5, -1, 7, -3, -1, -2]
    window_size = 4
    # Expected: 18
    print(f"Total sum of min/max: {solve(nums_list, window_size)}")

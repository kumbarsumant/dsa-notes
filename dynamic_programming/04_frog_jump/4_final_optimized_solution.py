"""
Problem Statement:
There is a frog on the 1st step of an N-step staircase. The frog is currently
at the (i)th stair and wants to reach the Nth stair.

The frog can jump either to the (i+1)th stair or the (i+2)th stair.
The cost of a jump is the absolute difference between the heights of the
stairs, i.e., |height[i] - height[j]|, where j is the stair the frog jumps to.

Find the minimum total energy used by the frog to reach from the 1st stair
to the Nth stair.

Example 1:
Input: heights = [10, 20, 30, 10]
Output: 20

Example 2:
Input: heights = [30, 10, 60, 10, 60, 50]
Output: 40
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
Looking at the Tabulation approach, we notice that to calculate the minimum
energy for the current stair 'i', we only ever refer to the results of the
two immediate previous stairs: 'i-1' and 'i-2'.


Instead of maintaining a whole array of size N, we can just use two variables:
- 'prev' to store the result of the (i-1)th stair.
- 'prev2' to store the result of the (i-2)th stair.

After calculating the result for the current stair, we shift 'prev2' to 'prev'
and 'prev' to the current result, effectively sliding our window forward.

Final Optimized State:
This is the most efficient version. We have solved the "Pain Point" of
redundant calculations (via DP) and the "Pain Point" of extra memory usage
(via Space Optimization).

Complexity:
- Time:  O(N) - Single loop from 2 to N.
- Space: O(1) - Only using two variables regardless of input size.
"""


def frog_jump(arr):
    n = len(arr)
    if n <= 1:
        return 0

    if n == 2:
        return abs(arr[1] - arr[0])

    # Variable initialization
    # prev2 represents energy for (i-2), initially step 0
    # prev represents energy for (i-1), initially step 1
    prev2 = 0
    prev = abs(arr[1] - arr[0])

    for i in range(2, n):
        # Calculate cost for current step using only the two previous values
        jump_two = prev2 + abs(arr[i] - arr[i - 2])
        jump_one = prev + abs(arr[i] - arr[i - 1])
        prev2 = prev
        prev = min(jump_one, jump_two)

    return prev


if __name__ == "__main__":
    heights = [10, 20, 30, 10]
    print(f"Minimum Energy (Space Optimized): {frog_jump(heights)}")

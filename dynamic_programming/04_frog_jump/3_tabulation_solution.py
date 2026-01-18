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
By observing the Overlapping Subproblems in the recursive approach, we moved
to Memoization. However, Memoization still carries the overhead of recursive
function calls and potential stack overflow for large N.


In Tabulation (Bottom-Up), we solve the problem iteratively. We build a 'memo'
table from the base cases (stair 0 and 1) upwards to the Nth stair. This
ensures that when we are at stair 'i', the answers for 'i-1' and 'i-2'
are already calculated and sitting in our table.

Complexity:
- Time:  O(N) - Single loop from 2 to N.
- Space: O(N) - To store the memoization table.
"""


def frog_jump(arr):
    n = len(arr)
    if n <= 1:
        return 0

    if n == 2:
        return abs(arr[1] - arr[0])

    memo = [-1] * n

    # Fill base values
    memo[0] = 0
    memo[1] = abs(arr[1] - arr[0])

    # Iteratively fill the table
    for i in range(2, n):
        jump_two = memo[i - 2] + abs(arr[i] - arr[i - 2])
        jump_one = memo[i - 1] + abs(arr[i] - arr[i - 1])
        memo[i] = min(jump_one, jump_two)

    return memo[-1]


if __name__ == "__main__":
    heights = [10, 20, 30, 10]
    print(f"Minimum Energy (Tabulation): {frog_jump(heights)}")

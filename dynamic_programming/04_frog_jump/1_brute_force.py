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
Explanation:
1. Jump from 1st to 2nd stair (|20-10| = 10), then 2nd to 4th (|10-20| = 10).
   Total = 20.
2. Jump from 1st to 3rd stair (|30-10| = 20), then 3rd to 4th (|10-30| = 20).
   Total = 40.
The minimum energy is 20.

Example 2:
Input: heights = [30, 10, 60, 10, 60, 50]
Output: 40
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
To find the minimum energy to reach the current stair (index), we consider
two possibilities:
1. The frog jumped from (index - 1).
2. The frog jumped from (index - 2).

We recursively calculate the energy for both paths and return the minimum.

Recurrence Relation:
f(i) = min(f(i-1) + abs(h[i] - h[i-1]), f(i-2) + abs(h[i] - h[i-2]))

Complexity:
- Time:  O(2^N)
- Space: O(N) (Recursive stack depth)
"""


def calculate_min_energy(arr, index):
    # Base Case 1: Already at the first step (index 0)
    if index <= 0:
        return 0

    # Base Case 2: At the second step, can only come from index 0
    if index == 1:
        return abs(arr[1] - arr[0])

    jump_one = calculate_min_energy(arr, index - 1) + abs(arr[index] - arr[index - 1])
    jump_two = calculate_min_energy(arr, index - 2) + abs(arr[index] - arr[index - 2])

    return min(jump_one, jump_two)


def frog_jump(arr):
    n = len(arr)
    return calculate_min_energy(arr, n - 1)


if __name__ == "__main__":
    # Example input
    heights = [10, 20, 30, 10]

    print(f"Minimum Energy (Brute Force): {frog_jump(heights)}")

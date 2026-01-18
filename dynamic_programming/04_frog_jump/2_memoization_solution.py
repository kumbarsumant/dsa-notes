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
In the brute-force recursive approach, we observe the presence of
"Overlapping Subproblems." For instance, to calculate the energy for
stair 4, we need the results of stair 3 and 2. To calculate stair 3,
we again need the result of stair 2.

Instead of recalculating the minimum energy for stair 2 multiple times,
we can store the result in a 'lookup' table (dictionary or array) the
first time we compute it. This technique is called Memoization (Top-Down).

Complexity:
- Time:  O(N) - Each state is calculated only once.
- Space: O(N) - For the lookup table + O(N) for the recursive stack.
"""


def calculate_min_energy(arr, index, lookup=None):
    if lookup is None:
        lookup = {}

    if index <= 0:
        return 0

    if index == 1:
        return abs(arr[1] - arr[0])

    # Check if result is already memoized
    if index in lookup:
        return lookup[index]

    # Recursive steps with lookup storage
    jump_two = calculate_min_energy(arr, index - 2, lookup) + abs(
        arr[index] - arr[index - 2]
    )
    jump_one = calculate_min_energy(arr, index - 1, lookup) + abs(
        arr[index] - arr[index - 1]
    )

    lookup[index] = min(jump_two, jump_one)
    return lookup[index]


def frog_jump(arr):
    if not arr:
        return 0
    return calculate_min_energy(arr, len(arr) - 1)


if __name__ == "__main__":
    heights = [10, 20, 30, 10]
    print(f"Minimum Energy (Memoization): {frog_jump(heights)}")

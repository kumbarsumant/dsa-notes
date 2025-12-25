"""
Problem Statement:
Given a grid of size n x m filled with non-negative integers, find a path from
the top-left corner (0, 0) to the bottom-right corner (n-1, m-1) that minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
Output: 7
Explanation: Path 1 → 3 → 1 → 1 → 1 minimizes the sum (1+3+1+1+1 = 7).

Example 2:
Input: grid = [[1, 2], [1, 1]]
Output: 3
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
Instead of working backward, we build the solution forward from the origin.
By calculating the exact cost to reach the first cell, then the entire first
row, and then the entire first column, we establish the boundaries.

With these boundaries filled, every subsequent cell has its potential
minimum-cost neighbors (top and left) already computed, allowing us to fill
the rest of the grid iteratively.

- Time:  O(N * M)
- Space: O(N * M)
"""


def min_cost_path(grid):
    n = len(grid)
    m = len(grid[0])

    memo = [[-1 for _ in range(m)] for _ in range(n)]

    # Base Case: Origin
    memo[0][0] = grid[0][0]

    # Pre-calculate first row costs
    for j in range(1, m):
        memo[0][j] = memo[0][j - 1] + grid[0][j]

    # Pre-calculate first column costs
    for i in range(1, n):
        memo[i][0] = memo[i - 1][0] + grid[i][0]

    # Calculate remaining cells
    for i in range(1, n):
        for j in range(1, m):
            min_prev_path = min(memo[i - 1][j], memo[i][j - 1])
            memo[i][j] = grid[i][j] + min_prev_path

    return memo[n - 1][m - 1]


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1],
        [60, 70, 60, 19, 1],
        [1, 1, 1, 1, 1],
        [1, 50, 40, 20, 22],
        [1, 1, 1, 1, 1],
    ]

    print(f"Minimum Path Cost: {min_cost_path(grid)}")

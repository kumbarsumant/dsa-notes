"""
Problem Statement:
Given a grid of size n x m filled with non-negative integers, find a path from
the top-left corner (0, 0) to the bottom-right corner (n-1, m-1) that minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
Output: 7
Explanation: The path 1 → 3 → 1 → 1 → 1 minimizes the sum (1+3+1+1+1 = 7).

Example 2:
Input: grid = [[1, 2], [1, 1]]
Output: 3
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
To find the minimum cost to reach the destination (n-1, m-1), we realize that
we could have only arrived there from two places: the cell directly above it
or the cell directly to its left.

If we already knew the minimum cost to reach those two neighbors, our current
cell's minimum cost is simply its own value plus the minimum of those two
incoming paths.

Special Considerations:
- Top Row: You can only arrive at these cells from the left.
- First Column: You can only arrive at these cells from the top.
- Origin (0,0): This is our starting point; its cost is simply the cell's value.


- Time:  O(2^(N+M))
- Space: O(N+M)
"""


def _get_min_cost(grid, i, j):
    # Base Case: The starting point
    if i == 0 and j == 0:
        return grid[i][j]

    # Edge Case: Top row (can only come from the left)
    if i == 0:
        return _get_min_cost(grid, i, j - 1) + grid[i][j]

    # Edge Case: First column (can only come from above)
    if j == 0:
        return _get_min_cost(grid, i - 1, j) + grid[i][j]

    # Recursive Step: Min of Top and Left
    min_cost_top_cell = _get_min_cost(grid, i - 1, j)
    min_cost_left_cell = _get_min_cost(grid, i, j - 1)

    return min(min_cost_top_cell, min_cost_left_cell) + grid[i][j]


def min_cost_path(grid):
    n = len(grid)
    m = len(grid[0])
    return _get_min_cost(grid, n - 1, m - 1)


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1],
        [60, 70, 60, 19, 1],
        [1, 1, 1, 1, 1],
        [1, 50, 40, 20, 22],
        [1, 1, 1, 1, 1],
    ]

    print(f"Minimum Path Cost: {min_cost_path(grid)}")

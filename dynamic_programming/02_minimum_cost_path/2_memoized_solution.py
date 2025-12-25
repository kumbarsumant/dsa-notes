"""
Problem Statement:
Given a grid of size n x m filled with non-negative integers, find a path from
the top-left corner (0, 0) to the bottom-right corner (n-1, m-1) that minimizes
the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
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
To reach the bottom-right cell (n-1, m-1), we must have come from either the
cell above it or the cell to its left. If we find the minimum cost to reach
those two neighbors, we can calculate the current cell's cost by adding its
value to the minimum of those two paths.

Special Considerations:
- Top Row: Can only be reached by moving right (from the left cell).
- First Column: Can only be reached by moving down (from the top cell).
- Origin (0,0): This is our entry point; its cost is just the cell's value.

By storing each calculated result in a 'memo' table, we ensure each cell is
only computed once, avoiding redundant recursive calls.

- Time:  O(N * M)
- Space: O(N * M)
"""


def _get_min_cost(grid, i, j, memo):
    # Return cached result if present
    if memo[i][j] != -1:
        return memo[i][j]

    # Base Case: Reached the starting point (0, 0)
    if i == 0 and j == 0:
        memo[i][j] = grid[i][j]
        return memo[i][j]

    # Boundary Case: Top Row (Can only come from the left)
    if i == 0:
        memo[i][j] = _get_min_cost(grid, i, j - 1, memo) + grid[i][j]
        return memo[i][j]

    # Boundary Case: First Column (Can only come from above)
    if j == 0:
        memo[i][j] = _get_min_cost(grid, i - 1, j, memo) + grid[i][j]
        return memo[i][j]

    # Recursive Step: Minimum of arriving from top vs. left
    min_cost_top_cell = _get_min_cost(grid, i - 1, j, memo)
    min_cost_left_cell = _get_min_cost(grid, i, j - 1, memo)

    memo[i][j] = min(min_cost_top_cell, min_cost_left_cell) + grid[i][j]
    return memo[i][j]


def min_cost_path(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Initialize memoization table with -1 (-1 represents uncalculated)
    memo = [[-1 for _ in range(cols)] for _ in range(rows)]

    return _get_min_cost(grid, rows - 1, cols - 1, memo)


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1],
        [60, 70, 60, 19, 1],
        [1, 1, 1, 1, 1],
        [1, 50, 40, 20, 22],
        [1, 1, 1, 1, 1],
    ]

    print(f"Minimum Path Cost: {min_cost_path(grid)}")

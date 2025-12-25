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
To calculate the cost for a cell, we only need the value above it (previous row)
and the value to its left (current row). By calculating the first row and
first column first, we create the boundaries needed to fill the rest.

Using two rows allows us to discard old data we no longer need, reducing
space from O(N*M) to O(M).

- Time:  O(N * M)
- Space: O(M)
"""


def min_cost_path(grid):
    n = len(grid)
    m = len(grid[0])

    prev_row = [-1] * m
    current_row = [-1] * m

    # Initialize first row (Boundary)
    prev_row[0] = grid[0][0]
    for j in range(1, m):
        prev_row[j] = prev_row[j - 1] + grid[0][j]

    # Process remaining rows
    for i in range(1, n):
        current_row[0] = prev_row[0] + grid[i][0]

        for j in range(1, m):
            current_row[j] = grid[i][j] + min(prev_row[j], current_row[j - 1])

        prev_row = current_row
        current_row = [-1] * m

    return prev_row[m - 1]


if __name__ == "__main__":
    grid = [
        [1, 1, 1, 1, 1],
        [60, 70, 60, 19, 1],
        [1, 1, 1, 1, 1],
        [1, 50, 40, 20, 22],
        [1, 1, 1, 1, 1],
    ]

    print(f"Minimum Path Cost: {min_cost_path(grid)}")

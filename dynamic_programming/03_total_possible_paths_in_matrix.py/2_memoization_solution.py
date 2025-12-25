"""
Problem Statement:
Given a grid of size n x m where 1 represents a wall (obstacle) and 0 represents
an empty path, find the total number of unique paths from the top-left corner
(0, 0) to the bottom-right corner (n-1, m-1).

Note: You can only move either down or right at any point in time.

Example 1:
Input: matrix = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
Output: 2

Example 2:
Input: matrix = [[0, 1], [0, 0]]
Output: 1
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
To find the total paths to reach cell (i, j), we sum up the total paths to reach
the cell directly above it and the cell directly to its left.

Rules:
- If a cell contains a wall (1), the number of paths passing through it is 0.
- The first row and first column cells can only take paths from the left
  and above respectively.
- For all other cells, the total paths is the sum of paths from the top
  and left neighbors.

Recurrence Relation:
Paths(i, j) =
    0                              if matrix[i][j] == 1
    1                              if i == 0, j == 0
    Paths(i, j-1)                  if i == 0
    Paths(i-1, j)                  if j == 0
    Paths(i-1, j) + Paths(i, j-1)  otherwise

Complexity:
- Time:  O(N * M)
- Space: O(N * M)
"""


def _find_total_possible_paths(matrix, i, j, lookup=None):
    # Dictionary is used as lookup (we can also use 2D matrix for lookup as well)
    if lookup is None:
        lookup = {}

    # Check for the solution in the lookup (cache)
    if (i, j) in lookup:
        return lookup[(i, j)]

    # 1. Wall Case: No paths possible through a wall
    if matrix[i][j] == 1:
        return 0

    # 2. Base Case: Reached the origin
    if i == 0 and j == 0:
        return 1

    # 3. Boundary Case: Top Row (Only come from the left)
    if i == 0:
        possible_paths = _find_total_possible_paths(matrix, i, j - 1, lookup)
        lookup[(i, j)] = possible_paths
        return possible_paths

    # 4. Boundary Case: First Column (Only come from above)
    if j == 0:
        possible_paths = _find_total_possible_paths(matrix, i - 1, j, lookup)
        lookup[(i, j)] = possible_paths
        return possible_paths

    # 5. General Case: Sum of paths from top and left
    total_path_top_cell = _find_total_possible_paths(matrix, i - 1, j, lookup)
    total_paths_left_cell = _find_total_possible_paths(matrix, i, j - 1, lookup)

    possible_paths = total_path_top_cell + total_paths_left_cell
    lookup[(i, j)] = possible_paths
    return possible_paths


def total_possible_paths(matrix):
    # Edge Case: If matrix is empty or the start is blocked
    if not matrix or matrix[0][0] == 1:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    return _find_total_possible_paths(matrix, n - 1, m - 1)


if __name__ == "__main__":
    # 0 = Path, 1 = Wall
    matrix = [[0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]]

    print(f"Total Possible Paths: {total_possible_paths(matrix)}")

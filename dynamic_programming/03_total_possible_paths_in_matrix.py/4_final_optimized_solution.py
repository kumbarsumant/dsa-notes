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
To find the total paths to reach cell (i, j), we sum up the paths from the
cell above it and the cell to its left.

IMPORTANT: While updating 'prev_row' or 'current_row', we must verify if the
current cell is a wall. If matrix[i][j] == 1, the path count for that cell
must be set to 0 immediately to block further propagation.

Recurrence Relation:
Paths(i, j) =
    0                              if matrix[i][j] == 1
    1                              if i == 0, j == 0
    Paths(i, j-1)                  if i == 0
    Paths(i-1, j)                  if j == 0
    Paths(i-1, j) + Paths(i, j-1)  otherwise

- Time:  O(N * M)
- Space: O(M)
"""


def total_possible_paths(matrix):
    # Check if starting point is blocked or matrix is empty
    if not matrix or matrix[0][0] == 1:
        return 0

    n = len(matrix)
    m = len(matrix[0])

    prev_row = [-1] * m
    current_row = [-1] * m

    # Base Case: Starting point
    prev_row[0] = 1

    # While updating prev_row (First Row), check for wall case
    for j in range(1, m):
        if matrix[0][j] == 1:
            prev_row[j] = 0
        else:
            prev_row[j] = prev_row[j - 1]

    for i in range(1, n):
        # While updating current_row (First Column), check for wall case
        if matrix[i][0] == 1:
            current_row[0] = 0
        else:
            current_row[0] = prev_row[0]

        # While updating current_row (Remaining cells), check for wall case
        for j in range(1, m):
            if matrix[i][j] == 1:
                current_row[j] = 0
            else:
                current_row[j] = prev_row[j] + current_row[j - 1]

        prev_row = current_row
        current_row = [-1] * m

    return prev_row[m - 1]


if __name__ == "__main__":
    # 0 = Path, 1 = Wall
    matrix = [[0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]]

    print(f"Total Possible Paths: {total_possible_paths(matrix)}")

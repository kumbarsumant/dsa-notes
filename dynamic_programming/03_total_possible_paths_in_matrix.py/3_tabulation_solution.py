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
We build the solution from the origin forward. We first determine the paths
for the boundaries (first row and column). If a cell is a wall, it contributes
0 paths. Otherwise, it inherits the path count from the only available direction.

Once the boundaries are set, the value of any internal cell is simply the sum
of paths from the cell above it and the cell to its left.

Recurrence Relation:
Paths(i, j) =
    0                          if matrix[i][j] == 1
    1                          if i == 0, j == 0
    Paths(i, j-1)              if i == 0
    Paths(i-1, j)              if j == 0
    Paths(i-1, j) + Paths(i, j-1)  otherwise

Complexity:
- Time:  O(N * M)
- Space: O(N * M)
"""


def total_possible_paths(matrix):
    if not matrix or matrix[0][0] == 1:
        return 0

    n = len(matrix)
    m = len(matrix[0])

    memo = [[-1 for _ in range(m)] for _ in range(n)]

    # Base Case: Starting point
    memo[0][0] = 1

    # Initialize first row
    for j in range(1, m):
        if matrix[0][j] == 1:  # Wall case
            memo[0][j] = 0
        else:
            memo[0][j] = memo[0][j - 1]

    # Initialize first column
    for i in range(1, n):
        if matrix[i][0] == 1:  # Wall case
            memo[i][0] = 0
        else:
            memo[i][0] = memo[i - 1][0]

    # Fill remaining cells
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:  # Wall case
                memo[i][j] = 0
            else:
                # Total paths = sum of paths from top and left
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

    return memo[n - 1][m - 1]


if __name__ == "__main__":
    # 0 = Path, 1 = Wall
    matrix = [[0, 0, 1, 0, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0]]

    print(f"Total Possible Paths: {total_possible_paths(matrix)}")

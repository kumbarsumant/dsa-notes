"""
Problem Statement:
Given a list of squares where each square is represented by [x, y, side_length],
find a horizontal line y = k such that the total area of the squares below the
line is equal to the total area of the squares above the line.

The answer should be accurate within a precision of 10^-5.

Example:
Input: squares = [[0, 0, 1], [2, 2, 1]]
Output: 1.50000
Explanation: Total area is 1 + 1 = 2. Line y = 1.5 gives 1 unit area below
(the first square) and 1 unit area above (the second square).
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
The total area of all squares is constant. As we move a horizontal line 'y'
from the bottom-most point to the top-most point, the area trapped below
the line increases monotonically.

This monotonic property (Area increases as Y increases) allows us to Binary
Search for the specific 'y' coordinate where:
    Area_Below(y) * 2 >= Total_Area

For any square starting at 'yi' with side 'l', the area below a line 'y' is:
    - 0 if y <= yi
    - l * l if y >= yi + l
    - l * (y - yi) if yi < y < yi + l
This is simplified as: side * min(max(0, y - yi), side)

Complexity:
- Time:  O(N * log(Search_Space / precision))
  Where N is the number of squares. The binary search runs roughly
  log2((ymax - ymin) / 10^-5) times.
- Space: O(1)
"""


def get_area_below(squares, ymid):
    area = 0
    for _, y, side in squares:
        if ymid > y:
            # Calculate height of the square covered below ymid
            height_below = min(ymid - y, side)
            area += height_below * side
    return area


def solve(squares):
    ymin = float("inf")
    ymax = -float("inf")
    total_area = 0

    for _, y, side in squares:
        total_area += side * side
        ymin = min(ymin, y)
        ymax = max(ymax, y + side)

    low = ymin
    high = ymax
    precision = 1e-5

    # Binary Search on a continuous range
    # Using a fixed number of iterations (e.g., 100) is also a common trick
    # to guarantee precision, but while high - low > eps is standard.
    while high - low > precision:
        mid = (low + high) / 2

        # If area below mid is at least half of total, try a lower line
        if get_area_below(squares, mid) * 2 >= total_area:
            high = mid
        else:
            low = mid

    return high


if __name__ == "__main__":
    test_squares = [[0, 0, 1], [2, 2, 1]]
    # Expected: 1
    print(f"Dividing line y = {solve(test_squares):.5f}")

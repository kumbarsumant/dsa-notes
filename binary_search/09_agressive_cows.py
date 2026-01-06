"""
Problem Statement:
You are given an array 'stalls' representing positions on a straight line
and an integer 'n' (total cows). Assign cows to stalls such that the
minimum distance between any two of them is as large as possible.

Example 1:
Input: stalls = [1, 2, 4, 8, 9], n = 3
Output: 3
Explanation: Place cows at 1, 4, and 8. Min distance is 3.
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
The answer (the largest minimum distance) exists within a defined range.
If we can place all 'n' cows with a minimum gap of 'd', then any gap
smaller than 'd' is also possible. This creates a monotonic 'Yes/No'
pattern, which is the trigger to use Binary Search on the possible
distance (the search space).

Complexity:
- Time:  O(N log N + N log(search_space))
  Where search_space = (max_stall_pos - min_stall_pos).
  Sorting takes O(N log N). Binary search runs log(search_space) times,
  and each check takes O(N).
- Space: O(1)
"""


def is_possible(stalls, n, mid_dist):
    count = 1  # Place the first cow
    last_pos = stalls[0]

    for i in range(1, len(stalls)):
        # If the current stall is far enough from the last placed cow
        if stalls[i] - last_pos >= mid_dist:
            count += 1
            last_pos = stalls[i]

            # If we've successfully placed all n cows
            if count >= n:
                return True
    return False


def solve(stalls, n):
    stalls.sort()
    num_stalls = len(stalls)

    # Calculate the lower bound
    min_gap = float("inf")
    for i in range(1, num_stalls):
        min_gap = min(min_gap, stalls[i] - stalls[i - 1])

    low = min_gap
    high = stalls[-1] - stalls[0]
    result = low

    while low <= high:
        mid = (low + high) // 2

        # If mid distance is possible, we try to push for a larger gap
        if is_possible(stalls, n, mid):
            result = mid
            low = mid + 1
        else:
            # If mid distance isn't possible, we must reduce the gap
            high = mid - 1

    return result


if __name__ == "__main__":
    stalls_pos = [1, 2, 4, 8, 9]
    total_cows = 3
    # Expected Output: 3
    print(f"Largest minimum distance: {solve(stalls_pos, total_cows)}")

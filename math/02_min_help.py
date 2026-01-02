"""
Problem Statement:
Alex starts with a score of 0 and wants to reach exactly 'target'. He has two
possible moves:
1. Double his current score (Cost: 0 help)
2. Add 1 to his current score (Cost: 1 help from Sam)

Return the minimum number of times Alex needs Sam's help.

Example 1:
Input: target = 5
Output: 2
Explanation: 0 -> 1 (Sam) -> 2 (Double) -> 4 (Double) -> 5 (Sam). Total = 2.

Example 2:
Input: target = 8
Output: 1
Explanation: 0 -> 1 (Sam) -> 2 (Double) -> 4 (Double) -> 8 (Double). Total = 1.
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
Since doubling an integer always results in an even number, Alex can never
reach an odd score on his own. Whenever the target (or current intermediate
score) is odd, it serves as a signal that Sam's help was mandatory to reach
that specific value. Working backwards, we identify these 'odd' hurdles to
count the minimum help required.

Complexity:
- Time:  O(log2(target))
- Space: O(1)
"""


def min_sam_help(target):
    sam_help_count = 0
    current_score = target

    while current_score > 0:
        # If the current value is odd, Need to take help from Sam
        if current_score % 2 != 0:
            sam_help_count += 1
        current_score //= 2

    return sam_help_count


if __name__ == "__main__":
    target_val = 5
    # Expected: 2
    print(f"Minimum help needed for {target_val}: {min_sam_help(target_val)}")

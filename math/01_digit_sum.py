"""
Problem Statement:
Given a non-negative integer 'num', calculate the sum of its digits.

Example 1:
Input: num = 1234
Output: 10
Explanation: 1 + 2 + 3 + 4 = 10.

Example 2:
Input: num = 98
Output: 17
"""

# =============================================================================
# INTUITION
# =============================================================================

"""
Intuition:
To find the sum of digits, we need to extract each digit one by one starting
from the right (the units place).

1. Use the Modulo operator (%) with 10 to get the last digit of the number.
2. Add that digit to a running sum.
3. Use Integer Division (//) by 10 to remove that last digit from the number.
4. Repeat these steps until the number becomes zero.

Complexity:
- Time:  O(log10(num))
  The number of iterations is equal to the number of digits in num.
- Space: O(1)
  We only use a single variable to store the sum.
"""


def digit_sum(num):
    total_sum = 0

    while num:
        # Extract the last digit
        last_digit = num % 10
        total_sum += last_digit

        # Remove the last digit
        num //= 10

    return total_sum


if __name__ == "__main__":
    test_num = 1234
    # Expected: 1 + 2 + 3 + 4 = 10
    print(f"Digit sum of {test_num}: {digit_sum(test_num)}")

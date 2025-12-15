"""
Given a positive integer n, find the floor square root for the given number.

Examples:
1. n = 4  -> floor square root is 2
2. n = 8  -> floor square root is 2
"""


def square_root(n):
    start = 1  # positive integer starts from 1
    end = n  # taking n for n = 1 case
    result = n

    while start <= end:
        mid = start + (end - start) // 2

        if mid * mid == n:
            result = mid
            break
        elif mid * mid < n:
            result = mid  # store the result as it can be possible
            start = mid + 1  # move right to check further possibility
        else:
            end = mid - 1

    return result


n = 4
result = square_root(n)

print(result)

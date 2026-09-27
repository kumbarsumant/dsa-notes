# Link: https://neetcode.io/solutions/contains-duplicate

# Brute Force:
# Compare all pairs via nested loops -> Time: O(n^2), Space: O(1)


# Sorting:
# Sort list, check adjacent elements -> Time: O(nlogn), Space: O(1)


def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        else:
            seen.add(num)
    return False





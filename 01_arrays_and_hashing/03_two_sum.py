# https://neetcode.io/solutions/two-sum

# Brute force:
# Add each pairs and check if it equals target
# Time: O(n^2), Space: O(1)

# Sorting:
# Sort the numbers, use left and right pointer, move left or right pointer comparing the sum with target
# Time: O(nlogn), Space: O(1)

def two_sum(nums, target):
    seen_map = dict()

    for index, num in enumerate(nums):
        diff = target - num
        if diff in seen_map:
            return [seen_map[diff], index]
        else:
            seen_map[num] = index

    return [-1, -1]

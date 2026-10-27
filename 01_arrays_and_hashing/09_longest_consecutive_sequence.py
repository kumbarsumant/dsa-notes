class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_length = 0

        # iterate over the set and not list, to avoid the repeated work on duplicate
        # numbers
        for num in nums_set:
            # `num` shouldn't have any left neighbour
            # to be at the starting point of a sequence
            if num - 1 not in nums_set:
                next_num = num + 1
                length = 1 # `num` is already considered hence length = 1
                while next_num not in nums_set:
                    length += 1
                    next_num += 1
                max_length = max(max_length, length)
        return max_length

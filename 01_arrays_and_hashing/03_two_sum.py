class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hmap = dict()

        ans = [-1, -1]
        for index, num in enumerate(nums):
            if target - num in hmap:
                ans[0], ans[1] = hmap[target - num], index
                break
            else:
                hmap[num] = index
        return ans

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n

        for i in range(n):
            result[i] = 1 if i == 0 else result[i-1] * nums[i-1]

        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right_prod
            right_prod *= nums[i]

        return result

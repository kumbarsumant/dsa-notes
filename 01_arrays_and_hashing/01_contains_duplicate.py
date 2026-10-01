class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        memmory = set()

        for num in nums:
            if num in memmory:
                return True
            else:
                memmory.add(num)

        return False



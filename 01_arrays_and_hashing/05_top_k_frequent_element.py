class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hmap = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # freqency map
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        # frequency list (index as the freqency count)
        for num, count in hmap.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result

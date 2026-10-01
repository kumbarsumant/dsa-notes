class Solution:
    def transform_str_to_arr(self, string):
        arr = [0] * 26
        for char in string:
            arr[ord(char) - ord('a')] += 1
        return arr

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hmap = {}
        for string in strs:
            arr = self.transform_str_to_arr(string)
            tup = tuple(arr)
            if tup in hmap:
                hmap[tup].append(string)
            else:
                hmap[tup] = [string]

        return list(hmap.values())

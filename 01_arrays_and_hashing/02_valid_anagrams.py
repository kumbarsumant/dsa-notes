class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # build the hasmap
        hmap = dict()

        # add counts
        for letter in s:
            hmap[letter] = hmap.get(letter, 0) + 1

        # subtract counts
        for letter in t:
            if letter not in hmap:
                return False
            hmap[letter] -= 1

        # check count
        for count in hmap.values():
            if count != 0:
                return False

class Solution:
    def encode(self, strs):
        result = []
        for word in strs:
            result.append(str(len(word)))
            result.append("#")
            result.append(word)
        return "".join(result)


    def decode(self, s: str):
        i = 0
        result = []
        while i < len(s):
            j = i
            length_str = ""
            while s[j] != "#":
                length_str += s[j]
                j += 1
            length = int(length_str)

            # now j is at #
            start_index = j + 1
            end_index = j + length
            word = s[start_index : end_index + 1]
            result.append(word)

            i = end_index + 1
        return result

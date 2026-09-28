# https://neetcode.io/solutions/group-anagrams

# Brute Force:
# Already seen anagrams takes O(n) where n is the lenght of strings. We can add them to hasmap. If the key and string are anagram add it to the of that key else add it as a new key...
# Time: O(n^2 * m), Space: O(n + m), where n = length of the list, m = length of each string


# Sorting:
# Sort each individual strings, now you just have to check if that string there in the hasmap, if yes then add to list for that key, else add as a new key
# Time: O(n * mlogm), Space: O(n) where n = length of the list, m = length of each string


def transform_str_to_arr(string):
    arr = [0] * 26 # 26 alphabets, only smalll case used in the problem
    for char in string:
        arr[ord(char) - ord('a')] += 1
    return arr


def group_anagrams(strs):
    hmap = {}
    for string in strs:
        arr = transform_str_to_arr(string)
        tup = tuple(arr)
        if tup in hmap:
            hmap[tup].append(string)
            break
        else:
            hmap[tup] = [string]
    return list(hmap.values())

### 1. Contains Duplicate

[Neetcode Link](https://neetcode.io/solutions/contains-duplicate)
[Python File](./01_contains_duplicate.py)

- **Pattern:** Hash Set
- **Trigger:** The problem asks to check for uniqueness or find if any value appears at least twice.
- **Complexity:** O(N) Time, O(N) Space.
- **Core Trick:** Use a `set()` to track seen numbers during the loop. If the current number is already in the set, a duplicate exists.

### 2. Valid Anagram

[NeetCode Solution](https://neetcode.io/solutions/valid-anagram)
[Python File](./02_valid_anagrams.py)

- **Pattern:** Frequency Count (Hash Map)
- **Trigger:** Check if two strings use the same letters the same number of times.
- **Complexity:** O(N) Time, O(1) Space
- **Core Trick (simple):** If lengths differ return False. Count letters in the first string, subtract while scanning the second. If any count goes negative or any count left over, it's not an anagram.

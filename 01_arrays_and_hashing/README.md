### 1. Contains Duplicate

[NeetCode](https://neetcode.io/solutions/contains-duplicate) |
[Python File](./01_contains_duplicate.py)

- **Pattern:** Hash Set (Seen/Unseen, Unique)
- **Trigger:** The problem asks to check for uniqueness or find if any value appears at least twice.
- **Complexity:** O(N) Time, O(N) Space.
- **Core Trick:** Use a `set()` to track seen numbers during the loop. If the current number is already in the set, a duplicate exists. Also a simple approach, convert list to set and compare their lengths.

### 2. Valid Anagram

[NeetCode](https://neetcode.io/solutions/valid-anagram) |
[Python File](./02_valid_anagrams.py)

- **Pattern:** Frequency Count (Hash Map)
- **Trigger:** Check if two strings use the same letters the same number of times.
- **Complexity:** O(N) Time, O(N) Space
- **Core Trick (simple):** If lengths differ return False. Count letters in the first string, subtract while scanning the second. If any count goes negative or any count left over, it's not an anagram.

### 3. Two Sum

[NeetCode](https://neetcode.io/solutions/two-sum) |
[Python File](./03_two_sum.py)

- **Pattern:** Hash Map (Seen/Unseen with index reference)
- **Trigger:** `target - current_num` is the required number. If we have already seen this required number, we can easily find our answer.
- **Complexity:** O(N) Time, O(N) Space
- **Core Trick:** `target - current_num` is the number we need. If this number was already seen during our pass, then both of their indices form the answer. We can use a hash map here with the number as the key and its index as the value.

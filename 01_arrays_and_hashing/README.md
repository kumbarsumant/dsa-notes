### 1. Contains Duplicate

[Neetcode Link](https://neetcode.io/solutions/contains-duplicate)
[Python File](./01_contains_duplicate.py)

- **Pattern:** Hash Set
- **Trigger:** The problem asks to check for uniqueness or find if any value appears at least twice.
- **Complexity:** O(N) Time, O(N) Space.
- **Core Trick:** Use a `set()` to track seen numbers during the loop. If the current number is already in the set, a duplicate exists.

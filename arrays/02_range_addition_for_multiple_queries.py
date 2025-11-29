"""
Problem: Range Addition with Suffix Updates

You are given an array of size n, initially filled with zeros.
You are also given multiple queries in the form (i, x), where:
- i is the starting index
- x is the value to add

Each query means: add x to all elements from index i to the end of the array.

Return the final state of the array after applying all the queries.

Example:
n = 5
queries = [(1, 3), (0, 2), (4, 2)]

Step-by-step changes:
Initial:  [0, 0, 0, 0, 0]
Query 1:  [0, 3, 3, 3, 3]
Query 2:  [2, 5, 5, 5, 5]
Query 3:  [2, 5, 5, 5, 7]

Final result: [2, 5, 5, 5, 7]

Optimized Approach: Prefix Sum Trick

Steps:
1. Initialize an array of size n with all zeros.
2. For each query (i, x), update result[i] += x.
   This is like building a difference array where we apply x at the start of
   the range.
3. After all queries are applied, compute the prefix sum over the array.
   This ensures each value x gets propagated from index i to the end.

Why this works:
- Instead of updating every index from i to n-1 in each query (which is slow),
  we delay the full update and use prefix sum to simulate the effect
  efficiently.

Time Complexity: O(n + q), where q is the number of queries
Space Complexity: O(n)
"""


def compute_prefix_sum(arr):
    result = []
    current = 0
    for num in arr:
        current += num
        result.append(current)
    return result


def range_addition_for_multiple_queries(queries, n):
    result = [0] * n
    for start_index, val in queries:
        result[start_index] += val
    return compute_prefix_sum(result)


# Example usage
if __name__ == "__main__":
    queries = [(1, 3), (0, 2), (4, 2)]
    n = 5
    final_array = range_addition_for_multiple_queries(queries, n)
    print("result:", final_array)  # Output: [2, 5, 5, 5, 7]

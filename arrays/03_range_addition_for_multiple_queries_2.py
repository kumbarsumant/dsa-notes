"""
Problem: Range Addition with Start and End Indices

You are given an array of size n, initially filled with zeros.
Each query is a tuple (start, end, val), meaning:
- Add 'val' to all elements from index 'start' to index 'end' (inclusive)

Return the final state of the array after applying all the queries.

Example:
n = 7
queries = [
    (1, 3, 2),
    (2, 5, 3),
    (5, 6, -1),
    (2, 4, 2)
]

Step-by-step updates (naive view for understanding):
Initial:      [0, 0, 0, 0, 0, 0, 0]
After 1st:    [0, 2, 2, 2, 0, 0, 0]
After 2nd:    [0, 2, 5, 5, 3, 3, 0]
After 3rd:    [0, 2, 5, 5, 3, 2, -1]
After 4th:    [0, 2, 7, 7, 5, 2, -1]

Final result: [0, 2, 7, 7, 5, 2, -1]

Optimized Approach: Difference Array + Prefix Sum

Steps:
1. Initialize an array of size n with all zeros.
2. For each query (start, end, val):
    - Add val at index 'start'
    - Subtract val at index 'end + 1' (if within bounds)
3. After all queries, compute prefix sum to apply the final values.

Why this works:
- This efficiently simulates a range update in O(1) time per query.
- The prefix sum spreads the difference values across the array.

Time Complexity: O(n + q), where q is number of queries
Space Complexity: O(n)
"""


def compute_prefix_sum(arr):
    result = []
    sum = 0
    for num in arr:
        sum += num
        result.append(sum)
    return result


def range_addition_for_multiple_queries(queries, n):
    result = [0] * n

    for start_index, end_index, val in queries:
        result[start_index] += val
        if end_index + 1 < n:  # check end_index condition
            result[end_index + 1] -= val

    return compute_prefix_sum(result)


# Example usage
if __name__ == "__main__":
    queries = [(1, 3, 2), (2, 5, 3), (5, 6, -1), (2, 4, 2)]
    n = 7
    final_array = range_addition_for_multiple_queries(queries, n)
    print("Result:", final_array)  # Output: [0, 2, 7, 7, 5, 2, -1]

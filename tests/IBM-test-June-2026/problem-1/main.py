#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   June 26th, 2026

IBM Problem #1: Count Increasing Triplets

Given an integer array arr of length n, count how many
strictly increasing subsequences of length 3 can be formed.

A valid triplet uses indices i, j, k where:
    i < j < k
    arr[i] < arr[j] < arr[k]

Return the result modulo 1,000,000,007.

Example:
    [1, 2, 3, 4, 1] -> 4
    [3, 1, 4, 5]    -> 2

Constraints:
    1 <= n <= 5000
    0 <= arr[i] <= 10^9

------------------------------------------------------
Time & Space Complexity: Coordinate Compression + Fenwick Trees
------------------------------------------------------
Let:           n = len(arr), u = number of unique values

Time Complexity:  O(n log u)  | Each value updates/queries Fenwick trees
Space Complexity: O(u)        | Compressed ranks plus two Fenwick trees
------------------------------------------------------

********************************************************
"""

MOD = 10**9 + 7


class Solution:
    @staticmethod
    def countIncreasingTriplets(arr):
        """
        Count strictly increasing subsequences of length 3.

        @param arr: The list of integers to search for increasing triplets.
        @result: Number of valid triplets modulo 1,000,000,007.
        """

        # Compress large values into compact 1-based ranks.
        # This lets Fenwick trees index values up to 10^9 safely.
        sorted_values = sorted(set(arr))
        rank = {value: i + 1 for i, value in enumerate(sorted_values)}
        unique_count = len(sorted_values)

        class Fenwick:
            def __init__(tree_obj, size):
                """
                Store prefix counts with efficient point updates.

                @param size: Number of compressed value ranks.
                @result: A Fenwick tree initialized with all counts set to 0.
                """

                tree_obj.tree = [0] * (size + 2)

            def add(tree_obj, index, delta):
                """
                Add delta to one compressed rank.

                @param index: 1-based compressed rank to update.
                @param delta: Amount to add, usually +1 or -1.
                @result: Updates the tree in place.
                """

                while index < len(tree_obj.tree):
                    tree_obj.tree[index] += delta
                    index += index & -index

            def sum(tree_obj, index):
                """
                Count how many stored values have rank <= index.

                @param index: 1-based compressed rank boundary.
                @result: Prefix count from rank 1 through index.
                """

                total = 0

                while index > 0:
                    total += tree_obj.tree[index]
                    index -= index & -index

                return total

        left_tree = Fenwick(unique_count)
        right_tree = Fenwick(unique_count)

        # Start with every number on the right side.
        # As we scan, each number moves from right -> middle -> left.
        for value in arr:
            right_tree.add(rank[value], 1)

        triplets = 0

        for middle_value in arr:
            middle_rank = rank[middle_value]

            # Current value is the middle, so remove it from the future side.
            right_tree.add(middle_rank, -1)

            # Pick one smaller value before it and one greater value after it.
            left_smaller = left_tree.sum(middle_rank - 1)
            right_greater = (
                right_tree.sum(unique_count)
                - right_tree.sum(middle_rank)
            )

            triplets = (triplets + left_smaller * right_greater) % MOD

            # Current value can be used as the left element for later triplets.
            left_tree.add(middle_rank, 1)

        return triplets


def main() -> None:
    """
    Run a few quick examples for local verification.

    @param: None.
    @result: Prints each test result beside its expected answer.
    """

    sol = Solution()

    # Test 1: problem example with four valid triplets
    # print(sol.countIncreasingTriplets([1, 2, 3, 4, 1]))    # 4

    # Test 2: problem example with two valid triplets
    # print(sol.countIncreasingTriplets([3, 1, 4, 5]))       # 2

    # Test 3: duplicates do not count as strictly increasing
    print(sol.countIncreasingTriplets([1, 2, 2, 3]))        # 2


if __name__ == "__main__":
    main()

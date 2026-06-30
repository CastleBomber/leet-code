#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   June 28th, 2026

HackerRank
IBM Problem #1: Count Increasing Triplets

Given an integer array arr, count how many strictly
increasing subsequences of length 3 can be formed

A valid triplet uses indixes i,j,k where:
I < J < K
arr[i] < arr[j] < arr[k]

REturn the result modulo 1,00,000,007

Example:
    [1,2,3,4,1] -> 4
    [3,1,4,5] -> 2

Constraints:
    1 <= n <= 5000
    0 <= arr[i] <= 10^9



------------------------------------------------------
Time & Space Complexity: Coordinate compression + finwick trees
------------------------------------------------------
Let: n= len(arr), u = number of unique values

Time Complexity: O(n log u) | Query/update each value twice
Space complexity: O(u) | Two fenwick trees
------------------------------------------------------

********************************************************
"""

import sys

MOD = 10**9 + 7

def add(bit: list[int], i: int, delta: int) -> None:
    """
    Add delta at one Fenwick index.
    @param detla: Amount to add at index i
    @result: Updates bit in place
    """

    while i < len(bit):
        bit[i] += delta
        i += i & -1

def prefix(bit: list[int], i: int) -> int:
    """
    Count values with compressed index <= i

    @param bit: Fenwick tree storing value counts
    @param i: 1-based compressed prefix boundary
    @result: Number of stored values from 1 through i
    """

    total = 0

    while i > 0:
        total += bit[i]
        i -= i & -i

    return total

def countIncreasingTriplets(arr: list[int]) -> int:
    """
    Count strictly increasing subsequences of length 3

    @param arr: List of integers to search
    @result: Number of valid triplets modulo 1,000,000,007
    """

    if len(arr) < 3:
        return 0
    
    vals = sorted(set(arr))
    rank = {x: i + 1 for i, x in enumerate(vals)}
    m = len(vals)

    left = [0] * (m + 2)
    right = [0] * (m + 2)

    # Everything starts to the right of the middle pointer
    for x in arr:
        add(right, rank[x], 1)

    ans = 0

    for x in arr:
        r = rank[x]

        # Move current value into the middle position
        add(right, r, -1)

        smaller = prefix(left, r - 1)
        greater = prefix(right, m) - prefix(right, r)

        ans = (ans + smaller * greater) % MOD

        # Current value becomes available for future left choices
        add(left, r, 1)

    return ans

def main() -> None:
    # Test 1: problem example with four valid triplets
    # print(countIncreasingTriplets([1, 2, 3, 4, 1]))    # 4

    # Test 2: problem example with two valid triplets
    # print(countIncreasingTriplets([3, 1, 4, 5]))       # 2

    # Test 3: duplicates do not count as strictly increasing
    print(countIncreasingTriplets([1, 2, 2, 3]))        # 2

main()



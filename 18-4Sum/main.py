#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   July 18th, 2026

    LeetCode: #18 4Sum
    URL: https://leetcode.com/problems/4sum/

    Given an array nums of n integers, return an array of all the unique
    quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

        0 <= a, b, c, d < n
        a, b, c, and d are distinct.
        nums[a] + nums[b] + nums[c] + nums[d] == target

    You may return the answer in any order.

    Example 1:
        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

    Example 2:
        Input: nums = [2,2,2,2,2], target = 8
        Output: [[2,2,2,2]]

    Constraints:
        1 <= nums.length <= 200
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9

    Usage: python3 ./main.py

    Solution: 
        Accepted - 295 / 295 testcases passed

    ------------------------------------------------------
    Time & Space Complexity: Nested Two-Pointer Search
    ------------------------------------------------------
    Let:
        n = len(nums)
        q = number of unique quadruplets stored in result

    Sorting:           O(n log n)
    Candidate Search:  O(n^3)
    Duplicate Check:   O(q) per match | Linear search through result

    Time Complexity:   O(n^3 * q)      | O(n^6) worst case when q = O(n^3)
    Space Complexity:  O(n + q)        | Sorted copy plus returned results
    ------------------------------------------------------

*********************************************************
"""

from typing import Optional, List, Dict, Tuple, Set, Deque, DefaultDict, Any
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappush, heappop, heapify, heappushpop, heapreplace
from itertools import combinations, permutations, product, accumulate
from functools import lru_cache, cache, reduce, cmp_to_key
from bisect import bisect_left, bisect_right, insort
from math import gcd, lcm, ceil, floor, sqrt, inf, comb, factorial
from string import ascii_lowercase, ascii_uppercase, digits
import math
import heapq
import bisect
import itertools
import functools
import operator
import copy
import re
import sys
import os


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        nums = sorted(nums)

        for i in range(len(nums) - 2):
            for j in range(len(nums) - 2):
                left = i + j + 2
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums [i+j+1] + nums[left] + nums[right]

                    # Found a match
                    if total == target:
                        value = [nums[i], nums [i+j+1], nums[left], nums[right]]

                        if value not in result:
                            result.append(value)

                    if total < target:
                        left += 1       # Increase the total
                    else:
                        right -= 1      # Decrese the total



        return result


if __name__ == "__main__":
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    expected1 = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    expected2 = [[2, 2, 2, 2]]

    sol = Solution()
    result1 = sol.fourSum(nums1, target1)
    # result2 = sol.fourSum(nums2, target2)

    print(f"Example 1 result:   {result1}")
    print(f"Example 1 expected: {expected1}")
    print()
    # print(f"Example 2 result:   {result2}")
    # print(f"Example 2 expected: {expected2}")

#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   October 11th, 2026

    LeetCode: #27 Remove Element
    URL: https://leetcode.com/problems/remove-element/

    Problem statement (paraphrased):
        Modify the integer array nums in place to exclude every occurrence
        of val. Return k, the count of retained elements. Store those
        elements in nums[:k]; their order is unrestricted. Entries beyond
        that prefix and the array's final size do not affect correctness.

    Custom judge behavior:
        The judge supplies nums, val, and a sorted expected array without
        val. It calls removeElement, checks that k equals the expected
        length, sorts the first k entries, and compares each against the
        expected array. Every check must succeed.

    Example 1:
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums = [2,2,_,_]
        Explanation: Return 2 and place two 2s in the leading positions.
        Underscores denote ignored entries.

    Example 2:
        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums = [0,1,4,0,3,_,_,_]
        Explanation: Return 5. The prefix must contain 0, 0, 1, 3, and 4
        in any order; subsequent entries are ignored.

    Constraints:
        0 <= nums.length <= 100
        0 <= nums[i] <= 50
        0 <= val <= 100

    Usage: python3 ./main.py
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
    def __repr__(self) -> str:
        """Show a compact label in the debugger"""
        return "Solution"

    def removeElement(self, nums: List[int], val: int) -> int:
        # TODO: Implement the solution
        return 0


if __name__ == "__main__":
    nums1 = [3, 2, 2, 3]
    val1 = 3
    expected1 = 2
    expected_nums1 = [2, 2]

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    expected2 = 5
    expected_nums2 = [0, 1, 4, 0, 3]

    sol = Solution()
    result1 = sol.removeElement(nums1, val1)
    result2 = sol.removeElement(nums2, val2)

    print(f"Example 1 result k:        {result1}")
    print(f"Example 1 expected k:      {expected1}")
    print(f"Example 1 nums after call: {nums1}")
    print(f"Example 1 actual prefix:   {nums1[:result1]}")
    print(f"Example 1 expected prefix: {expected_nums1} (any order)")
    print()
    print(f"Example 2 result k:        {result2}")
    print(f"Example 2 expected k:      {expected2}")
    print(f"Example 2 nums after call: {nums2}")
    print(f"Example 2 actual prefix:   {nums2[:result2]}")
    print(f"Example 2 expected prefix: {expected_nums2} (any order)")

#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   September 30th, 2026

    LeetCode: #26 Remove Duplicates from Sorted Array
    URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Given an integer array nums sorted in non-decreasing order, remove the
    duplicates in-place such that each unique element appears only once. The
    relative order of the elements should be kept the same.

    Let k be the number of unique elements in nums. After removing the
    duplicates, return k.

    The first k elements of nums should contain the unique numbers in sorted
    order. The remaining elements beyond index k - 1 can be ignored.

    Custom Judge:
        The judge calls removeDuplicates(nums), verifies that the returned k
        equals the expected length, and compares the first k elements of nums
        with the expected unique values.

    Example 1:
        Input: nums = [1,1,2]
        Output: 2, nums = [1,2,_]
        Explanation: Return k = 2, with 1 and 2 as the first two elements.
                     Values beyond the returned k do not matter.

    Example 2:
        Input: nums = [0,0,1,1,1,2,2,3,3,4]
        Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
        Explanation: Return k = 5, with 0, 1, 2, 3, and 4 as the first five
                     elements. Values beyond the returned k do not matter.

    Constraints:
        1 <= nums.length <= 3 * 10^4
        -100 <= nums[i] <= 100
        nums is sorted in non-decreasing order.

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
        """Avoid Python's noisy default debugger representation."""
        return "Solution"

    def removeDuplicates(self, nums: List[int]) -> int:
        result = 0

        return result


if __name__ == "__main__":
    nums1 = [1, 1, 2]
    expected_k1 = 2
    expected_nums1 = [1, 2]

    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_k2 = 5
    expected_nums2 = [0, 1, 2, 3, 4]

    sol = Solution()
    result1 = sol.removeDuplicates(nums1)
    result2 = sol.removeDuplicates(nums2)

    print(f"Example 1 k result:    {result1}")
    print(f"Example 1 k expected:  {expected_k1}")
    print(f"Example 1 nums result: {nums1[:result1]}")
    print(f"Example 1 nums expected: {expected_nums1}")
    print()
    print(f"Example 2 k result:    {result2}")
    print(f"Example 2 k expected:  {expected_k2}")
    print(f"Example 2 nums result: {nums2[:result2]}")
    print(f"Example 2 nums expected: {expected_nums2}")

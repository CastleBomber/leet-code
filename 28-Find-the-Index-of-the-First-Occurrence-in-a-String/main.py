#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   October 11th, 2026

    LeetCode: #28 Find the Index of the First Occurrence in a String
    URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

    Given two strings needle and haystack, 
    return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.

    Example 1:
        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0

    Example 2:
        Input: haystack = "leetcode", needle = "leeto"
        Output: -1

    Constraints:
        1 <= haystack.length, needle.length <= 10^4
        haystack and needle consist of only lowercase English characters.

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

    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        
        # Check on the needle and haystack sizes
        if len(needle) > len(haystack):
            return -1

        for i in range(0, len(haystack)):
            j = 0
            letters_matched = 0

            while j < len(needle) and needle[j] == haystack[i+j]:
                letters_matched = letters_matched + 1
                j = j + 1

            if letters_matched == len(needle):
                return i

        return -1


if __name__ == "__main__":
    haystack1 = "sadbutsad"
    needle1 = "sad"
    expected1 = 0

    haystack2 = "leetcode"
    needle2 = "leeto"
    expected2 = -1

    haystack3 = "mississippi"
    needle3 = "issip"
    expected3 = 4

    sol = Solution()
    # result1 = sol.strStr(haystack1, needle1)
    #result2 = sol.strStr(haystack2, needle2)
    result3 = sol.strStr(haystack3, needle3)

    # print(f"Example 1 result:   {result1}")
    # print(f"Example 1 expected: {expected1}")
    # print()
    # print(f"Example 2 result:   {result2}")
    # print(f"Example 2 expected: {expected2}")
    print()
    print(f"Example 3 result:   {result3}")
    print(f"Example 3 expected: {expected3}")

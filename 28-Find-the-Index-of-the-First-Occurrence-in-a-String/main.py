#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   October 11th, 2026

    LeetCode: #28 Find the Index of the First Occurrence in a String
    URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

    Problem statement (paraphrased):
        Locate needle within haystack and return its earliest starting
        index (zero-based). Return -1 when no matching substring exists.

    Example 1:
        Input: haystack = "sadbutsad", needle = "sad"
        Output: 0
        Explanation: Matches begin at positions 0 and 6; choose 0 because
        it is the earlier position.

    Example 2:
        Input: haystack = "leetcode", needle = "leeto"
        Output: -1
        Explanation: There is no matching substring, so the result is -1.

    Constraints:
        Each string has between 1 and 10,000 characters, inclusive.
        Both strings use lowercase English letters exclusively.

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
        # TODO: Implement the solution
        return -1


if __name__ == "__main__":
    haystack1 = "sadbutsad"
    needle1 = "sad"
    expected1 = 0

    haystack2 = "leetcode"
    needle2 = "leeto"
    expected2 = -1

    sol = Solution()
    result1 = sol.strStr(haystack1, needle1)
    result2 = sol.strStr(haystack2, needle2)

    print(f"Example 1 result:   {result1}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {result2}")
    print(f"Example 2 expected: {expected2}")

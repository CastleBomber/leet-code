#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   August 24th, 2026

    LeetCode: #20 Valid Parentheses
    URL: https://leetcode.com/problems/valid-parentheses/

    Given a string s containing just the characters
      '(', ')', '{', '}', '['and ']', 
    determine if the input string is valid.

    An input string is valid if:
        1. Open brackets must be closed by the same type of brackets.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.

    Example 1:
        Input: s = "()"
        Output: true

    Example 2:
        Input: s = "()[]{}"
        Output: true

    Example 3:
        Input: s = "(]"
        Output: false

    Example 4:
        Input: s = "([])"
        Output: true

    Example 5:
        Input: s = "([)]"
        Output: false

    Constraints:
        1 <= s.length <= 10^4
        s consists of parentheses only '()[]{}'.

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
    def isValid(self, s: str) -> bool:
        result = False
        stack = []

        # Check that the # elements is not odd
        if len(s) % 2 == 1:
            return result
        
        brackets = set("()[]{}")

        # Check that each character is a valid
        for c in s:
            if c not in brackets:
                return result

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
            "(": ")",
            "[": "]",
            "{": "}",
        }

        # Split in half for string comparison
        middle = len(s) // 2
        left = s[:middle]
        right = s[middle:]
        right = right[::-1] # flip for easy comparisons

        # Check that the halves have mirrored pairings
        for i in range(len(left)):
            if pairs.get(left[i]) != right[i]:
                return result

        result = True

        return result


if __name__ == "__main__":
    s1 = "()"
    expected1 = True

    s2 = "()[]{}"
    expected2 = True

    s3 = "(]"
    expected3 = False

    s4 = "([])"
    expected4 = True

    s5 = "([)]"
    expected5 = False

    sol = Solution()
    result1 = sol.isValid(s1)
    result2 = sol.isValid(s2)
    result3 = sol.isValid(s3)
    result4 = sol.isValid(s4)
    result5 = sol.isValid(s5)

    print(f"Example 1 result:   {result1}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {result2}")
    print(f"Example 2 expected: {expected2}")
    print()
    print(f"Example 3 result:   {result3}")
    print(f"Example 3 expected: {expected3}")
    print()
    print(f"Example 4 result:   {result4}")
    print(f"Example 4 expected: {expected4}")
    print()
    print(f"Example 5 result:   {result5}")
    print(f"Example 5 expected: {expected5}")

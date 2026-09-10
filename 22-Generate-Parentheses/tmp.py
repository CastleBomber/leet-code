#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   September 4th, 2026

    LeetCode: #22 Generate Parentheses
    URL: https://leetcode.com/problems/generate-parentheses/

    Given n pairs of parentheses, write a function to generate all
    combinations of well-formed parentheses.

    Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

    Example 2:
        Input: n = 1
        Output: ["()"]

    Constraints:
        1 <= n <= 8

    ------------------------------------------------------
    Time & Space Complexity: Intended Valid Construction
    ------------------------------------------------------
    Let:               Cn = nth Catalan number

    Algorithm:         Build each string one symbol at a time while
                       preventing closers from exceeding openers

    Time Complexity:   O(n * Cn)  | Build every valid 2n-symbol string
    Space Complexity:  O(n * Cn)  | Store results plus an O(n) path
    ------------------------------------------------------

    Usage: python3 ./tmp.py


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
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        # Base string
        start = "()"

        if n == 1:
            return [start]

        start = "()" * n

        for _ in range(n):
            # Build string
            build = ""
            for _ in range(n):
                build.append("(")
            # Add to result
            result.append("x")

        # Rule: must have an opener, an it must have a closer



        return result


if __name__ == "__main__":
    n1 = 3
    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]

    n2 = 1
    expected2 = ["()"]

    sol = Solution()
    result1 = sol.generateParenthesis(n1)
    result2 = sol.generateParenthesis(n2)

    print(f"Example 1 result:   {result1}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {result2}")
    print(f"Example 2 expected: {expected2}")

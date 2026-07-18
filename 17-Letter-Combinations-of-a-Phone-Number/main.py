#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   July 17th, 2026

    LeetCode: #17 Letter Combinations of a Phone Number
    URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

    Given a string containing digits from 2-9 inclusive, return all possible
    letter combinations that the number could represent. Return the answer in
    any order.

    A mapping of digits to letters (just like on the telephone buttons) is
    given below. Note that 1 does not map to any letters.

        2: abc    3: def
        4: ghi    5: jkl    6: mno
        7: pqrs   8: tuv    9: wxyz

    Example 1:
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

    Example 2:
        Input: digits = "2"
        Output: ["a","b","c"]

    Constraints:
        1 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9'].

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

phone_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combos = []
        result = []

        for digit in digits:
            if digit in phone_map:
                combos.append(phone_map[digit])


        for i in range(len(combos)):
            print("x")
            self.backtrack(combos, 0, "")
            

        return result
    
    def backtrack(self, combos, index, path):
        if index == len(digits):
            combos.append(path)
            return

        current_digit = digits[index]
        letters = phone_map[current_digit]

        for letter in letters:
            self.backtrack(combos, index + 1, path + letter)

    

if __name__ == "__main__":
    digits1 = "23"
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    digits2 = "2"
    expected2 = ["a", "b", "c"]

    sol = Solution()
    result1 = sol.letterCombinations(digits1)
    result2 = sol.letterCombinations(digits2)

    print(f"Example 1 result:   {result1}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {result2}")
    print(f"Example 2 expected: {expected2}")

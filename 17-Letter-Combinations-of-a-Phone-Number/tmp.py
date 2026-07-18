#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   July 17th, 2026

LeetCode: #17 Letter Combinations of a Phone Number
URL: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2 through 9, return every
possible letter combination represented by those telephone buttons.
Return the combinations in any order.

Digit Mapping:
    2: abc    3: def
    4: ghi    5: jkl    6: mno
    7: pqrs   8: tuv    9: wxyz

Examples:
    digits = "23"  -> ["ad", "ae", "af", "bd", "be", "bf",
                       "cd", "ce", "cf"]
    digits = "2"   -> ["a", "b", "c"]
    digits = ""    -> []

Constraints:
    0 <= len(digits) <= 4
    Each character is a digit from 2 through 9.

------------------------------------------------------
Time & Space Complexity: Backtracking
------------------------------------------------------
Let: n = len(digits), c = number of combinations

Time complexity: O(n * c) | Build every n-letter combination
Space complexity: O(n * c) | Store results plus an O(n) path
------------------------------------------------------

********************************************************
"""

from typing import List 

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate every letter combiantion represented by the digits

        @param digits: String containing digits from 2 through 9 
        @results: List of all possible letter combinations
        """

        if not digits:
            return []
        
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



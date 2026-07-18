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
Let:               n = len(digits), c = number of combinations

Time Complexity:   O(n * c)  | Build every n-letter combination
Space Complexity:  O(n * c)  | Store results plus an O(n) path
------------------------------------------------------

********************************************************
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Generate every letter combination represented by the digits

        @param digits: String containing digits from 2 through 9
        @result: List of all possible letter combinations
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

        result = []
        path = []

        def backtrack(index: int) -> None:
            """
            Build combinations one digit at a time

            @param index: Position of the digit currently being processed
            @result: None, completed combinations are added to result
            """
            if index == len(digits):
                result.append("".join(path))
                return

            # Try each letter mapped to the current digit
            for letter in phone_map[digits[index]]:
                path.append(letter)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: two digits
    print(sol.letterCombinations("23"))  # [ad, ae, af, bd, be, bf, cd, ce, cf]

    # Test 2: one digit
    # print(sol.letterCombinations("2"))  # [a, b, c]

    # Test 3: empty input
    # print(sol.letterCombinations(""))   # []

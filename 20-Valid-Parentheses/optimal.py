#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   August 29th, 2026

LeetCode: #20 Valid Parentheses
URL: https://leetcode.com/problems/valid-parentheses/

Given a string containing only parentheses, brackets, and braces,
determine whether every opening bracket is closed by the same type
in the correct order.

Examples:
    s = "()"      -> True
    s = "()[]{}"  -> True
    s = "(]"      -> False
    s = "([])"    -> True
    s = "([)]"    -> False

Constraints:
    1 <= len(s) <= 10^4
    s contains only the characters ()[]{}.

------------------------------------------------------
Time & Space Complexity: Stack
------------------------------------------------------
Let:               n = len(s)

Time Complexity:   O(n)  | Examine each bracket once
Space Complexity:  O(n)  | Store unmatched opening brackets
------------------------------------------------------

********************************************************
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determine whether all brackets close in the correct order

        @param s: String containing only bracket characters
        @result: True when the bracket sequence is valid
        """
        matching_openers = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for bracket in s:
            if bracket not in matching_openers:
                stack.append(bracket)
                continue

            # A closer must match the most recent unmatched opener
            if not stack or stack[-1] != matching_openers[bracket]:
                return False

            stack.pop()

        # Any remaining opener was never closed
        return not stack


if __name__ == "__main__":
    sol = Solution()

    # Test 1: valid nesting with every bracket type
    print(sol.isValid("{[()]}"))  # True

    # Test 2: closing brackets appear in the wrong order
    # print(sol.isValid("([)]"))  # False

    # Test 3: closing bracket has no opening bracket
    # print(sol.isValid("]"))     # False

    # Test 4: opening brackets remain unmatched
    # print(sol.isValid("(("))    # False

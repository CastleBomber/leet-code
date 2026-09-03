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
    def __repr__(self) -> str:
        """Show a compact value in the debugger."""
        return "Solution"

    def isValid(self, s: str) -> bool:
        """
        Determine whether all brackets close in the correct order

        @param s: String containing only bracket characters
        @result: True when the bracket sequence is valid
        """

        # Holds closing symbols
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for symbol in s:
            # The symbol is an opener
            if symbol not in pairs:
                stack.append(symbol)
                continue

            # A closer must match the most recent unmatched opener
            # The stack is empty or
            # The latest opening bracket is the wrong type
            if not stack or stack[-1] != pairs[symbol]:
                return False

            stack.pop()

        # Returns False if any opening symbols remain unmatched
        return False if stack else True


if __name__ == "__main__":
    sol = Solution()

    # Test 1: valid nesting with every bracket type
    #print(sol.isValid("{[()]}"))  # True

    # Test 2: closing brackets appear in the wrong order
    #print(sol.isValid("([)]"))  # False

    # Test 3: closing bracket has no opening bracket
    #print(sol.isValid("]"))     # False

    # Test 4: opening brackets remain unmatched
    print(sol.isValid("(("))    # False

#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   September 9th, 2026

LeetCode: #22 Generate Parentheses
URL: https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, generate every combination of
well-formed parentheses.

Examples:
    n = 3  -> ["((()))", "(()())", "(())()", "()(())", "()()()"]
    n = 1  -> ["()"]

Constraints:
    1 <= n <= 8

------------------------------------------------------
Time & Space Complexity: Recursion + Backtracking
------------------------------------------------------
Let:               Cn = nth Catalan number

Time Complexity:   O(n * Cn)  | Build every valid string of length 2n
Space Complexity:  O(n * Cn)  | Store results plus an O(n) active path
------------------------------------------------------

********************************************************
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generate every well-formed arrangement of n parenthesis pairs

        @param n: Number of parenthesis pairs
        @result: List of every valid parenthesis string
        """
        result = []
        path = []

        def backtrack(open_count: int, close_count: int) -> None:
            """
            Build valid strings one parenthesis at a time

            @param open_count: Number of opening parentheses in the path
            @param close_count: Number of closing parentheses in the path
            @result: None, completed strings are added to result
            """
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            # Add an opener while unused pairs remain
            if open_count < n:
                path.append("(")
                backtrack(open_count + 1, close_count)
                path.pop()

            # Add a closer only when it matches an existing opener
            if close_count < open_count:
                path.append(")")
                backtrack(open_count, close_count + 1)
                path.pop()

        backtrack(0, 0)
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: standard example with multiple nesting patterns
    print(sol.generateParenthesis(3))
    # ["((()))", "(()())", "(())()", "()(())", "()()()"]

    # Test 2: minimum input
    # print(sol.generateParenthesis(1))  # [()]

    # Test 3: deeper branching with fourteen valid results
    # print(sol.generateParenthesis(4))  # 14 combinations

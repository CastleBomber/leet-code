#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   April 17th, 2026

    LeetCode: #9 Palindrome Number

    Given an integer x, return true if x is a palindrome, and false otherwise.

    Example 1:
        Input: x = 121
        Output: true
        Explanation: 121 reads as 121 from left to right and from right to left.


    Example 2:
        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

    Example 3:
        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    

    Constraints:
        -231 <= x <= 231 - 1

    Solution
        Accepted - 11511 / 11511 testcases passed


*********************************************************
"""

from typing import Optional, List, Dict, Tuple, Set
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappush, heappop, heapify
import math
import bisect
import itertools
import functools

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)

        halfwayPoint = len(s) // 2

        pStart = 0
        pEnd = len(s) - 1

        while pStart < halfwayPoint:
            if s[pStart] != s[pEnd]:
                return False
            
            pStart += 1
            pEnd -= 1
            
        return True

if __name__ == "__main__":
    x1 = 121
    x2 = -121
    x3 = 10
    x4 = 11

    sol = Solution()
    result = sol.isPalindrome(x4)

    print(result)



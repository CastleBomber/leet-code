#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   April 14th, 2026

    LeetCode: #7 Reverse Integer

    Given a signed 32-bit integer x, return x with its digits reversed. 
    If reversing x causes the value to go outside the 
    signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers 
    (signed or unsigned).

 
    Example 1:
        Input: x = 123
        Output: 321

    Example 2:
        Input: x = -123
        Output: -321
    
    Example 3:
        Input: x = 120
        Output: 21
    
    Constraints:
        -231 <= x <= 231 - 1
        



    Usage:
        python3 main.py

    Solution:
        Accepted - 1045 / 1045 testcases passed    
    

    Notes:

        32-BIT SIGNED INTEGER LIMITS
        ------------------------------------
        Minimum   | -2,147,483,648  | -2^31
        Maximum   |  2,147,483,647  |  2^31 - 1
        ------------------------------------

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
    def reverse(self, x: int) -> int:
        # Handle any leading negative "-"
        if x < 0:
            isNegative = True
            x = abs(x)
        else:
            isNegative = False
            
        # Convert to string
        s = str(x)
        s = s[::-1]

        # Handle leading 0's
        s = str(int(s))

        # Prepend "-" to front if it was used
        if isNegative:
            s = "-" + s

        lowest = -2147483647
        highest = 2147483647

        # Handle overflow
        s = int(s)
        if s > highest or s < lowest:
            s = 0
        
        return s


if __name__ == "__main__":
    x = 1534236469
    sol = Solution()
    result = sol.reverse(x)

    print(result)

#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 7th, 2026
    Purpose: Prepping for IBM coding test

    LeetCode: #1446 Consecutive Characters

    The power of the string is the maximum length of a non-empty substring 
    that contains only one unique character.

    Given a string s, return the power of s.

    Example 1:
        Input: s = "leetcode"
        Output: 2
        Explanation: The substring "ee" is of length 2 with the character 'e' only.
   
    Example 2:
        Input: s = "abbcccddddeeeeedcba"
        Output: 5
        Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
        
    Constraints:
        1 <= s.length <= 500
        s consists of only lowercase English letters.

    Usage:
        python3 main.py

    Notes:
        TIME AND SPACE COMPLEXITY: Single Pass Scan
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Single loop through the string of length n.
                                    Each character is examined once; operations are constant-time.
    Space Complexity | O(1)       | Only a fixed number of integer variables (power, count, i)
                                    and a character variable (tmp) are used.
                                    No additional data structures depend on input size.
    ----------------------------------------------------

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
    def maxPower(self, s: str) -> int:
        power = 0
        count = 0
        i = 0
        tmp = s[0]

        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        while i < len(s):
            cur = s[i]
            if cur == tmp:
                count += 1
            else:
                count = 1
            if count > power:
                    power = count
            tmp = cur
            i += 1
            
        return power
        


if __name__ == "__main__":
    s1 = "leetcode"
    s2 = "abbcccddddeeeeedcba"
    s3 = "tourist"
    s4 = "cc"

    sol = Solution()

    print(sol.maxPower(s4))      
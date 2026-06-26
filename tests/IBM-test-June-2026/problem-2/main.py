#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   June 23rd, 2026

IBM Problem #2: Maximum Cost to Segregate a Binary String

You are given a binary string s containing only '0' and '1'.

The string is considered segregated when all '1' characters
appear after all '0' characters.

In other words, every '1' must be to the right of every '0'.

------------------------------------------------------
Operation:

Choose a '1' character and move it rightward until it reaches
either:

     1. The end of the string
     2. The next '1' character

Each '1' must be moved to its furthest possible position to the
right whenever it is chosen.

------------------------------------------------------
Cost:

The cost of one operation is:

     1 + number of positions the '1' moved

------------------------------------------------------
Goal:

Compute the maximum total cost achievable while transforming
the string into a segregated string.

------------------------------------------------------
Example:

Input:
     s = "10100"

One optimal strategy:

     1. Swap the second and third characters
        Cost = 2
        Result: "11000"

     2. Swap the first and second characters
        Cost = 2
        Result: "01100"

     3. Move each '1' to the end
        Cost = 3 + 3
        Result: "00011"

Output:
     8

------------------------------------------------------
Sample Case 0:

Input:
     s = "10100"

Output:
     8

Explanation:
     One optimal way is:

         "10100" -> "01100" -> "00110" -> "00011"

     The operation costs are 2, 3, and 3.

------------------------------------------------------
Sample Case 1:

Input:
     s = "01110"

Output:
     6

Explanation:
     One optimal way is:

         "01110" -> "01011" -> "00111"

     Each operation has cost 3.

------------------------------------------------------
Constraints:

     1 <= length of s <= 10^5
     Each character of s is either '0' or '1'

Quick:
    Move 1's to the right
    Move 0's to the left

    Cost of operation:
    1 + (number of postions the '1' moved)

******************************************************
"""

from typing import Optional, List, Dict, Tuple, Set
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappush, heappop, heapify
import math
import bisect
import itertools
import functools
import os
import random
import re
import sys

class Solution:
    def getMaxCost(s):
        ones = 0
        cost = 0
        in_zero_block = False

        for ch in s:
            if ch == '1':
                ones += 1

                # A new 1 means the next zero starts a new zero-block
                in_zero_block = False

            else:
                # Every previous 1 must cross this 0
                cost += ones

                # Add operation cost once per zero-block:
                # each earlier 1 can be moved separately for max cost
                if ones > 0 and not in_zero_block:
                    cost += ones
                    in_zero_block = True

        return cost


if __name__ == "__main__":
    s1 = "10100" # Output: 8
    s2 = "01110" # Output: 6

    sol = Solution()

    print(sol.getMaxCost(s1))      
#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   June 23rd, 2026

    IBM - Problem #1

    Move 1's to the right
    Move 0's to the left

    Cost of operation:
    1 + (number of postions the '1' moved)

*********************************************************
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
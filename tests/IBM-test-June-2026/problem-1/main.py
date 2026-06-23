#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   June 23rd, 2026

    IBM - Problem #1

    Strictly increasing subsequences

    Indices:
    arr[i] < arr[j] < arr[k]


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
#import requests
from itertools import combinations

class Solution:
    def countIncreasingTriplets(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        # Coordinate compression: map big values to small ranks
        sorted_vals = sorted(set(arr))
        rank = {val: i + 1 for i, val in enumerate(sorted_vals)}
        size = len(sorted_vals)

        class Fenwick:
            def __init__(self, size):
                self.tree = [0] * (size + 2)

            def add(self, index, value):
                while index < len(self.tree):
                    self.tree[index] += value
                    index += index & -index

            def sum(self, index):
                total = 0
                while index > 0:
                    total += self.tree[index]
                    index -= index & -index
                return total

        left_tree = Fenwick(size)
        right_tree = Fenwick(size)

        # Put all numbers into right_tree first
        for num in arr:
            right_tree.add(rank[num], 1)

        count = 0

        for num in arr:
            r = rank[num]

            # Current num is now the middle element, so remove it from right side
            right_tree.add(r, -1)

            # Numbers before current that are smaller
            left_smaller = left_tree.sum(r - 1)

            # Numbers after current that are greater
            right_greater = right_tree.sum(size) - right_tree.sum(r)

            count = (count + left_smaller * right_greater) % MOD

            # Add current num to left side
            left_tree.add(r, 1)

        return count


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 1] # Output: 4
    arr2 = [3,1,4,5] # Output: 2

    sol = Solution()

    print(sol.countIncreasingTriplets(arr2))      
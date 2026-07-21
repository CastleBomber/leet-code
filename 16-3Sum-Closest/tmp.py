#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   July 11th, 2026

    LeetCode: #16 3Sum Closest
    URL: https://leetcode.com/problems/3sum-closest/

    Given an integer array nums of length n and an integer target,
    find three integers at distinct indices in nums such that the sum is
    closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.

    Example 1:
        Input: nums = [-1,2,1,-4], target = 1
        Output: 2
        Explanation: The sum that is closest to the target is 2.
                     (-1 + 2 + 1 = 2).

    Example 2:
        Input: nums = [0,0,0], target = 1
        Output: 0
        Explanation: The sum that is closest to the target is 0.
                     (0 + 0 + 0 = 0).

    Constraints:
        3 <= nums.length <= 500
        -1000 <= nums[i] <= 1000
        -10^4 <= target <= 10^4

    Usage: python3 ./tmp.py


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
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        threeSum = []

        

        return 0 


if __name__ == "__main__":
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    expected1 = 2

    nums2 = [0, 0, 0]
    target2 = 1
    expected2 = 0

    sol = Solution()
    result1 = sol.threeSumClosest(nums1, target1)
    result2 = sol.threeSumClosest(nums2, target2)

    print(f"Example 1 result:   {result1}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {result2}")
    print(f"Example 2 expected: {expected2}")




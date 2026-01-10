#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS + ChatGPT
    Date:   January 1st, 2026

    LeetCode: #4 Median Of Two Sorted Arrays

    Given two sorted arrays nums1 and nums2 of size m and n respectively, 
    return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Example 1:
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.

    Example 2:
        Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    

    Constraints:
        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -106 <= nums1[i], nums2[i] <= 106
    
    Usage:
        python3 main.py

    Solution:

    Notes:
        TYPE HINTING REFERENCE: list vs. List
        ---------------------------------------------------------------------------
        Feature          | list (lowercase)          | List (Capitalized)
        ---------------------------------------------------------------------------
        Source           | Built-in (no import)      | from typing import List
        Primary Purpose  | Creating actual objects   | Documenting/Hinting types
        Python 3.9+      | Supports type hinting     | Still used for compatibility
        Runtime Impact   | Defines how code runs     | Completely ignored by Python
        Example          | x = list()                | x: List[int] = [1, 2, 3]
        ---------------------------------------------------------------------------
        NOTE: In modern Python (3.9+), you can just use `list[int]` instead of 
        importing `List`. LeetCode uses the capital `List` to ensure the code 
        works on older versions of Python.


        TIME COMPLEXITY: Python List (Standard Array)
        ----------------------------------------------
        Operation               | Complexity | Reason
        ----------------------------------------------
        Access by Index         | O(1)       | Constant time; direct memory jump.
        Append to End           | O(1)*      | Fast (amortized).
        Insert/Delete at Start  | O(n)       | Slow; must shift every other item.
        Search (`item in list`) | O(n)       | Slow; must check every item.
        Slicing (`l[a:b]`)      | O(k)       | Where k is the slice length.
        ----------------------------------------------


        TIME AND SPACE COMPLEXITY: 
        
*********************************************************
"""
from typing import List
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # [* * | * *]
        # Always binary search the smaller array
        # nums1 smaller, nums2 bigger
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Handles an empty array
        if len(num1) == 0:
            return 0
        
        m, n = len(nums1), len(nums2)
        total = m + n

        # Number of elements that should be on the left side when we split the two arrays around the median
        # -inf [LEFT (x items) | RIGHT (y items)] +inf
        # If total is odd → left side has one extra
        # If total is even → left and right are equal
        half = (total + 1) // 2     # left side size

        lo, hi = 0, m # cut1 ranges from 0..m
        
        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = half - cut1

            left1 = nums1[cut1-1] if cut1 > 0 else float('-inf')
            right1 = nums1[cut1] if cut1 < m else float('inf')

            left2 = nums2[cut2-1] if cut2 > 0 else float('-inf')
            right2 = nums2[cut2] if cut2 < n else float('inf')

            # Check if partition is valid
            if max(left1, left2) <= min(right1, right2):
                # Computes median from boundary values (depends on odd/even total)
                if total%2 != 0:
                    # the median is the max value on the left side of the partition
                    return max(left1, left2)
                else:
                    x = (right1 + left2)/2
                    if math.isfinite(x):
                        return  x
                    else:
                        return (left1 + right2)/2
            
            # Move binary search window
            if left1 > right2:
                hi = cut1 - 1   # cut1 too far right, increment it to the left
            else:
                lo = cut1 + 1   # cut1 too far left, increment it to the right
            
        raise ValueError("Inputs not sorted or unexpected case")

        

if __name__ == "__main__":
    # nums1 = [2,2,4,4]
    # nums2 = [2,2,2,4,4]
    # nums1 = [0]
    # nums2 = [1,2,3,4,5,6]
    # nums1 = [3, 4]
    # nums2 = [1, 2, 5]
    # nums1 = [6,7, 8]
    # nums2 = [0,1,2,3]
    # nums1 = [0,1,2]
    # nums2 = [6,7,8,9]
    # nums1 = [1, 2, 3, 4]
    # nums2 = [6, 7, 8, 9]
    # nums1 = [1, 3]
    # nums2 = [2]
    # nums1 = [1,2]
    # nums2 = [3,4]
    #nums1 = [1,3]
    #nums2 = [2,7]
    nums1 = []
    nums2 = [2,3]

    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)

    print("result:", result)

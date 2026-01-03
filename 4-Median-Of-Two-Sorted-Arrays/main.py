#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
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
        myList = sorted(nums1 + nums2)
        L = len(myList)

        # Odd number of items
        if L%2 != 0:
            median = myList[math.floor(L/2)]
        # Even number of items
        elif L%2 == 0:
            median = (myList[math.floor(L/2)] + myList[math.ceil(L/2) - 1]) / 2
        # Single item
        elif L == 1:
            median = myList[0]
        else:
            print("uncaught possibility")

        # for n in myList:
        #     print(n)

        return median
        

if __name__ == "__main__":
    nums1 = [2,2,4,4]
    nums2 = [2,2,2,4,4]

    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)

    print("result:", result)

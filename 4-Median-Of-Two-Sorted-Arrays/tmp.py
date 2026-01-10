#!/usr/bin/env python3
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n

        # Number of elements that should be on the left side when we split the two arrays around the median
        # LEFT (x items) | RIGHT (y items)
        # If total is odd → left side has one extra
        # If total is even → left and right are equal
        half = (total + 1) // 2  # left side size

        lo, hi = 0, m  # cut1 ranges from 0..m

        while lo <= hi:
            cut1 = (lo + hi) // 2
            cut2 = half - cut1

            left1  = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            right1 = nums1[cut1]     if cut1 < m else float("inf")

            left2  = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
            right2 = nums2[cut2]     if cut2 < n else float("inf")

            # Check if partition is valid
            if max(left1, left2) <= min(right1, right2):
                # TODO: compute median from boundary values (depends on odd/even total)
                #pass
                return 0.0

            # Move binary search window
            if left1 > right2:
                hi = cut1 - 1  # cut1 too far right
            else:
                lo = cut1 + 1  # cut1 too far left

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
    nums1 = [0,1,2]
    nums2 = [6,7,8,9]



    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)

    print("result:", result)
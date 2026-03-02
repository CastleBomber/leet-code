#!/usr/bin/env python3
''' 
    LeetCode (Best)
    niits's Optimal Solution

    TIME AND SPACE COMPLEXITY: 
'''
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Since one of the arrays can be significantly longer than
        # the other, we always perform binary search on the shorter
        # array to ensure that the time complexity remains
        # O(log(min(m, n))).
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len1

        while left <= right:
            part1 = (left + right) // 2
            part2 = (len1 + len2 + 1) // 2 - part1

            max_left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            min_right1 = float('inf') if part1 == len1 else nums1[part1]
            max_left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            min_right2 = float('inf') if part2 == len2 else nums2[part2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (len1 + len2) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = part1 - 1
            else:
                left = part1 + 1

if __name__ == "__main__":
    # nums1 = [2,2,4,4]
    # nums2 = [2,2,2,4,4]
    # nums1 = [0]
    # nums2 = [1,2,3,4,5,6]
    # nums1 = [3, 4]
    # nums2 = [1, 2, 5]
    nums1 = [6,7,8]
    nums2 = [0,1,2,3]
    # nums1 = [0,1,2]
    # nums2 = [6,7,8,9]
    # nums1 = [1, 2, 3, 4]
    # nums2 = [6, 7, 8, 9]
    # nums1 = [1, 3]
    # nums2 = [2]
    # nums1 = [1,2]
    # nums2 = [3,4]
    # nums1 = [1,3]
    # nums2 = [2,7]
    # nums1 = []
    # nums2 = [2,3]
    # nums1 = []
    # nums2 = [1]
    # nums1 = [1,2]
    # nums2 = [-1,3]

    sol = Solution()
    result = sol.findMedianSortedArrays(nums1, nums2)

    print("result:", result)
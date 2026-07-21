#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   July 17th, 2026

LeetCode: #16 3Sum Closest
URL: https://leetcode.com/problems/3sum-closest/

Given an integer array nums and an integer target, choose three
distinct elements whose sum is closest to target. Return that sum.

Examples:
    nums = [-1, 2, 1, -4], target = 1  -> 2
    nums = [0, 0, 0], target = 1       -> 0

Constraints:
    3 <= len(nums) <= 500
    -1000 <= nums[i] <= 1000
    -10^4 <= target <= 10^4

------------------------------------------------------
Time & Space Complexity: Sorting + Two Pointers
------------------------------------------------------
Let:               n = len(nums)

Time Complexity:   O(n^2)  | Check pairs for each fixed value
Space Complexity:  O(n)    | Store a sorted copy of the input
------------------------------------------------------

********************************************************
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Find the sum of three values that is closest to the target

        @param nums: List of integers containing at least three values
        @param target: Value the three-number sum should approach
        @result: The three-number sum closest to target
        """
        nums = sorted(nums)

        # Start with a valid triplet so every later comparison is meaningful
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            # Equal fixed values produce the same two-pointer search
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                # An exact match is the closest result possible
                if current_sum == target:
                    return target

                if current_sum < target:
                    left += 1       # Increase the sum
                else:
                    right -= 1      # Decrease the sum

        return closest_sum


if __name__ == "__main__":
    sol = Solution()

    # Test 1: standard example
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # 2

    # Test 2: all zeros
    # print(sol.threeSumClosest([0, 0, 0], 1))      # 0

    # Test 3: exact match
    # print(sol.threeSumClosest([-2, 0, 1, 2], 0))  # 0

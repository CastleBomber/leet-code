#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   July 29th, 2026

LeetCode: #18 4Sum
URL: https://leetcode.com/problems/4sum/

Given an integer array nums and an integer target, return every
unique quadruplet whose four values add up to target.
Each quadruplet must use four distinct indices.
Return the quadruplets in any order.

Examples:
    nums = [1, 0, -1, 0, -2, 2], target = 0
    -> [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    nums = [2, 2, 2, 2, 2], target = 8
    -> [[2, 2, 2, 2]]

Constraints:
    1 <= len(nums) <= 200
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9

------------------------------------------------------
Time & Space Complexity: Sorting + Two Pointers
------------------------------------------------------
Let:               n = len(nums), q = number of results

Time Complexity:   O(n^3)    | Fix two values and scan the rest
Space Complexity:  O(n + q)  | Store sorted input and results
------------------------------------------------------

********************************************************
"""

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Find every unique quadruplet whose values add up to target

        @param nums: List of integers to search
        @param target: Required sum of each quadruplet
        @result: List of all unique target-sum quadruplets
        """
        nums = sorted(nums)
        result = []
        n = len(nums)

        for i in range(n - 3):
            # Skip duplicate values for the first fixed position
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            minimum_sum = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if minimum_sum > target:
                break

            maximum_sum = nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1]
            if maximum_sum < target:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate values for the second fixed position
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                minimum_sum = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if minimum_sum > target:
                    break

                maximum_sum = nums[i] + nums[j] + nums[n - 2] + nums[n - 1]
                if maximum_sum < target:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        # Skip duplicate values after recording a match
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif current_sum < target:
                        left += 1       # Increase the sum
                    else:
                        right -= 1      # Decrease the sum

        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: standard example with three unique results
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
    # [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # Test 2: repeated values produce one unique result
    # print(sol.fourSum([2, 2, 2, 2, 2], 8))  # [[2, 2, 2, 2]]

    # Test 3: no quadruplet reaches the target
    # print(sol.fourSum([0, 0, 0, 0], 1))      # []

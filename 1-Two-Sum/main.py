#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   November 25th, 2025

    LeetCode: #1 Two Sum

    Given an array of integers 'nums' and an integer 'target',
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

    Solution:
        Accepted
        Case 1-3

    Notes:
     

*********************************************************
"""

import math
from typing import List


class Solution:
    """
    Returns indices of the two numbers such that they add up to target

    Ex:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: List[int] = []

        for i in range(len(nums)):
            x = nums.pop(i)
            x_ndx = i
            leftover = target - x
            for j in range(len(nums)):
                y = nums[j]
                y_ndx = j + 1 # account for shift after popping x
                if y == leftover:
                    result.append(x_ndx)
                    result.append(y_ndx)
                    return result
            nums.insert(i, x) # put back in its original position
                
        return result

if __name__ == "__main__":
    # Sample input from problem
    nums = [3,2,4]
    target = 6

    # Create solution instance and call the function
    sol = Solution()
    result = sol.twoSum(nums, target)

    print(result) # [2,1]


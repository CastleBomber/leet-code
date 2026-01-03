#!/usr/bin/env python3
'''
    LeetCode's Optimal Solution

    Time complexity
    Iterating once over nums → O(n)
    Lookup in hashmap → O(1) average per lookup

    We use extra space (hashmap) to reduce the number of operations 
    from O(n²) (naive double loop solution) to O(n), 
    i.e., we trade space to save time.
'''

import math
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # Python dictionary
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[nums[i]] = i # key/value
        # Return an empty list if no solution is found
        return []
    

if __name__ == "__main__":
    # Sample input from problem
    nums = [3,2,4]
    target = 6

    # Create solution instance and call the function
    sol = Solution()
    result = sol.twoSum(nums, target)

    print(result) # [2,1]


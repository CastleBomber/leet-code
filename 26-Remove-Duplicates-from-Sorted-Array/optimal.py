#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   October 13th, 2026

LeetCode: #26 Remove Duplicates from Sorted Array
URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given nums sorted in non-decreasing order, remove duplicates
in place so each unique value appears once in the first k slots.
Keep the unique values in sorted order and return k.
Values after the first k slots do not matter.

Examples:
    nums = [1, 1, 2]
    -> k = 2, nums[:k] = [1, 2]

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    -> k = 5, nums[:k] = [0, 1, 2, 3, 4]

Constraints:
    1 <= len(nums) <= 3 * 10^4
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.

------------------------------------------------------
Time & Space Complexity: Read/Write Two Pointers
------------------------------------------------------
Let:               n = len(nums)

Time Complexity:   O(n)  | Read each value once
Space Complexity:  O(1)  | Write unique values into the existing list

Auxiliary space excludes slices used only to display local test results
------------------------------------------------------

********************************************************
"""

from typing import List


class Solution:
    def __repr__(self) -> str:
        """Avoid Python's noisy default debugger representation"""
        return "Solution"

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Compact sorted unique values into the beginning of nums

        @param nums: Sorted list of integers, modified in place
        @result: Number of unique values stored in the first k slots
        """
        if not nums:
            return 0

        # The first value is already unique; write marks the next free slot
        write = 1

        for read in range(1, len(nums)):
            # Sorted order makes comparison with the last kept value sufficient
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1

        # write is also the unique count; the remaining slots can be ignored
        return write


if __name__ == "__main__":
    sol = Solution()

    # Test 1: one duplicate followed by a new value
    # nums = [1, 1, 2]
    # k = sol.removeDuplicates(nums)
    # print(f"k = {k}, nums[:k] = {nums[:k]}")  # k = 2, nums[:k] = [1, 2]

    # Test 2: several duplicate runs
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = sol.removeDuplicates(nums)
    print(f"k = {k}, nums[:k] = {nums[:k]}")  # k = 5, nums[:k] = [0, 1, 2, 3, 4]

    # Test 3: all values match, so only the first is kept
    # nums = [7, 7, 7]
    # k = sol.removeDuplicates(nums)
    # print(f"k = {k}, nums[:k] = {nums[:k]}")  # k = 1, nums[:k] = [7]

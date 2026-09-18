#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   September 4th, 2026

    LeetCode: #23 Merge k Sorted Lists
    URL: https://leetcode.com/problems/merge-k-sorted-lists/

    You are given an array of k linked-lists lists, 
    each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and 
    return it.

    Example 1:
        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
            [
                1->4->5,
                1->3->4,
                2->6
            ]
            Merging them into one sorted linked list:
            1->1->2->3->4->4->5->6

    Example 2:
        Input: lists = []
        Output: []

    Example 3:
        Input: lists = [[]]
        Output: []

    Constraints:
        k == lists.length
        0 <= k <= 10^4
        0 <= lists[i].length <= 500
        -10^4 <= lists[i][j] <= 10^4
        lists[i] is sorted in ascending order.
        The sum of lists[i].length will not exceed 10^4.

    Solution:
        Accepted - 134 / 134 testcases passed


    Usage: python3 ./main.py


*********************************************************
"""

from typing import Optional, List, Dict, Tuple, Set, Deque, DefaultDict, Any
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heappush, heappop, heapify, heappushpop, heapreplace
from itertools import combinations, permutations, product, accumulate
from functools import lru_cache, cache, reduce, cmp_to_key
from bisect import bisect_left, bisect_right, insort
from math import gcd, lcm, ceil, floor, sqrt, inf, comb, factorial
from string import ascii_lowercase, ascii_uppercase, digits
import math
import heapq
import bisect
import itertools
import functools
import operator
import copy
import re
import sys
import os


# Singly-linked list definition provided by LeetCode.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        """
        Create one linked list node

        @param val: Value stored in the node
        @param next: Following node or None
        @result: Initialized ListNode object
        """
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        """Show a compact value in the debugger."""
        return f"ListNode({self.val})"


class Solution:
    def __repr__(self) -> str:
        """Avoid Python's noisy default debugger representation."""
        return "Solution"
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()

        # Handle empty lists
        if len(lists) == 0:
            return None

        # Handle one list
        if len(lists) == 1:
            return lists[0]

        list1 = lists[0]

        for i in range(1, len(lists)):
            list2 = lists[i]
            tail = dummy

            while list1 and list2:
                
                if list1.val <= list2.val:  # The first is smaller
                    tail.next = list1       # Add to our creation  (fix!!! making a loop)
                    list1 = list1.next      # Move start of list
                else:                       # The second is smaller
                    tail.next = list2
                    list2 = list2.next

                tail = tail.next

            # The remaining list is already sorted
            tail.next = list1 if list1 else list2
            list1 = dummy.next

        return dummy.next


# Build a linked list from LeetCode's example values for local testing.
def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


# Convert a linked list to a Python list for readable output.
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    values = []
    current = head

    while current:
        values.append(current.val)  # WARNING: REQUIRES SPECIFIC RETURN OUTPUTS
        current = current.next

    return values


if __name__ == "__main__":
    lists1 = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]
    expected1 = [1, 1, 2, 3, 4, 4, 5, 6]

    lists2 = []
    expected2 = []

    lists3 = [build_linked_list([])]
    expected3 = []

    sol = Solution()
    result1 = sol.mergeKLists(lists1)
    result2 = sol.mergeKLists(lists2)
    result3 = sol.mergeKLists(lists3)

    print(f"Example 1 result:   {linked_list_to_list(result1)}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {linked_list_to_list(result2)}")
    print(f"Example 2 expected: {expected2}")
    print()
    print(f"Example 3 result:   {linked_list_to_list(result3)}")
    print(f"Example 3 expected: {expected3}")

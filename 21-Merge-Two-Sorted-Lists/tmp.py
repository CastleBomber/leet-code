#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   August 24th, 2026

    LeetCode: #21 Merge Two Sorted Lists
    URL: https://leetcode.com/problems/merge-two-sorted-lists/

    You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. 
    The list should be made by splicing together 
    the nodes of the first two lists.

    Return the head of the merged linked list.

    Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

    Example 2:
        Input: list1 = [], list2 = []
        Output: []

    Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]

    Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

    ------------------------------------------------------
    Time & Space Complexity: Intended Two-Pointer Merge
    ------------------------------------------------------
    Let:               m = nodes in list1, n = nodes in list2

    Algorithm:         Compare both current nodes, splice the smaller
                       node into the result, and advance that pointer

    Time Complexity:   O(m + n)  | Visit each node once
    Space Complexity:  O(1)      | Reuse nodes with fixed pointers
    ------------------------------------------------------

    Usage: python3 ./tmp.py


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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        dummy = ListNode(0, list1)
        current = dummy
        cur1 = list1
        cur2 = list2
        x, y = 0

        # If list is empty, return the other
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        while cur1.next:
            if cur1.value >= cur2.value:
                current.next = cur1
            else:
                current.next = cur2










        while x < linked_list_size(list1) and y < linked_list_size(list2):
            # End of the list checks
            if list1[x] == null:
                add list2[y]
                y++
            if list2[y] == null:
                add list1[x]
                x++
            if list1[x] >= list2[y]:
                add list1[x]
                x++
            else:
                add list2[y]
                y++


            

        return result

def linked_list_size(head):
    size = 0
    current = head

    while current:
        size += 1
        current = current.next

    return size

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
        values.append(current.val)
        current = current.next

    return values


if __name__ == "__main__":
    list1_example1 = build_linked_list([1, 2, 4])
    list2_example1 = build_linked_list([1, 3, 4])
    expected1 = [1, 1, 2, 3, 4, 4]

    list1_example2 = build_linked_list([])
    list2_example2 = build_linked_list([])
    expected2 = []

    list1_example3 = build_linked_list([])
    list2_example3 = build_linked_list([0])
    expected3 = [0]

    sol = Solution()
    result1 = sol.mergeTwoLists(list1_example1, list2_example1)
    result2 = sol.mergeTwoLists(list1_example2, list2_example2)
    result3 = sol.mergeTwoLists(list1_example3, list2_example3)

    print(f"Example 1 result:   {linked_list_to_list(result1)}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {linked_list_to_list(result2)}")
    print(f"Example 2 expected: {expected2}")
    print()
    print(f"Example 3 result:   {linked_list_to_list(result3)}")
    print(f"Example 3 expected: {expected3}")

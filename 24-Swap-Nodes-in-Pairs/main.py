#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   September 11th, 2026

    LeetCode: #24 Swap Nodes in Pairs
    URL: https://leetcode.com/problems/swap-nodes-in-pairs/

    Given a linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's
    nodes (i.e., only nodes themselves may be changed).

    Example 1:
        Input: head = [1,2,3,4]
        Output: [2,1,4,3]

    Example 2:
        Input: head = []
        Output: []

    Example 3:
        Input: head = [1]
        Output: [1]

    Example 4:
        Input: head = [1,2,3]
        Output: [2,1,3]

    Constraints:
        The number of nodes in the list is in the range [0, 100].
        0 <= Node.val <= 100

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
        Create one linked list node.

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

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while head:
            tail.next = head.next
            tail = tail.next
            head = tail.next


        

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
        values.append(current.val)
        current = current.next

    return values


if __name__ == "__main__":
    head1 = build_linked_list([1, 2, 3, 4])
    expected1 = [2, 1, 4, 3]

    head2 = build_linked_list([])
    expected2 = []

    head3 = build_linked_list([1])
    expected3 = [1]

    head4 = build_linked_list([1, 2, 3])
    expected4 = [2, 1, 3]

    sol = Solution()
    result1 = sol.swapPairs(head1)
    result2 = sol.swapPairs(head2)
    result3 = sol.swapPairs(head3)
    result4 = sol.swapPairs(head4)

    print(f"Example 1 result:   {linked_list_to_list(result1)}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {linked_list_to_list(result2)}")
    print(f"Example 2 expected: {expected2}")
    print()
    print(f"Example 3 result:   {linked_list_to_list(result3)}")
    print(f"Example 3 expected: {expected3}")
    print()
    print(f"Example 4 result:   {linked_list_to_list(result4)}")
    print(f"Example 4 expected: {expected4}")

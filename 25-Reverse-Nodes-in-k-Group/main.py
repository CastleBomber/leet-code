#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   September 11th, 2026

    LeetCode: #25 Reverse Nodes in k-Group
    URL: https://leetcode.com/problems/reverse-nodes-in-k-group/

    Given the head of a linked list, 
    reverse the nodes of the list k at a time, 
    and return the modified list.

    k is a positive integer and is less than or equal to the length of the
    linked list. 
    If the number of nodes is not a multiple of k then left-out nodes, 
    in the end, should remain as they are.

    You may not alter the values in the list's nodes, only nodes themselves
    may be changed.

    Example 1:
        Input: head = [1,2,3,4,5], k = 2
        Output: [2,1,4,3,5]

    Example 2:
        Input: head = [1,2,3,4,5], k = 3
        Output: [3,2,1,4,5]

    Constraints:
        The number of nodes in the list is n.
        1 <= k <= n <= 5000
        0 <= Node.val <= 1000

    Follow-up: Can you solve the problem in O(1) extra memory space?

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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:






        

        return 0


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
    head1 = build_linked_list([1, 2, 3, 4, 5])
    k1 = 2
    expected1 = [2, 1, 4, 3, 5]

    head2 = build_linked_list([1, 2, 3, 4, 5])
    k2 = 3
    expected2 = [3, 2, 1, 4, 5]

    sol = Solution()
    result1 = sol.reverseKGroup(head1, k1)
    result2 = sol.reverseKGroup(head2, k2)

    print(f"Example 1 result:   {linked_list_to_list(result1)}")
    print(f"Example 1 expected: {expected1}")
    print()
    print(f"Example 2 result:   {linked_list_to_list(result2)}")
    print(f"Example 2 expected: {expected2}")

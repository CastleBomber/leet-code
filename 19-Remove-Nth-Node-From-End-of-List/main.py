#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   July 18th, 2026

    LeetCode: #19 Remove Nth Node From End of List
    URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

    Given the head of a linked list, 
    remove the nth node from the end of the list and return its head.

    Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

    Example 2:
        Input: head = [1], n = 1
        Output: []

    Example 3:
        Input: head = [1,2], n = 1
        Output: [1]

    Constraints:
        The number of nodes in the list is sz.
        1 <= sz <= 30
        0 <= Node.val <= 100
        1 <= n <= sz

    Usage: python3 ./main.py

    Solution:
        Accepted - 208 / 208 testcases passed

    ------------------------------------------------------
    Time & Space Complexity: Two-Pass Linked List Scan
    ------------------------------------------------------
    Let:               L = number of nodes in the list

    First Pass:        O(L)  | Count all nodes
    Second Pass:       O(L)  | Move to the node before removal

    Time Complexity:   O(L)  | Two linear passes remain O(L)
    Space Complexity:  O(1)  | Use only pointers and counters
    ------------------------------------------------------




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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = linked_list_size(head) 
        jumps = size - n

        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        counter = 0

        while current.next: # Does not move, just checks that it exists
            if counter == jumps:
                current.next = current.next.next
                break

            counter += 1
            current = current.next

        return dummy.next

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
    head1 = build_linked_list([1, 2, 3, 4, 5])
    n1 = 2
    expected1 = [1, 2, 3, 5]

    head2 = build_linked_list([1])
    n2 = 1
    expected2 = []

    head3 = build_linked_list([1, 2])
    n3 = 1
    expected3 = [1]

    sol = Solution()
    result1 = sol.removeNthFromEnd(head1, n1)
    # result2 = sol.removeNthFromEnd(head2, n2)
    # result3 = sol.removeNthFromEnd(head3, n3)

    print(f"Example 1 result:   {linked_list_to_list(result1)}")
    print(f"Example 1 expected: {expected1}")
    print()
    # print(f"Example 2 result:   {linked_list_to_list(result2)}")
    # print(f"Example 2 expected: {expected2}")
    # print()
    # print(f"Example 3 result:   {linked_list_to_list(result3)}")
    # print(f"Example 3 expected: {expected3}")

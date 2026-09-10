#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   September 9th, 2026

LeetCode: #23 Merge k Sorted Lists
URL: https://leetcode.com/problems/merge-k-sorted-lists/

Given an array of k linked lists where each list is sorted in
ascending order, merge every list into one sorted linked list.
Return the head of the merged list.

Examples:
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    -> [1, 1, 2, 3, 4, 4, 5, 6]

    lists = []
    -> []

    lists = [[]]
    -> []

Constraints:
    0 <= k <= 10^4
    0 <= nodes in each list <= 500
    -10^4 <= Node.val <= 10^4
    Total nodes across all lists will not exceed 10^4.

------------------------------------------------------
Time & Space Complexity: Min-Heap
------------------------------------------------------
Let: N = total nodes, k = number of lists

Time Complexity: O(N log k) | Push and pop each node once
Space Complexity: O(k) | Store at most one node per list

------------------------------------------------------

********************************************************
"""

from heapq import heappop, heappush
from typing import List, Optional


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


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        return 0


def build_linked_list(values: List[int]) -> Optional[ListNode]:
    """
    Build a linked list from Python list values

    @param values: Values to place into linked list nodes
    @result: Head of the new linked list
    """
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """
    Convert a linked list into a Python list

    @param head: First node in the linked list
    @result: Values from the linked list in order
    """
    values = []
    current = head

    while current:
        values.append(current.val)
        current = current.next

    return values


if __name__ == "__main__":
    sol = Solution()

    # Test 1: standard example with three lists
    lists = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6]),
    ]
    merged = sol.mergeKLists(lists)
    print(linked_list_to_list(merged))  # [1, 1, 2, 3, 4, 4, 5, 6]

    # Test 2: no lists
    # print(linked_list_to_list(sol.mergeKLists([])))  # []

    # Test 3: one empty list
    # print(linked_list_to_list(sol.mergeKLists([None])))  # []

    # Test 4: empty lists with negatives and duplicates
    # lists = [
    #     build_linked_list([-3, -1, 4]),
    #     None,
    #     build_linked_list([-2, -1, 3]),
    #     build_linked_list([0, 0, 5]),
    # ]
    # merged = sol.mergeKLists(lists)
    # print(linked_list_to_list(merged))
    # [-3, -2, -1, -1, 0, 0, 3, 4, 5]

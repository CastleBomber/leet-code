#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   August 29th, 2026

LeetCode: #21 Merge Two Sorted Lists
URL: https://leetcode.com/problems/merge-two-sorted-lists/

Given the heads of two sorted linked lists, merge their nodes into
one sorted linked list and return the head of the merged list.

Examples:
    list1 = [1, 2, 4], list2 = [1, 3, 4]
    -> [1, 1, 2, 3, 4, 4]

    list1 = [], list2 = []
    -> []

    list1 = [], list2 = [0]
    -> [0]

Constraints:
    0 <= total number of nodes <= 50
    -100 <= Node.val <= 100
    Both lists are sorted in non-decreasing order.

------------------------------------------------------
Time & Space Complexity: Iterative Two Pointers
------------------------------------------------------
Let:               m = nodes in list1, n = nodes in list2

Time Complexity:   O(m + n)  | Visit each node once
Space Complexity:  O(1)      | Reuse nodes with fixed pointers
------------------------------------------------------

********************************************************
"""

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
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:
        """
        Merge two sorted linked lists by reusing their nodes

        @param list1: Head of the first sorted linked list
        @param list2: Head of the second sorted linked list
        @result: Head of the merged sorted linked list
        """
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        # The remaining list is already sorted
        tail.next = list1 if list1 else list2

        return dummy.next


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

    # Test 1: standard example with duplicates
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])
    merged = sol.mergeTwoLists(list1, list2)
    print(linked_list_to_list(merged))  # [1, 1, 2, 3, 4, 4]

    # Test 2: both lists are empty
    # merged = sol.mergeTwoLists(None, None)
    # print(linked_list_to_list(merged))  # []

    # Test 3: one list is empty
    # list2 = build_linked_list([0])
    # merged = sol.mergeTwoLists(None, list2)
    # print(linked_list_to_list(merged))  # [0]

    # Test 4: first list contains the remaining nodes
    # list1 = build_linked_list([1, 3, 5, 7])
    # list2 = build_linked_list([2, 4])
    # merged = sol.mergeTwoLists(list1, list2)
    # print(linked_list_to_list(merged))  # [1, 2, 3, 4, 5, 7]

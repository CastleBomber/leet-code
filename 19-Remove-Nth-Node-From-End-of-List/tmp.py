#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   August 24th, 2026

LeetCode: #19 Remove Nth Node From End of List
URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end
of the list and return the updated head.

Examples:
    head = [1, 2, 3, 4, 5], n = 2  -> [1, 2, 3, 5]
    head = [1], n = 1              -> []
    head = [1, 2], n = 1           -> [1]

Constraints:
    1 <= number of nodes <= 30
    0 <= Node.val <= 100
    1 <= n <= number of nodes

------------------------------------------------------

------------------------------------------------------

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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end using two pointers

        @param head: First node in the linked list
        @param n: Position from the end of the list
        @result: Head of the updated linked list
       """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Create a gap of n nodes between the pointers
        for _ in range(n):
            fast = fast.next

        # Move together until slow is directly before the target
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

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

    # Test 1: remove a middle node
    head = build_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.removeNthFromEnd(head, 2))) # [1, 2, 3, 5]
    

    # Test 2: remove the only node
    # head = build_linked_list([1])
    # print(linked_list_to_list(sol.removeNthFromEnd(head, 1)))  # []

    # Test 3: remove the final node
    # head = build_linked_list([1, 2])
    # print(linked_list_to_list(sol.removeNthFromEnd(head, 1)))  # [1]

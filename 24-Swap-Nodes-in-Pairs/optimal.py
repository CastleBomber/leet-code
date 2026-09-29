#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   September 28th, 2026

LeetCode: #24 Swap Nodes in Pairs
URL: https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and
return its head. Change the links, not the node values.
An unpaired final node stays in place.

Examples:
    head = [1, 2, 3, 4]  -> [2, 1, 4, 3]
    head = []           -> []
    head = [1]          -> [1]
    head = [1, 2, 3]     -> [2, 1, 3]

Constraints:
    0 <= number of nodes <= 100
    0 <= Node.val <= 100

------------------------------------------------------
Time & Space Complexity: Iterative Pair Swapping
------------------------------------------------------
Let:               n = number of nodes

Time Complexity:   O(n)  | Visit each pair once and rewire its links
Space Complexity:  O(1)  | Reuse nodes with a dummy node and fixed pointers

Auxiliary space excludes the local test helpers
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

    def __repr__(self) -> str:
        """Show a compact value in the debugger"""
        return f"ListNode({self.val})"


class Solution:
    def __repr__(self) -> str:
        """Avoid Python's noisy default debugger representation"""
        return "Solution"

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap adjacent nodes by changing their links

        @param head: First node in the linked list
        @result: Head of the list with each complete pair swapped
        """
        # The dummy makes swapping the first pair work like every later pair
        dummy = ListNode(next=head)
        previous = dummy

        # Stop when fewer than two nodes remain
        while previous.next and previous.next.next:
            first = previous.next
            second = first.next

            # Before: previous -> first -> second -> rest
            # After:  previous -> second -> first -> rest
            first.next = second.next
            second.next = first
            previous.next = second

            # The original first node is now the end of the swapped pair
            previous = first

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

    # Test 1: standard example with two complete pairs
    # head = build_linked_list([1, 2, 3, 4])
    # print(linked_list_to_list(sol.swapPairs(head)))  # [2, 1, 4, 3]

    # Test 2: empty list
    # print(linked_list_to_list(sol.swapPairs(None)))  # []

    # Test 3: swap multiple pairs and leave the unpaired final node
    head = build_linked_list([1, 2, 3, 4, 5])
    print(linked_list_to_list(sol.swapPairs(head)))  # [2, 1, 4, 3, 5]

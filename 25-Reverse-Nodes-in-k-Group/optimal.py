#!/usr/bin/env python3
"""
********************************************************
Author: ChatGPT + CBOMBS
Date:   October 5th, 2026

LeetCode: #25 Reverse Nodes in k-Group
URL: https://leetcode.com/problems/reverse-nodes-in-k-group/

Reverse the linked list's nodes in groups of k and return
the modified head. Keep any incomplete final group unchanged.
Change the links, not the values stored in the nodes.

Examples:
    head = [1, 2, 3, 4, 5], k = 2  -> [2, 1, 4, 3, 5]
    head = [1, 2, 3, 4, 5], k = 3  -> [3, 2, 1, 4, 5]

Constraints:
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000

------------------------------------------------------
Time & Space Complexity: Iterative In-Place Group Reversal
------------------------------------------------------
Let:               n = number of nodes, k = group size

Time Complexity:   O(n)  | Check each group, then reverse its links
Space Complexity:  O(1)  | Reuse nodes with a dummy node and fixed pointers

Each node is visited at most twice
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

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse complete groups of k nodes by changing their links

        @param head: First node in the linked list
        @param k: Number of nodes per group, with k >= 1
        @result: Modified head, with any incomplete final group unchanged
        """
        if head is None or k == 1:
            return head

        dummy = ListNode(next=head)
        group_previous = dummy

        while True:
            # Find the kth node BEFORE changing any links
            group_end = group_previous
            for _ in range(k):
                group_end = group_end.next
                if group_end is None:
                    return dummy.next

            group_next = group_end.next
            group_first = group_previous.next

            # The original first node becomes the tail, linked to the next group
            previous = group_next
            current = group_first

            while current is not group_next:
                next_node = current.next  # Save the forward link before reversing it
                current.next = previous
                previous = current
                current = next_node

            # Connect the reversed group and advance to its new tail
            group_previous.next = group_end
            group_previous = group_first


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

    # Test 1: reverse pairs and keep the final node
    # head = build_linked_list([1, 2, 3, 4, 5])
    # print(linked_list_to_list(sol.reverseKGroup(head, 2)))  # [2, 1, 4, 3, 5]

    # Test 2: preserve an incomplete final group of two nodes
    # head = build_linked_list([1, 2, 3, 4, 5])
    # print(linked_list_to_list(sol.reverseKGroup(head, 3)))  # [3, 2, 1, 4, 5]

    # Test 3: reverse two complete groups with no leftover nodes
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    print(linked_list_to_list(sol.reverseKGroup(head, 3)))  # [3, 2, 1, 6, 5, 4]

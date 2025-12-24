#!/usr/bin/env python3
''' 
    LeetCode
    Rahul Varma's Optimal Solution

    Time complexity
'''

import math
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
    
if __name__ == "__main__":
    # Sample inputs from problem
    # Build l1 = 342, so the reverse nodes are: 2 -> 4 -> 3 -> None
    l1_node3 = ListNode(3)
    l1_node2 = ListNode(4, l1_node3)
    l1_head = ListNode(2, l1_node2)

    # Build l2 = 465, so the reverse nodes are: 5 -> 6 -> 4 -> None
    l2_node3 = ListNode(4)
    l2_node2 = ListNode(6, l2_node3)
    l2_head = ListNode(5, l2_node2)

    # Create solution instance and call the function
    sol = Solution()
    result = sol.addTwoNumbers(l1_head, l2_head)

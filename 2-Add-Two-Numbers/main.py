#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   December 4th, 2025

    LeetCode: #2 Add Two Numbers

    You are given two non-empty linked lists representing two non-negative integers. 
    The digits are stored in reverse order, and each of their nodes contains a single digit. 
    Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
    
    Example 2:
        Input: l1 = [0], l2 = [0]
        Output: [0]
    
    Example 3:
        Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        Output: [8,9,9,9,0,0,0,1]
    
    Usage:
        python3 main.py

    Solution:
        Accepted

    Notes:
         

*********************************************************
"""

import math
from typing import List, Optional


# Singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Provides methods for linked list arithmetic options
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented as reversed singly-linked lists

        Each linked list stores one digit per node, 
        w/ the least significant digit at the head of the list
        
        The function returns a new linked list representing the sum, also in reversed order

        Args:
            l1: Head of the first linked list
            l2: Head of the second linked list

        Returns:
            Head of the linked list representing the sum
            (starting w/ the least significant digit)
        """
        curr1 = l1
        curr2 = l2
        str1 = ""
        str2 = ""

        # Calculate the numbers represented by the reverse ordered Nodes
        while curr1:
            str1 = str(curr1.val) + str1
            curr1 = curr1.next
            
        while curr2:
            str2 = str(curr2.val) + str2
            curr2 = curr2.next

        # Sum of the node representations
        sum = str(int(str1)+int(str2))

        # Creates the first Node w/ the base being the first digit from the sum
        base_node = ListNode(int(sum[0]))
        head = base_node

        # Creates the next Nodes w/ the head being the last digit from the sum
        if len(sum) >= 2:
            for n in range(1, len(sum)):
                next_node = ListNode(int(sum[n]), head)
                head = next_node

        #self.printNodeValues(head)

        return head

    def printNodeValues(self, nodes: Optional[ListNode]):
        tmp = nodes
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next
        
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

    #sol.printNodeValues(result)

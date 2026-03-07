#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 6th, 2026
    Purpose: Prepping for IBM coding test

    LeetCode: #100 Same Tree

    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

    Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

    Constraints:
        The number of nodes in both trees is in the range [0, 100].
        -10^4 <= Node.val <= 10^4

    Usage:
        python3 main.py

    Solution:
        Recursive depth-first search (DFS) – compares nodes in a top-down manner.
        Time: O(n), where n is the number of nodes in the smaller tree.
        Space: O(h) for the recursion stack, where h is the tree height (worst-case O(n)).
        This is optimal because we must examine every node in the worst case.

    
    TIME AND SPACE COMPLEXITY: Recursive DFS
    ----------------------------------------------------
    Metric           | Complexity | Reason
    ----------------------------------------------------
    Time Complexity  | O(n)       | Each node is visited exactly once, performing
                                    constant-time comparisons (value checks + recursion).
                                    n = total number of nodes in both trees.
    Space Complexity | O(h)       | Recursion stack depth equals the tree height h.
                                    Worst-case O(n) for a skewed tree (like a linked list),
                                    best/average O(log n) for balanced trees.
    ----------------------------------------------------

*********************************************************
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None -> structurally same at this point
        if not p and not q:
            return True

        # If one is None and the other isn't, structures differ
        if not p or not q:
            return False

        # If values differ, trees are not the same
        if p.val != q.val:
            return False

        # Recursively check left and right subtrees
        # Both must be identical for the trees to be the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    # Test case 1: Same trees [1,2,3]
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))

    # Test case 2: Different structures [1,2] vs [1,null,2]
    p2 = TreeNode(1, TreeNode(2), None)
    q2 = TreeNode(1, None, TreeNode(2))

    # Test case 3: Different values [1,2,1] vs [1,1,2]
    p3 = TreeNode(1, TreeNode(2), TreeNode(1))
    q3 = TreeNode(1, TreeNode(1), TreeNode(2))

    sol = Solution()
    print(sol.isSameTree(p1, q1))  # True
    print(sol.isSameTree(p2, q2))  # False
    print(sol.isSameTree(p3, q3))  # False
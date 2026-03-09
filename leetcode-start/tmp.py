#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 6th, 2026
    Purpose: Prepping for IBM coding test

    LeetCode: #101 Symmetric Tree

    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Example 1:
        Input: root = [1,2,2,3,4,4,3]
        Output: true

    Example 2:
        Input: root = [1,2,2,null,3,null,3]
        Output: false

    Constraints:
        The number of nodes in the tree is in the range [1, 1000].
        -100 <= Node.val <= 100

    Follow up: 
        Could you solve it both recursively and iteratively?

    Usage:
        python3 main.py

    Solution:
        Both recursive and iterative approaches compare the left and right subtrees
        in a mirrored fashion. Time O(n), space O(n) worst-case.

    Notes:
        The recursive solution uses the call stack; the iterative solution uses a queue.
*********************************************************
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # -------------------- Recursive Approach --------------------
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # An empty tree or a single node is symmetric
        if not root:
            return True
        # Check if the left and right subtrees are mirrors of each other
        return self._isMirror(root.left, root.right)

    def _isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        # Both nodes are None: symmetric at this level
        if not left and not right:
            return True
        # One is None and the other isn't: not symmetric
        if not left or not right:
            return False
        # Values must be equal, and then check mirrored children:
        # left's left vs right's right, and left's right vs right's left
        return (left.val == right.val and
                self._isMirror(left.left, right.right) and
                self._isMirror(left.right, right.left))

    # -------------------- Iterative Approach --------------------
    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        # Use a queue to hold pairs of nodes to compare
        queue = deque()
        # Start with the left and right children of the root
        queue.append((root.left, root.right))

        while queue:
            left, right = queue.popleft()

            # If both are None, continue (no further children to check)
            if not left and not right:
                continue
            # If one is None or values differ, not symmetric
            if not left or not right or left.val != right.val:
                return False

            # Enqueue the children in mirrored order:
            # left's left with right's right, and left's right with right's left
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True


if __name__ == "__main__":
    # Build symmetric tree: [1,2,2,3,4,4,3]
    root = TreeNode(1,
                    TreeNode(2, TreeNode(3), TreeNode(4)),
                    TreeNode(2, TreeNode(4), TreeNode(3)))

    sol = Solution()
    result = sol.isSymmetric(root)           # uses recursive version
    result_iter = sol.isSymmetricIterative(root)

    print(f"Recursive: {result}")    # True
    print(f"Iterative: {result_iter}")  # True
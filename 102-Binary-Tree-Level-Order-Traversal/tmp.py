#!/usr/bin/env python3
"""
********************************************************
    Author: CBOMBS
    Date:   March 6th, 2026
    Purpose: Prepping for IBM coding test

    LeetCode: #102 Binary Tree Level Order Traversal

    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).

    Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]

    Example 2:
        Input: root = [1]
        Output: [[1]]

    Example 3:
        Input: root = []
        Output: []

    Constraints:
        The number of nodes in the tree is in the range [0, 2000].
        -1000 <= Node.val <= 1000

    Usage:
        python3 optimal-solution-deepseek.py

    Solution:
        BFS using a queue. Process all nodes level by level.
        For each level, record the number of nodes in the queue (current level size)
        and pop only that many, appending their values to a level list.
        Then enqueue their children for the next level.

    Notes:
        Time: O(n), Space: O(n)
*********************************************************
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Edge case: empty tree
        if not root:
            return []

        result = []
        queue = deque([root])  # Start with the root node

        while queue:
            # Number of nodes at the current level
            level_size = len(queue)
            current_level = []

            # Process all nodes at this level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Enqueue left and right children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the completed level to the result
            result.append(current_level)

        return result


if __name__ == "__main__":
    # Example 1: [3,9,20,null,null,15,7]
    root = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20, TreeNode(15), TreeNode(7)))

    sol = Solution()
    result = sol.levelOrder(root)
    print(result)  # Output: [[3], [9, 20], [15, 7]]
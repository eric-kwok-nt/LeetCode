from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.current_max = -float("inf")
        _ = self.dfs(root)
        return self.current_max

    def dfs(self, Node: Optional[TreeNode]) -> int:
        if Node is None:
            return 0

        left_max = max(self.dfs(Node.left), 0)
        right_max = max(self.dfs(Node.right), 0)
        self.current_max = max((left_max + Node.val + right_max), self.current_max)
        return Node.val + max(left_max, right_max)  # Return maximum of a branch

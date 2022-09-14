from typing import Optional
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = Queue(maxsize=0)
        root.depth = 1
        q.put(root)
        while not q.empty():
            node = q.get()
            if node.left is None and node.right is None:
                return node.depth
            if node.left is not None:
                node.left.depth = node.depth + 1
                q.put(node.left)
            if node.right is not None:
                node.right.depth = node.depth + 1
                q.put(node.right)

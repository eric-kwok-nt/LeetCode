from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root)

    def is_valid(
        self, node: TreeNode, lower_bound=-float("inf"), upper_bound=float("inf")
    ) -> bool:
        if node.left is not None:
            if (
                node.left.val >= node.val
                or node.left.val <= lower_bound
                or node.left.val >= upper_bound
                or not self.is_valid(
                    node.left, lower_bound=lower_bound, upper_bound=node.val
                )
            ):
                return False
        if node.right is not None:
            if (
                node.right.val <= node.val
                or node.right.val <= lower_bound
                or node.right.val >= upper_bound
                or not self.is_valid(
                    node.right, lower_bound=node.val, upper_bound=upper_bound
                )
            ):
                return False
        return True

from typing import Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.num_of_good_nodes = 0
        self.check_is_good(root, max_number=-float("inf"))
        return self.num_of_good_nodes

    def check_is_good(self, node: TreeNode, max_number: Union[int, float]) -> None:
        if node.val >= max_number:
            self.num_of_good_nodes += 1
            max_number = node.val
        if node.left is not None:
            self.check_is_good(node=node.left, max_number=max_number)
        if node.right is not None:
            self.check_is_good(node=node.right, max_number=max_number)

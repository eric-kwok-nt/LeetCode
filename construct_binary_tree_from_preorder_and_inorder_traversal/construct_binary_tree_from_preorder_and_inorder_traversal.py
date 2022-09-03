from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.build_inorder_hashmap(inorder)
        self.preorder_index = 0
        self.preorder = preorder

        return self.build_sub_tree(0, len(preorder) - 1)

    def build_sub_tree(
        self, left_inorder_idx: int, right_inorder_idx: int
    ) -> Optional[TreeNode]:
        if left_inorder_idx > right_inorder_idx:
            return None
        Node = TreeNode(val=self.preorder[self.preorder_index])
        self.preorder_index += 1
        node_inorder_idx = self.inorder_idx_map[Node.val]
        Node.left = self.build_sub_tree(left_inorder_idx, node_inorder_idx - 1)
        Node.right = self.build_sub_tree(node_inorder_idx + 1, right_inorder_idx)
        return Node

    def build_inorder_hashmap(self, inorder: List[int]) -> None:
        self.inorder_idx_map = {node_val: idx for idx, node_val in enumerate(inorder)}

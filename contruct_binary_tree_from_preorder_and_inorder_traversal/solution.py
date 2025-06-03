from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.inorder = inorder
        pre_left, pre_right = 0, len(preorder) - 1
        in_left, in_right = 0, len(inorder) - 1
        self.in2idx = {val: idx for idx, val in enumerate(inorder)}
        root = self._build_tree_recursively(
            pre_left=pre_left,
            pre_right=pre_right,
            in_left=in_left,
            in_right=in_right
        )
        return root

    def _build_tree_recursively(
        self, pre_left: int, pre_right: int, in_left: int, in_right: int
    ) -> TreeNode:
        if in_left > in_right:
            return
        root = TreeNode(val=self.preorder[pre_left])
        if in_left == in_right:
            return root
        inorder_idx = self.in2idx[root.val]
        num_left_nodes = inorder_idx - in_left
        num_right_nodes = in_right - inorder_idx
        root.left = self._build_tree_recursively(
            pre_left=pre_left + 1,
            pre_right=pre_right - num_right_nodes,
            in_left=in_left,
            in_right=in_right - num_right_nodes - 1,
        )
        root.right = self._build_tree_recursively(
            pre_left=pre_left + num_left_nodes + 1,
            pre_right=pre_right,
            in_left=in_left + num_left_nodes + 1,
            in_right=in_right,
        )
        return root
    
# preorder = [3, 9, 20, 15, 7]
# inorder = [9, 3, 15, 20, 7]

preorder = [1, 2]
inorder = [2, 1]
    
def print_tree(root):
    if not root:
        print("null", end=" ")
    else:
        print(root.val, end=" ")
        print_tree(root.left)
        print_tree(root.right)

sol = Solution()
root = sol.buildTree(preorder=preorder, inorder=inorder)
print_tree(root)
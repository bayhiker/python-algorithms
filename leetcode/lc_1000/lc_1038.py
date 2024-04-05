# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.tree import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        return self.bst_to_gst(root)

    def bst_to_gst(self, root: TreeNode) -> TreeNode:
        # Traverse tree, and note val, left_sum, right_sum
        # Then use the three intermediate result to calculate gst
        # Note that all nodes in the right subtree are greater than root
        pass

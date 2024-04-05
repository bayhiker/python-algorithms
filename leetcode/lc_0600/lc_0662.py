# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from lib.tree import TreeNode
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.width_of_binary_tree(root)
        
    def width_of_binary_tree(self, root: Optional[TreeNode]) -> int:
        # DFS of tree while memorizing level and node sequence number
        # Reuse node.val to store node index in current level
        left, right = 0, 0
        max_width = 0

        pass
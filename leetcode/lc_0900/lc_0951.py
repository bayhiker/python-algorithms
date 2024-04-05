from typing import Optional
from lib.tree import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # DFS trees a and b at the same time,
        # When visiting a.left
        # if a.left == b.left, then b go left,
        # if a.left == b.right, then b go right
        # When visiting a.right
        # if a.right == b.left, then b go left,
        # if a.right == b.right, then b go right
        # Return True if the two trees finish at the same time, otherwise False
        pass

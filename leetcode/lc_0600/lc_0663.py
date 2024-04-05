""" 
Given a binary tree with n nodes, your task is to check if it's possible to
partition the tree to two trees which have the equal sum of values after
removing exactly one edge on the original tree. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lib.tree import TreeNode


class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        return self.check_equal_tree(root)

    def check_equal_tree(self, root: TreeNode) -> bool:
        # Get sum of all subtrees, check if half of sum(root) is found
        pass

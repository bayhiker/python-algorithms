# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from lib.tree import TreeNode


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Option 1: Traverse BST, and then use a dict d to check k - x exists in d: O(n) time and O(n) space
        # Option 2: Traverse BST and generate a sorted list, then use two pointers: O(n) and O(n)
        pass

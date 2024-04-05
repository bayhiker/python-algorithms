# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from lib.tree import TreeNode
from functools import reduce


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        return self.pseudo_palindromic_paths(root)

    def pseudo_palindromic_paths(self, root: Optional[TreeNode]) -> int:
        # DFS, a path is pseudo-palindromic: at most one in 1-9 has odd occurrences
        result = 0

        def dfs(node: TreeNode, freq: list[int]) -> None:
            # Search and analyze all leaf nodes
            nonlocal result
            if node.val:
                freq[node.val] += 1
            if node.left is None and node.right is None:
                total_odds = reduce(lambda x, y: x + y, [i % 2 for i in freq])
                result += 1 if total_odds <= 1 else 0
                return
            if node.left:
                dfs(node.left, freq.copy())
            if node.right:
                dfs(node.right, freq.copy())

        dfs(root, [0 for _ in range(10)])
        return result

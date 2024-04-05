"""
Given a root of N-ary tree, compute The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value. For example, tree root = [1,null,3,2,4,null,5,6] represents the following tree: 

1 --> 2
  |-> 3 --> 5
  |     |-> 6
  |-> 4

  
Solution:
1. Define Node class and convert array to N-ary tree
2. Use DFS, each recursive call returns a nodes top two longest path to its leaves,
   and diameter of that subtree. Note that a diameter doesn't have to pass through
   root of the sub-tree. For example, when a tree is very unbalanced,
   the longest path might be inside the heavier sub-tree.
"""

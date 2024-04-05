from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst2inorder():
    raise RuntimeError("Not Implemented")

def preorder2bst():
    raise RuntimeError("Not Implemented")


def array2bt(root: list[any], node_index=0) -> TreeNode:
    if len(root) <= node_index or root[node_index] is None:
        return None
    node = TreeNode(val=root[node_index])
    node.left = array2bt(root, 2 * node_index + 1)
    node.right = array2bt(root, 2 * node_index + 2)
    return node


def bt2array(root: TreeNode) -> list[any]:
    if root is None:
        return []
    q = deque()
    q.append(root)
    result = []
    while len(q) > 0:
        head: TreeNode = q.popleft()
        if head is None:
            result.append(None)
        else:
            result.append(head.val)
            q.append(head.left)
            q.append(head.right)
    while len(result) > 0 and result[-1] is None:
        result.pop()
    return result

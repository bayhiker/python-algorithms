class Solution:
    def deleteTreeNodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
        return self.delete_tree_nodes(nodes, parent, value)

    def delete_tree_nodes(self, nodes: int, parent: list[int], value: list[int]) -> int:
        # Traverse from nodes - 1 to 0, add values[i] to values[parent[i]]
        # Go from 0 -> nodes - 1, if values[parent[i]] is 0, then set values[i] to 0
        # Count non-0 items along the way
        pass

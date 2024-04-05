class Solution:
    def reachableNodes(
        self, n: int, edges: list[list[int]], restricted: list[int]
    ) -> int:
        return self.reachable_nodes(edges, restricted)

    def reachable_nodes(
        self, n: int, edges: list[list[int]], restricted: list[int]
    ) -> int:
        # Use BFS to traverse, set visited flag for blocked nodes to True
        pass

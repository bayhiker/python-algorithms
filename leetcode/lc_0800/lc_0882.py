class Solution:
    def reachableNodes(self, edges: list[list[int]], maxMoves: int, n: int) -> int:
        return self.reachable_nodes(edges, maxMoves)

    def reachable_nodes(self, edges: list[list[int]], max_moves: int, n: int) -> int:
        # Use modified weighted dijkstra's algorithm to get shortest distance
        # to all other nodes from node 0.
        pass

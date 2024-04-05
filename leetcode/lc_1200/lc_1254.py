class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        return self.closed_island(grid)

    def closed_island(self, grid: list[list[int]]) -> int:
        # Look for the first 0, then do a DFS search, change all 0s reachable to 2.
        # If no cell borders edge, result+=1.
        # Keep doing this until no 0s present in he matrix. O(m*n)
        pass

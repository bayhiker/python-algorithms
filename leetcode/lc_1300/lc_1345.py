class Solution:
    def minJumps(self, arr: list[int]) -> int:
        return self.min_jumps(arr)

    def min_jumps(self, arr: list[int]) -> int:
        # Use dict to track all occurrences to each unique integer
        # The neighbor of each integer at i is:
        # i - 1, i + 1, d[arr[i]]
        # Then use BFS to search for min distance between 0 and n-1
        pass

from functools import lru_cache
from collections import defaultdict
import math


class Solution:
    def waysToBuildRooms(self, prevRoom: list[int]) -> int:
        return self.ways_to_build_rooms_dfs(prevRoom)

    def ways_to_build_rooms_dfs(self, prev_room: list[int]) -> int:
        # https://walkccc.me/LeetCode/problems/1916/
        mod = 1_000_000_007
        graph = defaultdict(list)
        # Build tree graph, prev_room[i] is parent of i
        for i, prev in enumerate(prev_room):
            graph[prev].append(i)

        def dfs(node: int) -> tuple[int, int]:  # Returns total possibilities and
            if not graph[node]:
                return 1, 1

            ans = 1
            l = 0

            for child in graph[node]:
                temp, r = dfs(child)
                ans = (ans * temp * math.comb(l + r, r)) % mod
                l += r

            return ans, l + 1

        return dfs(0)[0]

    def ways_to_build_rooms_dfs_timed_out(self, prev_room: list[int]) -> int:
        # Branch and bound: TLE
        # This problem converts to: for all permutations of 0:n-1
        # Find the ones that satisfy prev_room constraints
        # Use DFS of all permutations, head back if prev_room[next_number] is not visited yet
        n = len(prev_room)
        counter = 0
        rooms = set(range(n))

        @lru_cache
        def dfs(visited: tuple[int]):
            nonlocal counter
            if len(visited) == n:
                counter += 1
                return
            remaining = rooms - set(visited)
            for r in remaining:
                if prev_room[r] in visited:
                    dfs(tuple(list(visited) + [r]))

        dfs((0,))

        return counter

    def ways_to_build_rooms_dp(self, prev_room: list[int]) -> int:
        pass

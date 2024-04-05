import functools


class Solution:
    def minimumTotalPrice(
        self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]
    ) -> int:
        return self.minimum_total_price(n, edges, price, trips)

    # Adapted from https://walkccc.me/LeetCode/problems/2646/ @pengyuc_
    def minimum_total_price(
        self, n: int, edges: list[list[int]], price: list[int], trips: list[list[int]]
    ) -> int:
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # count[i] times i is traversed for all trips
        count = [0] * n

        def dfs_count(u: int, prev: int, end: int, path: list[int]) -> None:
            path.append(u)
            if u == end:
                for i in path:
                    count[i] += 1
                return
            for v in graph[u]:
                if v != prev:
                    dfs_count(v, u, end, path)
            path.pop()

        for start, end in trips:
            dfs_count(start, -1, end, [])

        @functools.lru_cache(None)
        def dfs(u: int, prev: int, parent_halved: bool) -> int:
            sum_with_full_node = price[u] * count[u]
            for v in graph[u]:
                if v != prev:
                    sum_with_full_node += dfs(v, u, False)

            if parent_halved:  # Can't halve this node if parent was halved.
                return sum_with_full_node

            sum_with_halved_node = (price[u] // 2) * count[u]
            for v in graph[u]:
                if v != prev:
                    sum_with_halved_node += dfs(v, u, True)

            return min(sum_with_full_node, sum_with_halved_node)

        return dfs(0, -1, False)

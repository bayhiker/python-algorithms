class Solution:
    def minCost(
        self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int
    ) -> int:
        return self.min_cost(houses, cost, m, n, target)

    def min_cost(
        self, houses: list[int], cost: list[list[int]], m: int, n: int, target: int
    ) -> int:
        # dp[c][b]: min cost painting the current house with color c, and b blocks
        # While iterating through houses, keep updating dp[c][b] into dp_next
        dp, dp_next = {(0, 0): 0}, {}
        for house_index, curr_color in enumerate(houses):
            # Check all possible colors for current house_index
            color_range = range(1, n + 1) if curr_color == 0 else [curr_color]
            for color in color_range:
                for prev_color, prev_blocks in dp:
                    blocks = prev_blocks + (color != prev_color)
                    if blocks > target:
                        # Exceeding target blocks, cannot paint with this color
                        continue
                    dp_next[color, blocks] = min(
                        dp_next.get((color, blocks), float("inf")),
                        dp[prev_color, prev_blocks]
                        + (cost[house_index][color - 1] if color != curr_color else 0),
                    )
            dp, dp_next = dp_next, {}
        return min(
            [dp[color, blocks] for color, blocks in dp if blocks == target] or [-1]
        )

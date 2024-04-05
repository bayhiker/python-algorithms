from queue import PriorityQueue


class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        return self.trap_rain_water_ii_heap(heightMap)

    def trap_rain_water_ii_heap(self, height_map: list[list[int]]) -> int:
        """
        Now imagine putting this shape into an ocean with sea level starting from
        base of this shape. When water starts to rise, water always flow into the inside
         of this shape via the lowest units. Therefore, we use a min-heap to store visited
        border units to measure how much water can flow into the shape. One observation
        is that the heap contains all current edge units. While popped out units are
        those submerged under water as we let sea level rise.

        When sea level rises until it reaches those lowest items, these items are popped
        out of the heap, and water starts to flow
        into the neighboring units of those lowest items. We look at all neighbors of
        those lowest item. If a neighbor is higher, water cannot flow in, we mark it visited
        and add it into the heap. If a neighbor is lower, we add the diff to total trapped
        water and push (curr_sea_level, neighbor_i, neighbor_j) into the heap.

        Repeat until the heap is empty. Total contains the amount of water this shape can trap

        Args:
            height_map (list[list[int]]): _description_

        Returns:
            int: _description_
        """
        m = len(height_map)
        n = 0 if m == 0 else len(height_map[0])
        if m == 0 or n == 0:
            return 0
        pq = PriorityQueue()
        visited: list[list[bool]] = [[False for j in range(n)] for i in range(m)]

        def get_neighbor(i, j, offset_x, offset_y) -> (int, int):
            (new_x, new_y) = (i + offset_x, j + offset_y)
            if (
                new_x < 0
                or new_x > m - 1
                or new_y < 0
                or new_y > n - 1
                or visited[new_x][new_y]
            ):
                return None
            return (new_x, new_y)

        for j in range(n):
            pq.put((height_map[0][j], 0, j))
            visited[0][j] = True
            pq.put((height_map[m - 1][j], m - 1, j))
            visited[m - 1][j] = True
        for i in range(m):
            pq.put((height_map[i][0], i, 0))
            visited[i][0] = True
            pq.put((height_map[i][n - 1], i, n - 1))
            visited[i][n - 1] = True

        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        total = 0
        while not pq.empty():
            (curr_sea_level, i, j) = pq.get()
            for offset in offsets:
                neighbor = get_neighbor(i, j, offset[0], offset[1])
                if neighbor is None:
                    continue
                neighbor_level = height_map[neighbor[0]][neighbor[1]]
                if neighbor_level < curr_sea_level:
                    total += curr_sea_level - neighbor_level
                    pq.put((curr_sea_level, neighbor[0], neighbor[1]))
                else:
                    pq.put((neighbor_level, neighbor[0], neighbor[1]))
                visited[neighbor[0]][neighbor[1]] = True
        return total

    def trap_rain_water_ii_to_be_fixed(self, height_map: list[list[int]]) -> int:
        """This approach needs to be fixed to make it work.
        For each cell, similar to leetcode 42 (trapping rain water), find min of its
        left_peak, right_peak, top_peak, bottom_peak.
        This is problematic when the shortest xx_peak is not its immediate neighbor,
        5 5 2 5
        5 3 2 5
        5 5 5 5

        height 3 has all four peaks of 5, however, water will leak out from 2-2 direction

        Args:
            height_map (list[list[int]]): _description_

        Returns:
            int: _description_
        """
        m = len(height_map)
        n = 0 if m == 0 else len(height_map[0])
        if m == 0 or n == 0:
            return 0
        min_peak: list[list[int]] = [
            [height_map[i][j] for j in range(n)] for i in range(m)
        ]

        for row in range(m):
            (i, j) = (0, n - 1)
            left_max = height_map[row][i]
            right_max = height_map[row][j]
            while j > i:
                if left_max > right_max:
                    min_peak[row][j] = min(min_peak[row][j], right_max)
                    j -= 1
                    if height_map[row][j] > right_max:
                        right_max = height_map[row][j]
                else:
                    min_peak[row][i] = min(min_peak[row][j], left_max)
                    i += 1
                    if height_map[row][i] > left_max:
                        left_max = height_map[row][i]

        total = 0
        for col in range(n):
            (i, j) = (0, m - 1)
            top_max = height_map[i][col]
            bottom_max = height_map[j][col]
            while j > i:
                if top_max > bottom_max:
                    total += min(min_peak[j][col], bottom_max) - height_map[j][col]
                    j -= 1
                    if height_map[j][col] > bottom_max:
                        bottom_max = height_map[j][col]
                else:
                    total += min(min_peak[j][col], top_max) - height_map[i][col]
                    i += 1
                    if i <= m - 1 and height_map[i][col] > top_max:
                        top_max = height_map[i][col]
        return total

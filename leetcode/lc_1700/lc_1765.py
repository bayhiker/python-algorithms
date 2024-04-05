class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        return self.highest_peak_bfs(isWater)

    def highest_peak_bfs(self, is_water: list[list[int]]) -> list[list[int]]:
        from queue import Queue

        q = Queue()
        m, n = len(is_water), len(is_water[0])
        for i in range(m):
            for j in range(n):
                is_water[i][j] -= 1  # water height is 0, -1 indicates unprocessed cell
                if is_water[i][j] == 0:
                    q.put((0, i, j))

        def get_unvisited_neighbors(i, j) -> list[list[int]]:
            neighbors = []
            for offset_i, offset_j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_i, new_j = i + offset_i, j + offset_j
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                if is_water[new_i][new_j] >= 0:  # visited
                    continue
                neighbors.append([new_i, new_j])
            return neighbors

        while not q.empty():
            height, i, j = q.get()
            neighbors = get_unvisited_neighbors(i, j)
            for neighbor in neighbors:
                is_water[neighbor[0]][neighbor[1]] = height + 1
                q.put((height + 1, neighbor[0], neighbor[1]))
        return is_water

    def highest_peak_heap(self, is_water: list[list[int]]) -> list[list[int]]:
        # This problem is look for max of min distance to water (for any land cell)
        # Similar to ideas used in trapping rain water II (407).
        # We let the sea level rise from 0
        m, n = len(is_water), len(is_water[0])
        result: list[list[bool]] = [[-1 for j in range(n)] for i in range(m)]
        from queue import PriorityQueue

        pq = PriorityQueue()
        for i in range(m):
            for j in range(n):
                if is_water[i][j] == 1:
                    pq.put((0, i, j))
                    result[i][j] = 0

        def get_unvisited_neighbors(i, j) -> list[list[int]]:
            neighbors = []
            for offset_i, offset_j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                new_i, new_j = i + offset_i, j + offset_j
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                if result[new_i][new_j] >= 0:  # visited
                    continue
                neighbors.append([new_i, new_j])
            return neighbors

        max_peak = 0
        while not pq.empty():
            (max_peak, i, j) = pq.get()
            neighbors = get_unvisited_neighbors(i, j)
            for neighbor in neighbors:
                pq.put((max_peak + 1, neighbor[0], neighbor[1]))
                result[neighbor[0]][neighbor[1]] = max_peak + 1
        return result

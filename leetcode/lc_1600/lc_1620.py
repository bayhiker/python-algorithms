from collections import defaultdict
from math import floor, sqrt


class Solution:
    def bestCoordinate(self, towers: list[list[int]], radius: int) -> list[int]:
        return self.best_coordinate(towers, radius)

    def best_coordinate(self, towers: list[list[int]], radius: int) -> list[int]:
        # d[(x_i, y_i)] -> accumulated quality
        d: defaultdict[(int, int):int] = defaultdict(int)
        for tower in towers:
            for delta_x in range(-radius, radius + 1):
                for delta_y in range(-radius, radius + 1):
                    distance = sqrt(delta_x**2 + delta_y**2)
                    if distance > radius:
                        continue
                    d[(tower[0] + delta_x, tower[1] + delta_y)] += floor(
                        tower[2] / (1 + distance)
                    )
        max_quality, best_coordinates = 0, [0, 0]
        for k in sorted(d.keys()):
            if d[k] > max_quality:
                max_quality = d[k]
                best_coordinates = list(k)
        return best_coordinates

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        return self.max_width_off_vertical_area(points)

    def max_width_off_vertical_area(self, points: list[list[int]]) -> int:
        all_x = [point[0] for point in points]
        all_x.sort()
        widest = 0
        for i in range(len(all_x) - 1):
            widest = max(widest, all_x[i + 1] - all_x[i])
        return widest

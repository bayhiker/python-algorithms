class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: list[int], verticalCuts: list[int]
    ) -> int:
        return self.max_area(h, w, horizontalCuts, verticalCuts)

    def max_area(
        self, h: int, w: int, horizontal_cuts: list[int], vertical_cuts: list[int]
    ) -> int:
        horizontal_cuts.sort()
        vertical_cuts.sort()
        horizontal_cuts.append(h)
        vertical_cuts.append(w)
        max_horizontal = horizontal_cuts[0]
        for i in range(1, len(horizontal_cuts)):
            max_horizontal = max(
                horizontal_cuts[i] - horizontal_cuts[i - 1], max_horizontal
            )
        max_vertical = vertical_cuts[0]
        for i in range(1, len(vertical_cuts)):
            max_vertical = max(vertical_cuts[i] - vertical_cuts[i - 1], max_vertical)
        return max_horizontal * max_vertical % (10**9 + 7)

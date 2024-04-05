class Solution:
    def numPoints(self, darts: list[list[int]], r: int) -> int:
        return self.num_points(darts)

    def num_points(self, darts: list[list[int]], r: int) -> int:
        # Solution 1: loop thru every pair of points. Given r, each pair defines two unique
        #      circles of radius r. With each dart in darts, check how many fall in the circles
        # Solution 2: Angle sweep
        #      Each single point P1 (x1,y1) defines a series of circles of radius r with that point on the circle.
        #      Let's imagine we are rotating that circle around P1, and we
        #      define alpha as the angle of the diameter passing thru that point.
        #      For every other point in darts P2 (x2, y2), let
        #      P2 goes into our rotating circle when
        #      alpha is arctan((y2-y1)/(x2-x1)) -
        pass

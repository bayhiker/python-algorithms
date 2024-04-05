# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
    def hasShips(self, topRight: "Point", bottomLeft: "Point") -> bool:
        pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: Sea, topRight: Point, bottomLeft: Point) -> int:
        return self.count_ships(sea, topRight, bottomLeft)

    def count_ships(self, sea: Sea, top_right: Point, bottom_left: Point) -> int:
        # Use recursion and 2-D binary search to pinpoint each ship.
        # Divide each square into 4 sub-squares,
        # Use sea.hasShips() to check if a specific quarter has a ship
        # Keep going until all ships are identified
        pass

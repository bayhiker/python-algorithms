class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        return self.find_farmland(land)

    def find_farmland(self, land: list[list[int]]) -> list[list[int]]:
        # Traverse the whole matrix, for each node, check if it is the top left corder
        # of a rectangle (must be border or forest on the left and on top of it). If it
        # is, expand to the right and down as much as possible to find the max rectangle
        pass

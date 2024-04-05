class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        return self.num_of_burgers(tomatoSlices, cheeseSlices)

    def num_of_burgers(self, tomatoSlices: int, cheeseSlices: int) -> list[int]:
        total_jumbo = (tomatoSlices - 2 * cheeseSlices) / 2
        total_small = (4 * cheeseSlices - tomatoSlices) / 2

        if total_small < 0 or total_jumbo < 0:
            return []

        if total_jumbo != int(total_jumbo) or total_small != int(total_small):
            return []

        return [int(total_jumbo), int(total_small)]

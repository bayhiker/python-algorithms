class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        return self.find_radius(houses, heaters)

    def find_radius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()
        m, n = (len(houses), len(heaters))
        # Add -inf and inf on ends of heaters to unify radius calculation
        heaters.insert(0, float("-inf"))
        heaters.append(float("inf"))
        heater_left_index, heater_right_index, i = 0, 1, 0
        max_radius = 0
        while heater_right_index < n + 2:
            heater_left, heater_right = (
                heaters[heater_left_index],
                heaters[heater_right_index],
            )
            # Look at radius until heater_right_index, or until m if heater_right is inf
            check_until = m - 1 if heater_right_index == n + 1 else heater_right_index
            while i < m and houses[i] <= heater_right:
                radius = min(houses[i] - heater_left, heater_right - houses[i])
                if radius > max_radius:
                    max_radius = radius
                i += 1
            heater_left_index += 1
            heater_right_index += 1
        # max_radius is the farthest distance between a house and nearest heater
        return max_radius

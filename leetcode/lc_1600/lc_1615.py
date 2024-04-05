class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        return self.maximal_network_rank(n, roads)

    def maximal_network_rank(self, n: int, roads: list[list[int]]) -> int:
        cities: dict[int : list[int]] = {i: [] for i in range(n)}
        road_counts: dict[int : list[int]] = {i: [] for i in range(n)}
        road_counts[0] = [i for i in range(n)]
        for road in roads:
            for i in [0, 1]:
                cities[road[i]].append(road[1 - i])
                road_count = len(cities[road[i]])
                road_counts[road_count].append(road[i])
                road_counts[road_count - 1].remove(road[i])
        # Cities that contain the city with top degrees
        city_group_1 = []
        # Cities that contain the city with runner-up degrees
        city_group_2 = []
        for i in range(n - 1, -1, -1):
            if len(city_group_2) > 0:
                # Found both cities
                break
            cities_with_len_i = road_counts[i]
            if len(road_counts[i]) > 0:
                if len(city_group_1) > 0:
                    city_group_2 = cities_with_len_i
                else:
                    city_group_1 = cities_with_len_i
                    if len(cities_with_len_i) > 1:
                        city_group_2 = cities_with_len_i

        for city_1 in city_group_1:
            for city_2 in city_group_2:
                if city_1 == city_2:
                    continue
                if city_2 not in cities[city_1]:
                    return len(cities[city_1]) + len(cities[city_2])
        return len(cities[city_1]) + len(cities[city_2]) - 1

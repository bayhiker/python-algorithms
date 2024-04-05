class Solution:
    def numberOfCleanRooms(self, room: list[list[int]]) -> int:
        return self.number_of_clean_rooms(room)

    def number_of_clean_rooms(self, room: list[list[int]]) -> int:
        visited: dict[str:bool] = {}
        cleaned: set[str] = set()
        i = 0
        j = 0
        direction = 90
        while f"{i}-{j}-{direction}" not in visited:
            visited[f"{i}-{j}-{direction}"] = True
            cleaned.add(f"{i}-{j}")
            next_i = (
                i
                if direction == 90 or direction == 270
                else i + 1
                if direction == 180
                else i - 1
            )
            next_j = (
                j
                if direction == 0 or direction == 180
                else j + 1
                if direction == 90
                else j - 1
            )
            if (
                next_i < 0
                or next_i >= len(room)
                or next_j < 0
                or next_j >= len(room[i])
                or room[next_i][next_j] == 1
            ):
                direction = (direction + 90) % 360
            else:
                i = next_i
                j = next_j
            print(f"next: {i}, {j}, {direction}")
        return len(cleaned)

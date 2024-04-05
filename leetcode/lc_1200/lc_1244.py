class Leaderboard:
    def __init__(self):
        self.scores: list[(int, int)] = []
        # Maintain self.scores as a sorted list (player_id, score), sorted by score in non-inc order
        # addScore uses bisect.bisect() to find insertion point and insert (player_id, score)
        # top(k) returns sum of scores of the first k elements
        # reset() removes player_id from list
        pass

    def addScore(self, playerId: int, score: int) -> None:
        return self.add_score(playerId, score)

    def add_score(self, player_id: int, score: int) -> None:
        pass

    def top(self, k: int) -> int:
        pass

    def reset(self, player_id: int) -> None:
        pass

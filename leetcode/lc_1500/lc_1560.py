class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        return self.most_visited(n, rounds)

    def most_visited(self, n: int, rounds: list[int]) -> list[int]:
        first, last = rounds[0], rounds[len(rounds) - 1]

        return (
            [i for i in range(first, last + 1)]
            if first <= last
            else [i for i in range(1, last + 1)] + [i for i in range(first, n + 1)]
        )

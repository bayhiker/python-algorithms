class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        return self.escape_ghosts(ghosts, target)

    def escape_ghosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        # (A) min_distance(ghost, target) <= min_distance(you, target)
        # (B) ghost can catch target
        # A => B: if A, ghost goes to target and wait for you, catch
        # B => A, logical equivalent to not A => not B, obviously, if min(ghost, target)
        #     is larger than your distance, you can go directly to target, so no catch
        distances: list[int] = [
            abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) for ghost in ghosts
        ]
        for distance in distances:
            if distance <= abs(target[0]) + abs(target[1]):
                return False
        return True

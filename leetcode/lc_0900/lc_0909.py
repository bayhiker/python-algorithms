from collections import deque
from math import ceil


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        if board is None:
            return 0
        n = len(board)
        if n <= 1:
            return 0

        def k2ij(k: int):
            i = n - ceil(k / 6)
            j = (k - 1) % n if (n - i) % 2 else (n - 1 - (k - 1)) % n
            return [i, j]

        steps: int = 0
        dq = deque()
        dq.append(1)
        dq.append(None)
        while len(dq) > 0:
            head = dq.popleft()
            if head is None:
                steps += 1
                dq.append(None)
                continue
            for r in range(1, 7):
                k = head + r
                if k == n**2:
                    return steps + 1
                [i, j] = k2ij(k)
                if board[i][j] == -1 and k not in dq:
                    dq.append(k)
                elif board[i][j] > 0 and board[i][j] > k:
                    dq.append(board[i][j])

        return -1

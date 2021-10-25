from typing import List

# The problem is specified in TED-ED youtube video: Can you solve this virus riddle
# https://www.youtube.com/watch?v=ZKh6z0X6KRw


class VirusMatrixRecursive:
    def __init__(self, n) -> None:
        self.n = n
        self.START_NODE = 0
        self.EXIT_ROOM = self.n ** 2 - 1
        self.valid_paths = []

    def solve(self, visited: list = None, remaining: list = None):
        if remaining is None:
            remaining = []
            for i in range(1, self.n ** 2):
                remaining.append(i)
        if visited is None:
            visited = [0]

        if len(visited) == 0 or len(remaining) == 0:
            raise ValueError("Neither visited nor remaining can be empty")
        if len(remaining) == 1:
            if self.same_room(remaining[0], self.EXIT_ROOM) and self.can_visit(
                self.last_visited(visited), remaining[0]
            ):
                visited.append(remaining.pop())
                self.valid_paths.append(visited)
            return
        neighbor_found = False
        for room in remaining:
            if self.can_visit(self.last_visited(visited), room):
                neighbor_found == True
                updated_visited = [i for i in visited if i != room]
                updated_visited.append(room)
                self.solve(updated_visited, [i for i in remaining if i != room])
        if not neighbor_found:
            return

    def same_room(self, room1, room2):
        return room1 // self.n == room2 // self.n and room1 % self.n == room2 % self.n

    def last_visited(self, visited):
        return visited[len(visited) - 1]

    def can_visit(self, current, next):
        x_diff = abs(current // self.n - next // self.n)
        y_diff = abs(current % self.n - next % self.n)
        return (x_diff == 1 and y_diff == 0) or (x_diff == 0 and y_diff == 1)


class VirusMatrixBacktrack:
    def __init__(self, n) -> None:
        # Init virus matrix
        self.n = n
        self.matrix = []
        for i in range(0, n):
            virus_vector = []
            for j in range(0, n):
                virus_vector.append(1)
            self.matrix.append(virus_vector)
        self.matrix[0][0] = 0
        self.pruned_branches = set()
        self.MAX_TRIES = 1000000

    def solve(self):
        stack = [(0, 0)]
        counter = 0
        while len(stack) > 0 and len(stack) < self.n * self.n:
            counter += 1
            if counter > self.MAX_TRIES:
                break
            head = stack[len(stack) - 1]
            neighbor = self.get_neighbor(stack, head[0], head[1])
            if neighbor is None:
                self.matrix[head[0]][head[1]] = 1
                self.add_pruned_branch(stack)
                stack.pop()
                continue
            self.matrix[neighbor[0]][neighbor[1]] = 0
            stack.append(neighbor)
        if len(stack) == self.n * self.n:
            print(f"Found, stack is {self.get_path(stack)}")
            return stack
        else:
            print(f"Not found, {len(self.pruned_branches)} path pruned.")
            return None

    def can_visit(self, stack, i, j):
        if i < 0 or j < 0 or i >= self.n or j >= self.n:
            return False
        if self.matrix[i][j] == 0:
            return False
        if i == self.n - 1 and j == self.n - 1 and len(stack) < self.n * self.n - 1:
            return False
        if self.get_path(stack, (i, j)) in self.pruned_branches:
            return False
        return True

    def get_neighbor(self, stack, i, j):
        if self.can_visit(stack, i + 1, j):
            return (i + 1, j)
        if self.can_visit(stack, i - 1, j):
            return (i - 1, j)
        if self.can_visit(stack, i, j - 1):
            return (i, j - 1)
        if self.can_visit(stack, i, j + 1):
            return (i, j + 1)
        return None

    def get_sn(self, neighbor):
        return None if not neighbor else neighbor[0] * self.n + neighbor[1]

    def get_path(self, stack, neighbor=None):
        path = ""
        for item in stack:
            path += f"-{self.get_sn(item)}"
        if neighbor:
            path += f"-{self.get_sn(neighbor)}"
        return path

    def add_pruned_branch(self, stack):
        self.pruned_branches.add(self.get_path(stack))


# This is a DP solution to the generic Hamiltonian Path problem
# Reference https://www.hackerearth.com/practice/algorithms/graphs/hamiltonian-path/tutorial/
def has_hamiltonian_path_dp(adj: List[List[int]]):
    total_nodes = len(adj)
    # dp[i][j]: if there is a path to node i, covering all nodes indicated by bits in
    # n-digit number j, going through each node once and only once
    total_masks = 1 << total_nodes  # or 2**total_nodes
    dp = [[False for i in range(0, total_masks)] for j in range(0, total_nodes)]
    for i in range(0, total_nodes):
        dp[i][1 << i] = True  # i th room always can reach itself
    for i in range(0, total_masks):
        for j in range(0, total_nodes):
            if i & 1 << j:  # j'th bit is set, meaning j'th room is included in mask i
                for k in range(0, total_nodes):
                    if (
                        j != k
                        and i & 1 << k  # k'th room is included in i also
                        and adj[k][j]
                        and dp[k][i ^ 1 << j]  # Same mask as i, excluding room j
                    ):
                        dp[j][i] = True
                        break
    for i in range(0, total_nodes):
        if dp[i][total_masks - 1]:
            return True
    return False


def solve_virus_matrix_dp(n: int):
    def is_neighbor(room1, room2):
        x_diff = abs(room1 // n - room2 // n)
        y_diff = abs(room1 % n - room2 % n)
        return (x_diff == 0 and y_diff == 1) or (x_diff == 1 and y_diff == 0)

    total_rooms = n ** 2
    total_masks = 1 << total_rooms  # or 2**total_rooms
    # dp[x][y]: value is path that starts with the top-left room,
    # ends up in room x, and goes through rooms indicated by 1 digits in
    # total_rooms digit number y, through each room once and only once.
    # For example: 0-1-2-3
    dp = [["" for i in range(0, total_masks)] for j in range(0, total_rooms)]
    dp[0][1] = "0"
    for i in range(0, total_masks):
        for j in range(0, total_rooms):
            if i & 1 << j:  # j'th bit is set, meaning j'th room is included in mask i
                for k in range(0, total_rooms):
                    if (
                        j != k
                        and i & 1 << k  # k'th room is included in i also
                        and is_neighbor(k, j)
                        and dp[k][i ^ 1 << j]  # Same mask as i, excluding room j
                    ):
                        dp[j][i] = f"{dp[k][i^1<<j]}-{j}"
                        break
    return dp[total_rooms - 1][total_masks - 1] or None


def test_virus_riddle_backtrack():
    virus_matrix_backtrack = VirusMatrixBacktrack(3)
    assert virus_matrix_backtrack.solve() is not None
    virus_matrix_backtrack = VirusMatrixBacktrack(4)
    assert virus_matrix_backtrack.solve() is None


def test_virus_riddle_recursive():
    virus_matrix_recursive = VirusMatrixRecursive(3)
    virus_matrix_recursive.solve()
    assert len(virus_matrix_recursive.valid_paths) == 2
    print(f"{len(virus_matrix_recursive.valid_paths)} paths found")
    for path in virus_matrix_recursive.valid_paths:
        print(f"{'-'.join([str(room) for room in path])}")
    virus_matrix_recursive = VirusMatrixRecursive(4)
    virus_matrix_recursive.solve()
    assert len(virus_matrix_recursive.valid_paths) == 0


def test_has_hamiltonian_path():
    # 0---1---3
    # |---2
    adj = [[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0], [0, 1, 0, 1]]
    assert has_hamiltonian_path_dp(adj)
    # 0---1-X-3
    # |---2
    adj = [[1, 1, 1, 0], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]]
    assert not has_hamiltonian_path_dp(adj)


def test_solve_virus_matrix_dp():
    assert solve_virus_matrix_dp(1) == "0"
    assert solve_virus_matrix_dp(2) is None
    path = solve_virus_matrix_dp(3)
    assert path is not None
    print(f"Path found when n=3 is {path}")
    assert solve_virus_matrix_dp(4) is None
    # Takes a long time to run
    # path = solve_virus_matrix_dp(5)
    # assert path is not None
    # print(f"Path found when n=5 is {path}")

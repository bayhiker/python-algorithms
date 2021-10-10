from .virus_riddle import (
    VirusMatrixBacktrack,
    VirusMatrixRecursive,
    has_hamiltonian_path_dp,
    solve_virus_matrix_dp,
)


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

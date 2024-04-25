from functools import reduce


#
# Dijkstra Algorithm, weights must be non-negative
#
def get_dijkstra_distance(
    nodes: list[int], edges: list[list[int]], source: int, target: int
) -> float:
    n = len(nodes)
    out_edges: dict[int, list[list[int]]] = {}
    for s, t, w in edges:
        if s not in out_edges:
            out_edges[s] = []
        out_edges[s].append((t, w))

    distances: dict[int:float] = {x: float("inf") for x in nodes}
    visited: dict[int:bool] = {x: False for x in nodes}
    distances[source] = 0

    while True:
        # Find minimum distance in the list of nodes that are not yet visited
        min_node = min(
            distances, key=lambda x: float("inf") if visited[x] else distances[x]
        )
        if distances[min_node] == float("inf"):
            # No more connected nodes
            break
        visited[min_node] = True
        if sum(1 for x in visited if visited[x]) == n:
            # All nodes visited
            break

        next_nodes = out_edges[min_node] if min_node in out_edges else []
        for t, w in next_nodes:
            # Update next nodes with the new min path found
            if distances[t] > distances[min_node] + w:
                distances[t] = distances[min_node] + w

    return distances[target]


def test_dict_min():
    distances = {1: 5, 2: 8, 3: 2}
    visited = {1: False, 2: False, 3: False}
    get_dist = lambda x: float("inf") if visited[x] else distances[x]
    assert min(distances, key=get_dist) == 3
    visited = {1: False, 2: False, 3: True}
    assert min(distances, key=get_dist) == 1


def test_dijkstra_distance() -> None:
    nodes = [0, 1, 2, 3, 4, 5, 6]
    edges = [
        [0, 1, 2],
        [0, 2, 6],
        [1, 3, 5],
        [2, 3, 8],
        [3, 4, 10],
        [3, 5, 15],
        [4, 5, 6],
        [4, 6, 2],
        [5, 6, 6],
    ]
    assert get_dijkstra_distance(nodes, edges, 0, 6) == 19
    assert get_dijkstra_distance(nodes, edges, 0, 5) == 22


def test_dijkstra_large_weights() -> None:
    nodes = [0, 1, 2, 3, 4, 5, 6]
    edges = [
        [0, 1, 2],
        [0, 2, 6],
        [1, 3, 1000],
        [2, 3, 8],
        [3, 4, 10],
        [3, 5, 15],
        [4, 5, 6],
        [4, 6, 2],
        [5, 6, 6],
    ]
    assert get_dijkstra_distance(nodes, edges, 0, 6) == 26

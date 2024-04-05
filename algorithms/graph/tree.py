# Dijkstra Algorithm, weights need to be non-negative
def get_dijkstra_distance(
    nodes: list[int], edges: list[list[int]], source: int, target: int
) -> float:
    n = len(nodes)
    out_edges: dict[int, list[list[int]]] = {}
    for s, t, w in edges:
        if s not in out_edges:
            out_edges[s] = []
        out_edges[s].append((t, w))

    distances: list[int] = [float("inf")] * n
    distances[source] = 0

    curr_node = source
    while True:
        next_nodes = out_edges[curr_node] if curr_node in out_edges else {}
        next_node, min_edge = None, float("inf")

        for t, w in next_nodes:
            # Update next nodes,
            # find the smallest edge that lowered distance of corresponding node
            if distances[t] > distances[curr_node] + w:
                distances[t] = distances[curr_node] + w
                if w < min_edge:
                    min_edge = w
                    next_node = t
        if next_node is None:
            break
        curr_node = next_node

    return distances[target]


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

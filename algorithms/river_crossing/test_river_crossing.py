from .river_crossing import RiverCrossing


def test_valid_states():
    river_crossing = RiverCrossing(num_lions=3, num_wildebeests=3)

    print()
    for valid_state in river_crossing.valid_states:
        print(valid_state.pretty_print(print_next=True))

    path = river_crossing.traverse_bfs()
    print()
    if not path:
        print("No path found with DFS")
    else:
        print("Valid path found from BFS!")
        for state in path:
            print(f"-> {state.pretty_print()}")

    path = river_crossing.traverse_dfs()
    print()
    if not path:
        print("No path found with DFS")
    else:
        print("Valid path found from DFS!")
        for state in path:
            print(f"-> {state.pretty_print()}")

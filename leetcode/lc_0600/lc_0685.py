class Solution:
    def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        return self.find_redundant_directed_connection(edges)

    def find_redundant_directed_connection(self, edges: list[list[int]]) -> list[int]:
        # Because graph is directed, adding an edge doesn't mean having a loop.
        # If all nodes have only one parent, then there's a loop, union find to search
        # If there is a node with two parents and there is a loop, still the last edge that causes loop
        # If there is a node with two parent and there is no loop, remove the last edge that causes double parent

        def find_parent(parent, u):
            if parent[u] == u:
                return u
            return find_parent(parent, parent[u])

        n = len(edges)
        parent = [i for i in range(n + 1)]
        # e1 and e2 are the two possible extra edges
        e1, e2, visited = None, None, {}
        for x, y in edges:
            if y in visited:
                # Found node with two parents
                e1, e2 = visited[y], [x, y]
                break
            visited[y] = [x, y]
        # If e1 and e2 aren't set, meaning all nodes have only one parent
        # then there must be a loop, the following union find algorithm will find the loop
        for x, y in edges:
            if [x, y] == e2:
                continue
            a = find_parent(parent, x)
            b = find_parent(parent, y)

            if a == b:
                # There is a loop
                if e1:
                    return e1
                return [x, y]
            parent[b] = a
        return e2

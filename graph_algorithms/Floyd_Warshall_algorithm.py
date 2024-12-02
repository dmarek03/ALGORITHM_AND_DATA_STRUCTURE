# Floyd-Warshall algorithm for finding the shortest paths between every pair of vertices in a given
# directed weighted graph.
import copy
from math import inf
# COMPLEXITY O(V^3)


def floyd_warshall_algorithm(matrix):
    n = len(matrix)

    # Create a copy of a graph as we have to have lengths
    # of edges stored at the beginning of an algorithm
    W = copy.deepcopy(matrix)

    # B[i][j] - a vetrex on the shortest path from i to j
    # for which a path has the lowest total weight (length)
    B = [[None] * n for _ in range(n)]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]
                    B[i][j] = t

    # Detect negative cycles (the same approach as in the
    # Bellman-Ford's algoritm)
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = -inf
                    B[i][j] = -1

    return W, B


def get_shortest_path(B, s , t):
    # Check if there is a path
    if B[s][t] is None:
        return None
    # Check if we have a negative cycle (there is no shortest path)
    if B[s][t] < 0:
        return []

    path = []

    # Recursively restore a path
    def recur(i, j):
        if B[i][j] is None:
            return path.append(i)
        recur(i, B[i][j])
        recur(B[i][j], j)

    recur(s, t)
    path.append(t)

    return path


def directed_weighted_graph_matrix(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[inf] * n for _ in range(n)]  # -1 means no edge
    for e in E:
        G[e[0]][e[1]] = e[2]
    return G


E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]

graph = directed_weighted_graph_matrix(E)

W, B = floyd_warshall_algorithm(graph)
print(*W, sep='\n', end='\n\n')
print(f'shortest path from v1 to v2 = {W[0][8]} ')
print(get_shortest_path(B, 0, 8))
print(get_shortest_path(B, 0, 9))
print(get_shortest_path(B, 0, 3))
print(get_shortest_path(B, 1, 7))
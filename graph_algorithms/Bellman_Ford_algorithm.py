# Bellman-Ford algorithm for finding the shortest paths from source vertex to all other vertices in
# a given graph in which edge weights may be negative.
# 1) ADJACENCY_LIST

from math import  inf
def bellman_ford(G, s):
    n = len(G)
    weights = [inf] * n
    parents = [None] * n
    weights[s] = 0

    # Calculate the shortest paths distances
    for _ in range(n):
        for u in range(n):
            for v, weight in G[u]:
                if weights[u] + weight < weights[v]:
                    weights[v] = weights[u] + weight
                    parents[v] = u

    # Look for negative cycles and replace distances
    # with a -infinity if a vertex is affected by
    # a negative cycle
    for _ in range(n):
        for u in range(n):
            for v, weight in G[u]:
                # If we still can relax a u vertex, there
                # must be a negative cycle
                if weights[u] + weight < weights[v]:
                    weights[v] = -inf

    return weights, parents


def get_shortest_path(G, s, t):
    weights, parents = bellman_ford(G, s)
    if weights[t] == -inf:
        # When there is a negative cycle, there is no shortest path (this is endless)
        return None

    path = []
    while t != s:
        path.append(t)
        t = parents[t]
    path.append(s)

    return path[::-1]


def directed_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append([e[1], e[2]])
    return G


E = [(0, 1, 5), (1, 6, 60), (6, 7, -50), (7, 8, -10), (5, 6, 5), (1, 5, 30), (5, 8, 50), (1, 2, 20),
     (2, 3, 10), (3, 2, -15), (2, 4, 75), (4, 9, 100), (5, 4, 25)]
# G = directed_weighted_graph_list(E)
# print(*G, sep='\n')
# print(bellman_ford(G, 0))
# print(get_shortest_path(G, 0, 9))



# 2) MATRIX


def bellman_ford(G: 'graph represented by adjacency matrix', s: 'source'):
    n = len(G)
    weights = [inf] * n
    parents = [None] * n
    weights[s] = 0

    # Calculate the shortest paths distances
    for _ in range(n):
        for u in range(n):
            for v in range(n):
                # Continue if there is no edge
                if G[u][v] == inf:
                    continue
                if weights[u] + G[u][v] < weights[v]:
                    weights[v] = weights[u] + G[u][v]
                    parents[v] = u

    # Look for negative cycles and replace distances
    # with a -infinity if a vertex is affected by
    # a negative cycle
    for _ in range(n):
        for u in range(n):
            for v in range(n):
                # Continue if there is no edge
                if G[u][v] == inf:
                    continue
                # If we still can relax a u vertex, there
                # must be a negative cycle
                if weights[u] + G[u][v] < weights[v]:
                    weights[v] = -inf

    return weights, parents


def get_shortest_path(G, s, t):
    weights, parents = bellman_ford(G, s)
    if weights[t] == -inf:
        # When there is a negative cycle, there is no shortest path (this is endless)
        return None

    path = []
    while t != s:
        path.append(t)
        t = parents[t]
    path.append(s)

    return path[::-1]


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
G = directed_weighted_graph_matrix(E)
print(*G, sep='\n')
print(bellman_ford(G, 0)[0])
print(get_shortest_path(G, 0, 9))
print(get_shortest_path(G, 0, 8))
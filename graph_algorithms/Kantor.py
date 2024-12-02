import copy
import math


def create_graph(K):
    n = 0
    for e in K:
        n = max(n, e[0], e[1])
    n += 1

    G = [[0] * n for _ in range(n)]
    for e in K:
        G[e[0]][e[1]] = math.log(e[2])
    return G


def floyd_warshall(G: 'graph represented by adjacency matrix'):
    n = len(G)
    inf = float('inf')

    # Create a copy of a graph as we have to have lengths
    # of edges stored at the beginning of an algorithm
    W = copy.deepcopy(G)

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]

    # Detect negative cycles (the same approach as in the
    # Bellman-Ford's algoritm)
    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = -inf

    return W


def can_rise(K):
    G = create_graph(K)
    W = floyd_warshall(G)
    n = len(G)
    for i in range(n):
        for j in range(n):
            if W[i][j] == float('-inf'):
                return True
    return False
from egzP7atesty import runtests
from math import inf


def ford_fulkerson(G, s, t):
    n = len(G)
    flow = [[0] * n for _ in range(n)]
    visited = [0] * n
    token = 1  # Number of iteration to check which vertices have been visited
    max_flow = 0

    def dfs(u, bottleneck):
        visited[u] = token

        if u == t:
            return bottleneck

        for v in range(n):
            remaining = G[u][v] - flow[u][v]
            if visited[v] != token and remaining > 0:
                new_bottleneck = dfs(v, min(remaining, bottleneck))
                if new_bottleneck:
                    flow[u][v] += new_bottleneck
                    flow[v][u] -= new_bottleneck
                    return new_bottleneck
        return 0

    while True:
        increase = dfs(s, inf)
        if not increase:
            break
        max_flow += increase
        token += 1

    return max_flow

#

def akademik( T ):
    #ADJACENCY LIST
    s = len(T)*2
    t = s+1
    n = t+1
    n1 = len(T)

    graph = [[] for _ in range(n)]
    for i in range(n1):
        for j in range(3):
            if T[i][j] is not None:
                graph[i].append(n1+T[i][j])

    for i in range(n1):
        graph[s].append(i)
        graph[n1+i].append(t)

    pustych = 0


    for i in range(n1):
        if T[i] == (None, None, None):
            pustych += 1

    #ADJACENCY MATRIX

    graph1 = [[0]*n for _ in range(n)]
    for i in range(len(graph)):
        for nb in graph[i]:
            graph1[i][nb] = 1



    return n1-pustych-ford_fulkerson(graph1, s, t)



runtests ( akademik )
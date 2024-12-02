from math import inf
import collections


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return


def Floyd_Warshall_algorithm(graph):
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance


def BlueAndGreen(T, K, D):
    graph = [[0] * (len(T) + 2) for _ in range(len(T) + 2)]
    distance = Floyd_Warshall_algorithm(T)
    for i in range(len(T)):
        for j in range(len(T)):
            if distance[i][j] >= D and distance[i][j] != inf:
                if K[i] == 'B' and K[j] == 'G':
                    graph[i][j] = graph[j][len(T) + 1] = graph[len(T)][i] = 1
    return edmonds_karp(graph, len(T), len(T) + 1)
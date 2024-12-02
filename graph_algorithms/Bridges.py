# An edge in consistent undirected graph is called a bridge if its removal spreads the graph.
from math import inf

# COMPLEXITY O(E+V) -> O(V^2)
def bridge(graph):
    n = len(graph)
    visited = [False] * n
    time_visit = [0] * n
    low = [inf] * n
    parent = [None] * n
    time = 0
    bridges = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited, parent, time_visit, time, low)
    for i in range(n):
        if time_visit[i] == low[i] and parent[i] is not None:
            bridges.append((parent[i], i))
    return bridges


def dfs(graph, source, visited, parent, time_visit, time, low):
    visited[source] = True
    time_visit[source] = time
    time += 1
    low[source] = time_visit[source]
    for v in graph[source]:
        if not visited[v]:
            parent[v] = source
            dfs(graph, v, visited, parent, time_visit, time, low)
            low[source] = min(low[source], low[v])
        elif parent[source] != v:
            low[source] = min(low[source], time_visit[v])


graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
graph1 = [[1, 2,] , [0, 2],[0, 1, 3, 5],[2, 4],[3],[2, 6, 8],[5, 7],[8, 6],[5, 7]]
print(*graph, sep='\n')
print("--------------")
print(bridge(graph1))
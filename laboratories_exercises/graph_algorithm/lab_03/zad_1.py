"""
Implementacja algorytmu djikstry dla grafu gęstego
"""
from math import inf

def dijkstra(graph, source):
    n = len(graph)
    distance = [inf] * n
    distance[source] = 0
    visited = [False]*n
    visited[source] = True
    parents = [None]*n

    for i in range(n):
        pass



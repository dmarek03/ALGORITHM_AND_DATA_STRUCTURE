# Checking connectivity using BFS i DFS
from collections import deque

# BFS

def bfs(adj_list):
    n = len(adj_list)
    res = []
    visited = [False]*n
    dequeue = deque()
    dequeue.append(0)
    visited[0] = True
    while dequeue:
        u = dequeue.popleft()
        res.append(u)
        for v in adj_list[u]:
            if not visited[v]:
                dequeue.append(v)
                visited[v] = True
    return all(visited), res if all(visited) else None


graph = [
    [1, 8],
    [0],
    [3, 4, 5, 8],
    [2],
    [2, 7],
    [2, 6],
    [5, 7, 8],
    [4, 6],
    [0, 2, 6]
]
print(bfs(graph))

# DFS


def DFS_adjacency_list(adj_list):
    visited = [False] * len(adj_list)
    res = []

    def dfs_visit(u):
        visited[u] = True
        res.append(u)
        for v in adj_list[u]:
            if not visited[v]:
                dfs_visit(v)
    dfs_visit(0)
    return all(visited), res if all(visited) else None

print(DFS_adjacency_list(graph))
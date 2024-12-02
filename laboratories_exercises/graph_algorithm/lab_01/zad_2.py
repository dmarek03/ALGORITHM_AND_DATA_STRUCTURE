"""
Sprawdzamy czy graf jest spójny
"""


def dfs(graph):

    visited = [0]*len(graph)

    def vdfs(vertex):
        nonlocal graph
        nonlocal visited
        visited[vertex] = 1
        for u in graph[vertex]:
            if not visited[u]:
                vdfs(u)


    vdfs(0)

    for flag in visited:
        if not flag:
            return False
    return True



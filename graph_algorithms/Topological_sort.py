# DAG is a directed acyclic graph
# Topological sorting of DAG consists in arranging the vertices in order that the edges point
# only from left to right.


# 1 solution
def dfs(graph, source, visited, result):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result)
    # Inserting the processed vertex at the top of the results list
    result.insert(0, source)


def topological_sort(graph):
    n = len(graph)
    visited = [False] * n
    result = []
    for u in range(n):
        if not visited[u]:
            dfs(graph, u, visited, result)
    return result


graph = [[1, 2],
         [2, 3],
         [],
         [4, 5, 6],
         [],
         [],
         [],
         [3],
         [7]]
print(topological_sort(graph))


# 2 solution

def topological_sort2(G: 'graph represented using adjacency lists'):
    n = len(G)
    visited = [False] * n
    result = [None] * n
    idx = n

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal idx
        idx -= 1
        result[idx] = u

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return result

print(topological_sort2(graph))
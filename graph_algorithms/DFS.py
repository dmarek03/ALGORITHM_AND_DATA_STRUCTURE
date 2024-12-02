# DEPTH-FIRST-SEARCH


# 1 ADJACENCY LIST

# First solution
def DFS_adjacency_list(adj_list, source):
    visited = [False] * len(adj_list)
    result = [source]

    def dfs_visit(u, graph, visited, result):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                result.append(v)
                dfs_visit(v, graph, visited, result)

    dfs_visit(source, adj_list, visited, result)
    return result

graph = [[1, 8], [0], [3, 4, 5, 8], [2], [2, 7], [2, 6], [5, 8], [4, 6], [0, 2, 6]]

result1 = DFS_adjacency_list(graph, 4)
print(result1)


# Second solution

def dfs_adj(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs_adj(graph, n, visited)
    return visited

result2 = dfs_adj(graph, 1, [])
print(result2)



# 2 MATRIX


def DFS_matrix(graph, root):
    visited = [False] * len(graph)
    result = []
    dfs_visit(root, graph, visited, result)
    return result


def dfs_visit(u, graph, visited, result):
    visited[u] = True
    result.append(u)
    for i in range(len(graph)):
        if not visited[i] and graph[u][i] == 1:
            dfs_visit(i, graph, visited, result)


graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(DFS_matrix(graph, 2))
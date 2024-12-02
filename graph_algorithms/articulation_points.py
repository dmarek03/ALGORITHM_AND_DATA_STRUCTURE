def find_articulation_points(graph):
    n = len(graph)
    low = [0] * n
    times = [0] * n
    is_art = [False] * n
    time = 0

    def dfs(root, u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        out_deg = 0

        for v in graph[u]:
            if v == parent:
                continue
            if not times[v]:
                out_deg += dfs(root, v, u) + u == root
                low[u] = min(low[u], low[v])
                if times[u] <= low[v]:
                    is_art[u] = True
            else:
                low[u] = min(low[u], times[v])

        return out_deg

    # Check all possible starting vertices as a graph doesn't have to be consistent
    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return [u for u in range(n) if is_art[u]]


def dfs(graph, visited, i, ban):
    visited[i] = 1
    for nb in graph[i]:
        if visited[nb] == 0 and nb != ban:
            dfs(graph, visited,  nb, ban)


def articulation(graph):
    n = len(graph)
    articulation_points = []
    for i in range(n):
        visited = [0]*n
        if i != 0:
            dfs(graph, visited, 0, i)

        else:
            dfs(graph, visited, 1, i)

        if sum(visited) < n-1:
            articulation_points.append(i)
    return articulation_points


def undirected_graph_list(edges_list, n):
    G = [[] for _ in range(n)]
    for edge in edges_list:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])
    return G


E = [(0, 1), (0, 2), (2, 1), (2, 3), (3, 4), (2, 5), (5, 6), (8, 5), (8, 7), (6, 7), (2, 8)]
G = undirected_graph_list(E, 9)
print(articulation(G))
print(find_articulation_points(G))

from queue import Queue
from math import inf


def colorize_vertices(graph):
    n = len(graph)

    # 0 means no color (we will use 2 colors as we want to divide vertices
    # into two disjoint sets)
    colors = [0] * n

    def dfs(u):
        for v in graph[u]:
            if not colors[v]:
                colors[v] = -1 * colors[u]
                if not dfs(v):
                    return False
            elif colors[v] == colors[u]:
                return False
        return True

    for u in range(n):
        if not colors[u]:
            colors[u] = 1
            if not dfs(u):
                return []  # Return an empty list if a graph is not bipartite

    return colors


def bfs(graph, s, t, parents, visited, token):
    n = len(graph)
    q = Queue()
    q.put(s)
    visited[s] = token

    while not q.empty():
        u = q.get()
        for v in range(n):
            if not graph[u][v] or visited[v] == token:
                continue
            q.put(v)
            visited[v] = token
            parents[v] = u

    return visited[t] == token


def get_bottleneck(graph, s, t, parents):
    bottleneck = inf
    u = t
    while u != s:
        bottleneck = min(bottleneck, graph[parents[u]][u])
        u = parents[u]
    return bottleneck


def update_flow(graph, s, t, parents, bottleneck):
    v = t
    while v != s:
        u = parents[v]
        graph[u][v] -= bottleneck
        graph[v][u] += bottleneck
        v = parents[v]


def create_residual_graph(graph, colors):
    n = len(graph)
    new_graph = [[0] * (n + 2) for _ in range(n + 2)]

    # Add residual undirected edges
    for u in range(n):
        for v in graph[u]:
            new_graph[u][v] = 1

    # Add directed edges from source to all vertices
    for u in range(n):
        if colors[u] == 1:
            new_graph[u][n + 1] = 1
        else:
            new_graph[n][u] = 1

    return new_graph, n, n + 1


def edmonds_karp(residual_graph, s, t):
    n = len(residual_graph)
    max_flow = 0
    parents = [-1] * n
    visited = [0] * n
    token = 1

    while bfs(residual_graph, s, t, parents, visited, token):
        # Find an augmenting path and its bottleneck value
        bottleneck = get_bottleneck(residual_graph, s, t, parents)
        # Update flow on a path which was found
        update_flow(residual_graph, s, t, parents, bottleneck)
        # Increase a value of the maximum flow
        max_flow += bottleneck
        token += 1

    return max_flow


def maximum_association(graph):
    colors = colorize_vertices(graph)
    # If a graph is not bipartite, return -1
    if not colors:
        return -1
    residual_graph, s, t = create_residual_graph(graph, colors)
    return edmonds_karp(residual_graph, s, t)

# znajdowanie liczby krawędzi i zwracanie listy krawędziw skojarzeniu
def get_association(G, flow, colors, s):
    edges = []
    n = len(G)

    for u in range(n):
        # If a vertex is connected to the fake source vertex
        # and there is no more capacity left in an edge
        if colors[u] == 1 and not flow[n][u]:
            # Look for an edge which is connected to u vertex
            # and also has no more capacity left (there is flow
            # going through this edge)
            for v in G[u]:
                if not flow[u][v]:
                    edges.append((u, v))

    return edges


def maximum_association2(G: 'undirected graph represented by adjacency lists'):
    colors = colorize_vertices(G)
    # If a graph is not bipartite, return -1 and empty edges list
    if not colors: return -1, []
    RG, s, t = create_residual_graph(G, colors)
    count = edmonds_karp(RG, s, t)
    return count, get_association(G, RG, colors, s)
# The Ford-Fulkerson algorithm is a greedy algorithm that computes the maximum flow in a flow network (graph).
from math import inf
from queue import Queue
from copy import deepcopy

def dfs_visit(graph, source, visited, parent):
    visited[source] = True
    for v in range(len(graph)):
        if not visited[v] and graph[source][v] != 0:
            parent[v] = source
            dfs_visit(graph, v, visited, parent)


def dfs(graph, s, t, parent):
    visited = [False] * len(graph)
    dfs_visit(graph, s, visited, parent)
    return visited[t]


def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while dfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


graph = [[0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
         [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(edmonds_karp_algorithm(graph, 0, 9))

# MATRIX

def ford_fulkerson1(G, s, t):
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
        if not increase: break
        max_flow += increase
        token += 1

    return max_flow

# ADJACENCY LIST

def add_back_edges(G):
    n = len(G)
    counts = [0] * n  # Numbers of edges in an initial graph (before modification)

    for u in range(n):
        counts[u] = len(G[u])

    for u in range(n):
        for i in range(counts[u]):
            v = G[u][i][0]
            G[v].append((u, 0))  # Add an edge with no weight

    return counts


def remove_back_edges(G, counts):
    n = len(G)

    for u in range(n):
        while len(G[u]) > counts[u]:
            G[u].pop()


def ford_fulkerson(G, s, t):
    n = len(G)
    flow = [[0] * n for _ in range(n)]
    visited = [0] * n
    token = 1  # Number of iteration to check which vertices have been visited
    max_flow = 0

    counts = add_back_edges(G)

    def dfs(u, bottleneck):
        visited[u] = token

        if u == t:
            return bottleneck

        for v, capacity in G[u]:
            remaining = capacity - flow[u][v]
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

    remove_back_edges(G, counts)

    return max_flow



#UNDIRECTED ADJACENCY LIST

""" Drobne zmiany w poniższej funkcji (to są jedynie zmiany względem powyższego algorytmu) """

# dodajemy funkcję map_graph i reszta jak wyżej

def map_graph(G: 'graph represented by adjacency lists'):
    n = len(G)
    G2 = [[] for _ in range(n)]
    w = n

    for u in range(n):
        for v, weight in G[u]:
            if u < v:
                G2.append([])
                G2[u].append((w, weight))
                G2[w].append((v, weight))
                w += 1
            else:
                G2[u].append((v, weight))

    return G2


# Implementation for directed or undirected graph represented by matrix:


def bfs(G, s, t, parents, visited, token):
    n = len(G)
    q = Queue()
    q.put(s)
    visited[s] = token

    while not q.empty():
        u = q.get()
        for v in range(n):
            if not G[u][v] or visited[v] == token:
                continue
            q.put(v)
            visited[v] = token
            parents[v] = u

    return visited[t] == token


def get_bottleneck(G, s, t, parents):
    bottleneck = inf
    u = t
    while u != s:
        bottleneck = min(bottleneck, G[parents[u]][u])
        u = parents[u]
    return bottleneck


def update_flow(G, s, t, parents, bottleneck):
    v = t
    while v != s:
        u = parents[v]
        G[u][v] -= bottleneck
        G[v][u] += bottleneck
        v = parents[v]


def copy_graph(G):
    n = len(G)
    G2 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            G2[i][j] = G[i][j]
    return G2


def edmonds_karp(G, s, t):
    n = len(G)
    RG = deepcopy(G)  # We won't modify the input graph
    max_flow = 0
    parents = [-1] * n
    visited = [0] * n
    token = 1

    while bfs(RG, s, t, parents, visited, token):
        # Find an augmenting path and its bottleneck value
        bottleneck = get_bottleneck(RG, s, t, parents)
        # Update flow on a path which was found
        update_flow(RG, s, t, parents, bottleneck)
        # Increase a value of the maximum flow
        max_flow += bottleneck
        token += 1

    return max_flow  # , RG


def undirected_weighted_graph_matrix(edges_list) -> list[list[tuple[int, int]]]:
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    matrix = [[0] * n for _ in range(n)]  # 0 means no edge
    for e in E:
        matrix[e[0]][e[1]] = e[2]
        matrix[e[1]][e[0]] = e[2]
    return matrix

E = [(0, 3, 10), (3, 1, 20), (3, 6, 15), (1, 2, 10), (2, 5, 15), (4, 3, 3), (4, 1, 15), (5, 4, 4),
     (5, 8, 10), (7, 5, 7), (7, 4, 10), (6, 7, 10), (9, 0, 10), (9, 1, 5), (9, 2, 10), (6, 10, 15),
     (8, 10, 10)]
# Niech s = 9. a t = 10
s = 9
t = 10

G = undirected_weighted_graph_matrix(E)
print(*G, sep='\n')
print(edmonds_karp(G, s, t))
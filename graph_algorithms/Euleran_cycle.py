# Undirected graph has eulerian cycle if is connected and each of its vertex has even degree.
from collections import deque
"""-----------------DETECTING_EULERIAN_CYCLE-----------------"""


def is_connected(adj_list):

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
    #return all(visited), res if all(visited) else None
    return True, res if len(res) == n else None


def has_eulerian_cycle(graph):
    connectivity_status = is_connected(graph)
    if not connectivity_status:
        return False

    n = len(graph)
    for i in range(n):
        if len(graph[i]) % 2 != 0:
            return False
    return True


def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    M = [[] for _ in range(n)]

    for edges in E:
        M[edges[0]].append(edges[1])
        M[edges[1]].append(edges[0])

    return M
E1 = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (1, 5), (1, 4), (2, 5), (2, 4)]
E2 = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 5), (1, 6), (2, 7), (3, 4)]

G1 = undirected_graph_list(E1, 6)
print(G1)
G2 = undirected_graph_list(E2, 2 ** 3)

print(has_eulerian_cycle(G1))
print(has_eulerian_cycle(G2))

"""-----------------DETECTING_EULERIAN_PATH-----------------"""

# The eulerian path is one that passes through each edge exactly ones.


def dfs(graph, source, result):
    for v in graph[source]:
        graph[source].remove(v)
        graph[v].remove(source)
        dfs(graph, v, result)
    result.append(source)


def eulerian_path(graph):
    connectivity_status = is_connected(graph)
    if not connectivity_status:
        return False
    n = len(graph)
    for i in range(n):
        if len(graph[i]) % 2 != 0:
            return False

    result = []
    dfs(graph, 0, result)
    return result[::-1]


print(eulerian_path(G1))
print(eulerian_path(G2))

"""-----------------DETECTING_EULERIAN_PATH_CYCLE-----------------"""

def is_consistent(graph_adj):
    n = len(graph_adj)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in graph_adj[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)
    return all(visited)


# Checks if a graph has either an euler cycle or an euler path
# Returns:
# 0 - if there is neither euler cycle nor euler path in a graph,
# 1 - if there is euler cycle,
# 2 - if there is euler path.
def is_eulerian(G: 'graph represented using adjacency list'):
    if not is_consistent(G): return 0, -1
    n = len(G)
    odd_count = 0
    begin_vertex = 0
    # Check for each vertex if its degree is even
    for u in range(n):
        if len(G[u]) % 2:
            odd_count += 1
            begin_vertex = u
    if odd_count == 0: return 1, begin_vertex
    if odd_count == 2: return 2, begin_vertex
    return 0, -1


# Generate either an euler cycle or an euler path
def euler(G: 'graph represented using adjacency list'):
    # Check if a graph has an euler cycle or an euler path
    g_type, begin_u = is_eulerian(G)
    if g_type == 0: return [], g_type

    n = len(G)
    result = []
    visited = [[False] * n for _ in range(n)]

    def dfs(u):
        for v in G[u]:
            if not visited[u][v]:
                visited[u][v] = visited[v][u] = True
                dfs(v)
        result.append(u)

    dfs(begin_u)

    return result, g_type
E = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0), (1, 5), (1, 4), (2, 5), (2, 4)]

G = undirected_graph_list(E, 6)
result, g_type = euler(G)
print('Cycle:' if g_type == 1 else 'Path:' if g_type == 2 else 'Nothing', result, end='\n\n')
print(*(' '.join(map(str, row)) for row in G), sep='\n')



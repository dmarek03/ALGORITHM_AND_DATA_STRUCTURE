def directed_graph_list(E: 'array of edges', n: 'number of vertices'):
    G = [[] for _ in range(n)]
    for edge in E:
        G[edge[0]].append(edge[1])
    return G


def get_process_times(G: 'graph represented using adjacency lists'):
    n = len(G)
    times = [0] * n
    visited = [False] * n
    time = 0

    def dfs(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs(v)
        nonlocal time
        time += 1
        times[u] = time

    for u in range(n):
        if not visited[u]:
            dfs(u)

    return times


def get_transposed_graph(G: 'graph represented using adjacency lists'):
    n = len(G)
    G2 = [[] for _ in range(n)]

    for u in range(n):
        for v in G[u]:
            G2[v].append([u])

    return G2


def get_vertices_order(times):
    n = len(times)
    order = [-1] * n
    for i in range(n):
        order[n - times[i]] = i
    return order


def find_coherent_components(G: 'graph represented using adjacency lists'):
    n = len(G)
    # Get processing time of each vertex
    times = get_process_times(G)
    # Create a transposed graph
    G = get_transposed_graph(G)
    # Get order of vertices in which DFS will be started from such vertices
    order = get_vertices_order(times)
    # Create an array in which a result will be stored (each number will refer
    # to the other coherent component of a graph)
    result = [-1] * n  # This array will also be used to check if a vertex was visited
    token = 0

    def dfs(u):
        result[u] = token
        for v in G[u]:
            if result[v] < 0:
                dfs(v)

    # Start dfs from vertices of the highest processing time
    for i in range(n):
        u = order[i]
        if result[u] < 0:
            dfs(u)
            token += 1

    return result


from string import ascii_lowercase

E = list(map(lambda p: tuple(map(lambda u: ord(u) - ord('a'), p)),
    ['ab', 'ae', 'bc', 'bd', 'ca', 'ch', 'de', 'dg', 'ef',
     'fd', 'gf', 'hj', 'jk', 'ki', 'ih', 'ig', 'kf']
))

G = directed_graph_list(E, 11)
print(*G, sep='\n')

print(*zip(ascii_lowercase, get_process_times(G)))
print(get_transposed_graph(G))
print(find_coherent_components(G))
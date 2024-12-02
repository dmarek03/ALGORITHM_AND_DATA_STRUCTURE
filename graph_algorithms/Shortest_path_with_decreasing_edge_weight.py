from queue import PriorityQueue
from math import inf


def dijkstra_decreasing_edges_path(G,s, t):
    if s == t:
        return 0

    n = len(G)
    W = [[inf] * n for _ in range(n)]
    P = [[None] * n for _ in range(n)]
    pq = PriorityQueue()

    for v, weight in G[s]:
        pq.put((weight, weight, s, v, None))

    last_u = None

    while not pq.empty():
        min_w, prev_weight, u, v, parent = pq.get()
        if min_w < W[u][v]:
            W[u][v] = min_w
            P[u][v] = parent
            if v == t:
                last_u = u
                break
            for w, weight in G[v]:
                if weight < prev_weight and W[v][w] == inf:
                    pq.put((min_w + weight, weight, v, w, u))

    print(*W, sep='\n')
    print("---------------------------")

    return (get_path(P, last_u, t), W[last_u][t]) if last_u is not None else ([], 0)


def get_path(P: 'array of edges parents', u: 'last edge first vertex', t: 'last edge second vertex'):
    path = [t]

    while u is not None:
        path.append(u)
        u, t = P[u][t], u

    return path[::-1]


def undirected_weighted_graph_list(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[] for _ in range(n)]
    for e in E:
        G[e[0]].append([e[1], e[2]])
        G[e[1]].append([e[0], e[2]])
    return G





E = [(0, 1, 1), (1, 2, 4), (2, 3, 3), (0, 5, 40), (5, 6, 38), (0, 7, 5), (6, 7, 8), (7, 1, 6),
     (7, 2, 16), (6, 2, 23), (6, 8, 35), (5, 4, 30), (8, 4, 20), (8, 3, 15), (4, 3, 80)]

G = undirected_weighted_graph_list(E)
print(*G, sep='\n')
print("-----------------------------")
print(dijkstra_decreasing_edges_path(G, 0, 3))
# print(dijkstra_decreasing_edges_path(G, 1, 3))
# print(dijkstra_decreasing_edges_path(G, 3, 1))
# print(dijkstra_decreasing_edges_path(G, 2, 0))
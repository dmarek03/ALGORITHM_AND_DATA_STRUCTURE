# DJIKSTRA ALGORITHM - the shortest path in weigthed graph

from queue import PriorityQueue
from math import inf

# COMPLEXITY : 0(E*logV)

"----------------------FIRST_SOLUTION_ADJACENCY_LIST----------------------"

def relax(u, v,weight,  distances, parent):
    if distances[v] > distances[u] + weight:
        distances[v] = distances[u] + weight
        parent[v] = u
        return True
    return False


def dijkstra_algorithm(graph, source):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0, source))
    parent = [None] * n
    distances = [inf] * n
    visited = [False] * n
    distances[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v, weight in graph[u]:
            if not visited[v] and relax(u, v,weight,  distances, parent):
                queue.put((dist + weight, v))
        visited[u] = True
    return parent, distances

graph = [[(1, 1), (2, 12)],
         [(0, 1), (2, 7), (3, 5)],
         [(0, 12), (1, 2), (3, 6), (4, 2)],
         [(1, 5), (2, 6), (4, 4), (5, 100)],
         [(2, 2), (3, 4), (5, 9)],
         [(3, 100), (4, 9)]]

parent, distances = dijkstra_algorithm(graph, 0)
print(f'{distances=}')
i = len(parent) - 1
while parent[i] is not None:
    print(i, distances[i])
    i -= 1


"----------------------SECOND_SOLUTION_ADJACENCY_LIST----------------------"


def better_dijkstra(G: 'graph represented by adjacency lists', s: 'source'):
    n = len(G)
    weights = [inf] * n
    # This variable is a counter of vertices remaining which we still
    # have to find the shortest paths to
    to_relax = n
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty() and to_relax:
        min_w, u = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            to_relax -= 1
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v))

    return weights


graph = [[(1, 1), (2, 12)],
         [(0, 1), (2, 7), (3, 5)],
         [(0, 12), (1, 7), (3, 6), (4, 2)],
         [(1, 5), (2, 6), (4, 4), (5, 100)],
         [(2, 2), (3, 4), (5, 9)],
         [(3, 100), (4, 9)]]
print('-----------------------')
print(better_dijkstra(graph, 3))
print('-----------------------')

# Jeśli chcemy wzynaczyć odległość z każdego wierzchołka do pewnego celu, to jako drugi argument podajemy nasz cel !!!


"----------------------MATRIX----------------------"

# FIRST SOLUTION - WITHOUT QUEUE


def dijkstra_matrix(matrix, source):
    n = len(matrix)
    # Store information about vertices which we already found the shortest path to
    processed = [False] * n
    parents = [None] * n
    weights = [inf] * n
    weights[source] = 0

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        min_w = inf
        min_u = None
        for u in range(n):
            if not processed[u] and weights[u] < min_w:
                min_w = weights[u]
                min_u = u
        # Check if a vertex was found (if not, all vertices must have
        # been processed before)
        if min_u is None: break
        # Mark the current vertex as processed
        u = min_u
        processed[u] = True
        # Iterate over the vertice's neighbours and update weights of the paths
        for v in range(n):
            # Skip if no edge (-1 means not edge) or a vertex v was processed
            if matrix[u][v] == -1 or processed[v]: continue
            # Update the weight of a path to the vertex v if found a better one
            if weights[u] + matrix[u][v] < weights[v]:
                weights[v] = weights[u] + matrix[u][v]
                parents[v] = u

    return parents, weights


# SECOND SOLUTION

def relax(graph, u, v, distance, parent):
    if distance[v] > distance[u] + graph[u][v]:
        distance[v] = distance[u] + graph[u][v]
        parent[v] = u
        return True
    return False


def dijkstra_algorithm(graph, source):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0, source))
    visited = [False] * n
    parent = [None] * n
    distances = [inf] * n
    distances[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        for v in range(n):
            if graph[u][v] > 0 and not visited[v]:
                if relax(graph, u, v, distances, parent):
                    queue.put((dist + graph[u][v], v))
        visited[u] = True
    return parent, distances


graph = [[0, 1, 5, 0, 0],
         [1, 0, 2, 8, 7],
         [5, 2, 0, 3, 0],
         [0, 8, 3, 0, 1],
         [0, 7, 0, 1, 0]]

parent, distance = dijkstra_algorithm(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i])
    i -= 1


"""----------------------THE_SHORTEST_PATH_BETWEEN_TWO_VERTEX----------------------"""

#1 SOLUTION
def relax(u, v, distance, parent):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        parent[v[0]] = u
        return True
    return False


def dijkstra(graph, source, end):
    min_dist = inf
    queue = PriorityQueue()
    queue.put((0, source))
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[source] = 0
    while not queue.empty():
        dist, u = queue.get()
        if u == end:
            min_dist = dist
            break
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v, distance, parent):
                queue.put((dist + v[1], v[0]))
        visited[u] = True
    return parent, min_dist



def get_shortest_path(G, s, t):
    parents, dist = dijkstra(G, t, s)
    path = []

    while s is not None:
        path.append(s)
        s = parents[s]

    return path, dist

graph1 = [
    [(1, 1), (2, 12)],
    [(0, 1), (2, 7), (3, 5)],
    [(0, 12), (1, 7), (3, 6), (4, 2)],
    [(1, 5), (2, 6), (4, 4), (5, 100)],
    [(2, 2), (3, 4), (5, 9)],
    [(3, 100), (4, 9)]]

path, dist = get_shortest_path(graph1, 2, 5)

print(path)
print(dist)


#2 better solution




def better_dijkstra2(G, s, t):
    n = len(G)
    min_distance = inf
    weights = [inf] * n
    parents = [None] * n
    pq = PriorityQueue()
    pq.put((0, s, None))

    while not pq.empty():
        min_w, u, parent = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            parents[u] = parent
            # Break a loop if we found a shortest path to the specified
            # target
            if u == t:
                min_distance = min_w
                break
            # Add all the neighbours of the u vertex to the priority queue
            for v, weight in G[u]:
                if weights[v] == inf:
                    pq.put((weights[u] + weight, v, u))

    return parents, min_w


"""Dodatkowo: Wyznaczanie najkrótszej scieżki między parą wierzchołków
(w postaci listy kolejno odwiedzanych wierzchołków - tylko dla grafów bez krawędzi wielokrotnych)
"""


def get_shortest_path(G, s, t):
    parents, _ = dijkstra(G, t, s)
    path = []

    while s is not None:
        path.append(s)
        s = parents[s]

    return path





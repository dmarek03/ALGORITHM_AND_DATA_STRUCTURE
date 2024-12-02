# Prim's algorithm for finding MST - minimum spanning tree .

#1 ADJACENCY LIST

# COMPLEXITY 0(E*logV)
from queue import PriorityQueue
from math import inf


def prims(G:list[list[tuple[int, int]]]):
    n = len(G)
    parents = [-1] * n
    weights = [inf] * n
    processed = [False] * n
    pq = PriorityQueue()
    pq.put((0, 0))

    while not pq.empty():
        u_weight, u = pq.get()
        # Skip a vertex if it was processed before
        # if processed[u]:
        #     continue
        # If we remove the vertex from a priority queue this must be a vertex
        # with the lowest weight in a queue so we will mark this vertex as
        # processed because all the future occurrences of this vertex
        # in a priority queue must be skipped
        processed[u] = True
        # Loop over all the u vertex's neighbours and update parents of such
        # vertices which are not processed and their current weight is greater
        # than the u_weight
        for v, e_weight in G[u]:
            if not processed[v] and e_weight < weights[v]:
                parents[v] = u
                weights[v] = e_weight
                pq.put((e_weight, v))

    return parents, weights


def get_MST(mst: list[list[tuple[int, int]]]) -> list[list[tuple[int, int]]]:
    parents, weights = prims(mst)
    n = len(mst)
    mst = [[] for _ in range(n)]
    for u in range(n):
        if parents[u] >= 0:
            mst[parents[u]].append((u, weights[u]))
            mst[u].append((parents[u], weights[u]))
    return mst


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


G = undirected_weighted_graph_list([(0, 1, 1), (1, 2, 5), (2, 3, 3000), (0, 5, 12), (1, 5, 7),

                                    (5, 2, 6), (5, 4, 8), (4, 2, 4), (4, 3, 9)])
print(*G, sep='\n')
print('----------------')
print(prims(G)[0])
print(prims(G)[1])

print("------------")
print(*get_MST(G), sep='\n')


#2 MATRIX
# COMPLEXITY 0(V^2)

class Node:


    def __init__(self, idx=None):
        self.idx = idx
        self.next = None


def vertices_to_process_ll(n):
    head = Node()
    tail = head
    for i in range(n):
        tail.next = Node(i)
        tail = tail.next
    return head


def get_min_weight_vertex(head, weights, n):
    if not head.next: return None  # If no more vertices are remaining

    # Find a vertex of the lowest weight
    min_prev = head
    prev = head.next
    while prev.next:
        if weights[prev.next.idx] < weights[min_prev.next.idx]:
            min_prev = prev
        prev = prev.next

    # Remove a vertex found
    u = min_prev.next.idx
    min_prev.next = min_prev.next.next

    return u


def prims(G: 'graph represented by adjacency matrix'):
    n = len(G)
    inf = float('inf')
    # Store information about vertices which haven't been processed yet
    to_process = vertices_to_process_ll(n)
    parents = [-1] * n
    weights = [inf] * n
    processed = [False] * n
    weights[0] = 0

    # Loop till there are some vertices which haven't been processed yet
    while True:
        # Find a vertex of the minimum total weight path
        u = get_min_weight_vertex(to_process, weights, n)
        # Check if a vertex was found (if not, all vertices must have
        # been processed before)
        if u is None: break
        processed[u] = True
        # Iterate over the vertice's neighbours and update weights of the paths
        for v in range(n):
            # Skip if no edge (inf means not edge) or a vertex v was processed
            if G[u][v] == inf or processed[v]: continue
            # Update a vertice's parent if we found an edge of the lower weight
            if G[u][v] < weights[v]:
                weights[v] = G[u][v]
                parents[v] = u

    return parents, weights


def get_MST(G: 'graph represented by adjacency matrix') -> 'minimum spanning tree graph':
    parents, weights = prims(G)
    n = len(G)
    G = [[float('inf')] * n for _ in range(n)]  # inf means no edge
    for u in range(n):
        if parents[u] >= 0:
            G[parents[u]][u] = weights[u]
            G[u][parents[u]] = weights[u]
    return G
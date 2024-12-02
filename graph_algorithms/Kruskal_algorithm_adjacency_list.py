# Kruskal's algorithm for finding MST - minimum spanning tree on adjacency list.
# Complexity -> O(ElogV) = O(V^2logV)
class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_set(v):
    return Node(v)


def convert_to_edges(graph):
    edges = []
    for u in range(len(graph)):
        for v, w in graph[u]:
            if u > v:
                edges.append([u, v, w])
    return edges


def kruskal_algorithm(graph):
    edges = convert_to_edges(graph)
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []
    for i in range(len(graph)):
        V.append(make_set(i))
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
    return MST

# Ze sprawdzaniem czy da się utworzyć mst
def kruskal_algorithm1(edges, n):
    MST = []
    V = []
    for i in range(n):
        V.append(make_set(i))
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        w = edges[i][2]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
            max_edge = (u, v, w)
    root = find(V[0])
    for i in range(1, len(V)):
        if find(V[i]) != root:
            return None
    return MST



graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]
print(kruskal_algorithm(graph))
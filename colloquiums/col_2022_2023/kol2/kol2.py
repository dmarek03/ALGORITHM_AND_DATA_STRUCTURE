# DOMINIK MAREK

# Kluczem do roziwązania zadania jest skorzystanie algorytmu Kruskal, który znajduję minimalne drzewo rozpinające w
# grafie nieskierowanym, który modyfikujemy aby spełniał warunki zadania. Modyfikacja polega na sprawdzeniu dla danej
# krawędzi czy jej waga zawiera się pomiędzy minimalna i maksymalną wagą krawdzi znajdujących się w naszym garfie wejściowym
# ,jeśli tak to powiększamy nasze drzewo rozpinające o tą krawędź. Na koniec po wywołaniu znalezieniu MST
# za pomocą algorytmu Kruskala , sumujemy wagi krawędzi w naszym MST, gdyż ich suma jest rozwiązaniem naszego zadania.
# Złożoność obliczeniowa prezentowanego algortymu wynosi : O(VElogE).


from kol2testy import runtests
from queue import Queue
#Graph is converted to list of edges (E), then Kruskal algorithm  looks for beautiful tree (n-1 edges), if algorithm
#skips any edges work is being interrupted, cuz it needs to be next n-1 edges


def Kruskal(G, n):
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def find(x):
        if parent[x] != x:
            x = find(parent[x])
        return x

    def union(x, y):
        x = find(x)
        y = find(y)

        if x == y:
            return
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    i = 0
    e = 0
    total_weight = 0
    while e < n - 1:
        u, v, w = G[i]
        i += 1
        if find(u) != find(v):
            union(u, v)
            e += 1
            total_weight += w

        else:
            # skipping edge means stopping algorythm
            return -1
        if i == len(G):
            return -1,

    return total_weight


def convert_to_edges(graph):
    edges = []
    for u in range(len(graph)):
        for v, w in graph[u]:
            if u > v:
                edges.append([u, v, w])
    return edges


def convert_to_directed_unweighted_adj(edges_list: list[list[tuple[int, int, int]]], n) -> list[list[int]]:
    adj = [[] for _ in range(n)]

    for u, v, w in edges_list:
        if u > v:
            adj[v].append(u)
            adj[u].append(v)
    return adj


def dfs_adj(graph, node, visited, num):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs_adj(graph, n, visited, num)
    return len(visited) == num


def get_sum(mst: list[list[tuple[int, int, int]]]) -> int:
    return sum(edge[2] for edge in mst)




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


def kruskal_algorithm(edges, n):
    V = [make_set(i) for i in range(n)]
    MST = []
    weight_sum = 0
    for u, v, w in edges:
        if find(V[u]) != find(V[v]):
            MST.append((u, v, w))
            weight_sum += w
            union(V[u], V[v])

        else:
            return -1
    if len(MST) == n - 1:
        return weight_sum




def beautree(G):
    n = len(G)
    E = convert_to_edges(G)
    E.sort(key=lambda x: x[2])


    # while len(E) > n-1:
    #     current_edges = E[:n-1]
    #
    #     weight = kruskal_algorithm(current_edges, n)
    #     if weight != -1:
    #         return weight
    #
    #     del [E[0]]


    # while len(E) > n - 1:
    #     total_weight = Kruskal(E, n)
    #     if total_weight != -1:
    #         return total_weight
    #     del [E[0]]
    while len(E) > n - 1:
        graph = convert_to_directed_unweighted_adj(E[:n-1], n)
        is_connected = dfs_adj(graph, 0, [], n)
        if is_connected:
            return get_sum(E[:n-1])
        del [E[0]]

    return None




runtests(beautree, all_tests=True)
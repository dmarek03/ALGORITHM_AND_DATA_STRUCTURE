from egzP3btesty import runtests 
# O(nlogm), gdzie m to liczba miast, a n to liczba połączeń
# Korzystając z algorytmu Kruskala znjadujemy maksymalne drzewo rozpinające a następnie znajdujemy krawędź o największej
# wadze, która nie należy do tego MST. Dzięki temu otrzymuje połącznia z największą ilością lotów , gdzie wszytskie poza
# jednym nie są redunantne.Finalnie zwracamy sumę krawędzi w grafie wyjściowym pomniejszoną o wagę MST  i wagę
# najcięższej krawędzi z poza MST.

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
    edges.sort(key=lambda x: -x[2])
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
    return MST, edges


def get_weight(list_edges) -> int:
    weight = 0
    for edge in list_edges:
        weight += edge[2]
    return weight


def lufthansa( G ):

    mst, edges = kruskal_algorithm(G)

    total_weight = get_weight(edges)
    mst_weight = get_weight(mst)
    j = 0
    # We have to find first edge that does not belong to mst to add its weight to mst_weight
    for i in range(len(mst)):
        if mst[i]== edges[i]:
            j += 1
        else:
            break

    mst_weight += edges[j][2]
    #To find the solution(number of flights to remove) we subtract number of needed flights from total number of filghts
    return total_weight-mst_weight

runtests ( lufthansa, all_tests='a')
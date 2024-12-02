"""
W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby
możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo jest płaski położenie
każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami liczona w kilometrach wyraża się
wzorem len = sqrt((x1 − x2)^2 + (y1 − y2)^2)
Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie
i jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej
w km).
Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza minimalną liczbę dni dzielącą
otwarcie pierwszej i ostatniej autostrady.
Przykład Dla tablicy A =[(10,10),(15,25),(20,20),(30,40)] wynikiem jest 7 (Autostrady
pomiędzy miastami 0-1, 0-2, 1-3).

"""

# Początkowo tworzę listę krawędzi  wszytskich możliwych połączeń między miastami z tablicy A,
# gdzie wagą danej krawędzi jest od odległość jedno miasta od drugiego wyliczona według podanego wzoru.Następnie dopóki
# z danej listy krawędzi mogę utworzyć MST, obliczam różnicę pomiędzy ostatnią i pierwszą krawędzią z MST i sprawdzam,
# czy otrzymana róźnica jest mniejsza niż obecna wartość min_time, jeśli tak to aktualizuje wartość tej zmiennej.
# Następnie usuwam pierwszą krawędz z listy krawędzi i wykonuje powyższe kroki.
# Finalna wartość zmiennej min_time jest rozwiązaniem zadania.
# Complexity -> O(E^2logE) = O(2V^4logV)
from math import ceil, inf
from highway_testy import runtests


def get_dist(city1, city2):
    return ceil(((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2)**0.5)


# Kruskal's algorithm for finding MST - minimum spanning tree on adjacency list.

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


def kruskal_algorithm(edges, n):
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

    root = find(V[0])
    for i in range(1, len(V)):
        if find(V[i]) != root:
            return
    print(*MST, sep='\n')
    return MST[-1][2]-MST[0][2]


def highway(array):
    n = len(array)

    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i, j, get_dist(array[i], array[j])))
    edges.sort(key=lambda x: x[2])
    min_time = inf
    while (curr_time := kruskal_algorithm(edges, n)) is not None:
        #curr_time = kruskal_algorithm(edges, n)
        print(f'{curr_time=}')
        # Uważaj na not curr_time bo jak będzie równe zero to kod spadnie z rowerka XD !!!!
        if curr_time is None:
            break
        if curr_time < min_time:
            min_time = curr_time
        del edges[0]

    return min_time


runtests(highway)
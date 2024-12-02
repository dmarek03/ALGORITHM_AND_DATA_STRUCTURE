# DOMINIK MAREK
# Aby znaleźć najkrótszą śćieżkę po między zadanymi wierzchołkami, przeszukuję graf G stosując algortym BFS, który przy
# wywołaniu z paramterem collect_shortest=True ,również zwróci listę kolejnych wierzchołków w najkrótszej ścieżce
# od s do t . Następnie w pętli sprawdzam czy usunięcie kolejnych krawędzi z znalezionej ścieżki, spowoduje jej
# wydłużenie, jeśli tak to zwracam usuniętą krawędź w przeciwnym przypadku None.
# Złożoność obliczeniowa zaproponwanego algrytmu to O((V+E)^2), gdzie V- liczba wierzchołków, E-liczba krawędzi grafu G.


from zad4testy import runtests

from math import inf
from collections import deque


def collect(vertices_from: list[int | None], u: int, distance: int) -> list[int]:

    shortest = [0] * (distance+1)

    for i in range(distance, -1, -1):

        shortest[i] = u

        u = vertices_from[u]

    return shortest


def remove_edge(graph: list[list[int]], vertex1: int, vertex2: int):
    graph[vertex1].remove(vertex2)
    graph[vertex2].remove(vertex1)


def add_edge(graph: list[list[int]], vertex1: int, vertex2: int):
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)


def BFS(graph: list[list[int]], vertex1: int, vertex2: int, collect_shortest=False) -> int | float | tuple[int | float, list[int]]:
    d = deque()
    n = len(graph)
    visited = [False] * n
    vertices_from = [None] * n
    d.append((0, vertex1))
    visited[vertex1] = True
    while d:
        (distance, u) = d.popleft()
        if u == vertex2:
            return (distance, collect(vertices_from, u, distance)) if collect_shortest else distance
        for v in graph[u]:
            if not visited[v]:
                d.append((distance+1, v))
                vertices_from[v] = u
                visited[v] = True

    return inf


def longer(G: list[list[int]], s: int, t: int) -> None | list[int]:
    # tu prosze wpisac wlasna implementacje

    distance, shortest = BFS(G,s, t, True)
    if s not in shortest:
        return None
    n = len(shortest)
    edge = None
    for i in range(0, n-1):
        v1, v2 = shortest[i], shortest[i+1]
        remove_edge(G, v1, v2)
        distance2 = BFS(G, s, t)
        add_edge(G, v1, v2)
        if distance2 > distance:
            edge = [v1, v2]
            break

    return edge

#print(longer(graph, 0, 5))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True)


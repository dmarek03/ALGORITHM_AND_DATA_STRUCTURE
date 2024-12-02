""" O(V + E) - 3 razy DFS """
"""
Każdy nieskierowany, spójny i acyckliczny graf G = (V, E) możemy traktować jako drzewo. Korzeniem tego drzewa może być 
dowolny wierzchołek v ∈ V . Napisz funkcję best root(L), która przyjmuje nieskierowany, spójny i acyckliczny graf G 
(reprezentowany w postaci listy sąsiedztwa) i wybiera taki jego wierzchołek, by wysokość zakorzenionego w tym 
wierzchołku drzewa była możliwie najmniejsza. Jeśli kilka wierzchołków spełnia warunki zadania, funkcja może zwrócić 
dowolny z nich. Wysokość drzewa definiujemy jako liczbę krawędzi od korzenia do najdalszego liścia. Uzasadnij
poprawność zaproponowanego algorytmu i oszacuj jego złożoność obliczeniową.
Funkcja best root(L) powinna zwrócić numer wierzchołka wybranego jako korzeń. Wierzchołki
numerujemy od 0. Argumentem best root(L) jest lista postaci:
L = [l0,l1, . . . ,ln−1],
gdzie li to lista zawierająca numery wierzchołków będących sąsiadami i−tego wierzchołka. Można
przyjąć (bez weryfikacji), że lista opisuje graf spełniający warunki zadania. W szczególności, graf
jest spójny, acykliczny, oraz jeśli a ∈ lb to b ∈ la (graf jest nieskierowany). Nagłówek funkcji powinien
mieć postać:
"""
# Wykorzystując algorytm dfs znajdujemy odległości od pierwszego wierzchołka do pozostałych a następnie szukamy
# wierzchołka do którego odległość jest największa. Następnie znowu wyznaczamy odległośći od znalezionego wierzchołka
# do wszytskich innych i znów znajdujemy najbardziej oddalony wierzchołek i dla niego również wyznaczamy dystans do
# innych wierzchołków. Tym samym mamy odległośći od wierzchołka będącego końcem średnicy wyjściowego drzewa oraz
# wierzchołka będącego końcem średnicy drzewa początkowym wierzchołku wspomnainaym wcześniej.Następnie dla szukamy
# takiego wierzchołka dla którego maksimum ze znalezionych odległośći będzie najmiejsze, więc będzie to wierzchołek,
# dla którego wysokość drzewa będzie najmniejsza.
# Complexity -> O(V + E)

from best_root_testy import runtests
from math import inf
from collections import deque


def is_connected(graph):
    n = len(graph)
    visited = [False] * n

    def dfs(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    dfs(0)

    return all(visited)


def max_val_idx(array):
    max_i = 0
    for i in range(1, len(array)):
        if array[i] > array[max_i]:
            max_i = i
    return max_i


def diam_dist(graph):
    n = len(graph)
    # Find the first diameter end vertex
    dist = [inf] * n
    visited = [0] * n
    token = 1

    def dfs(u):
        visited[u] = token
        for v in graph[u]:
            if visited[v] != token:
                dist[v] = dist[u] + 1
                dfs(v)

    # Find the first diameter end vertex
    dist[0] = 0
    dfs(0)
    diam_u = max_val_idx(dist)
    print(f'{dist=}')
    print(f'{diam_u=}')

    # Find distances of all vertices from the first diameter end vertex
    # and the second diameter end vertex
    token += 1
    dist[diam_u] = 0
    dfs(diam_u)
    diam_v = max_val_idx(dist)
    print(f'{dist=}')
    print(f'{diam_v=}')
    dist1 = dist[:]  # Copy all distances from the first diameter vertex
    print(f'{dist1=}')

    # Find all distances from the second diameter end vertex
    token += 1
    dist[diam_v] = 0
    dfs(diam_v)
    print(f'{dist=}')
    dist2 = dist[:]  # Copy all distances from the second diameter vertex
    print(f'{dist2=}')

    return dist1, dist2


def diam_vertex(graph):
    n = len(graph)
    # Find the first diameter end vertex
    dist = [inf] * n
    visited = [0] * n
    token = 1

    def dfs(u):
        visited[u] = token
        for v in graph[u]:
            if visited[v] != token:
                dist[v] = dist[u] + 1
                dfs(v)

    # Find the first diameter end vertex
    dist[0] = 0
    dfs(0)
    diam_u = max_val_idx(dist)
    # Find distances of all vertices from the first diameter end vertex
    # and the second diameter end vertex
    token += 1
    dist[diam_u] = 0
    dfs(diam_u)
    diam_v = max_val_idx(dist)

    return diam_u, diam_v


def shortest_path_between(graph, vertex1: int, vertex2: int):
    if vertex1 == vertex2:
        return [vertex1]
    dist = 0
    num_vertices = len(graph)
    visited = [False] * num_vertices
    dequeue = deque()
    # Adding the starting vertex to deque
    dequeue.append((vertex1, [vertex1], dist))
    # Marking the starting vertex as visited
    visited[vertex1] = True

    while dequeue:
        vertex, path, dist = dequeue.popleft()
        # if lately popped vertex is our destination we return path
        if vertex == vertex2:
            return path

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dequeue.append((neighbor, path + [neighbor], dist+1))
                visited[neighbor] = True

    return None


def best_root(adj_list):

    # This case will occur if a graph is not connected
    # (then the max distance will be infinity beacause for every vertex
    # there is at least one verex in another component and each vertex
    # then has its max distance equal to infinity)
    if not is_connected(adj_list):
        return -1

    n = len(adj_list)
    dist1, dist2 = diam_dist(adj_list)
    # Find a vertex of the lowest max dist
    best_u = None
    min_dist = inf
    for u in range(n):
        max_dist = max(dist1[u], dist2[u])
        if max_dist < min_dist:
            min_dist = max_dist
            best_u = u

    return best_u

# Znajdujemy środkowy wierzchołek na przekątnej drzewa
def best_root1(adj_list):

    # This case will occur if a graph is not connected
    # (then the max distance will be infinity beacause for every vertex
    # there is at least one verex in another component and each vertex
    # then has its max distance equal to infinity)
    if not is_connected(adj_list):
        return -1
    diam_u, diam_v = diam_vertex(adj_list)
    diam_path = shortest_path_between(adj_list, diam_u, diam_v)
    return diam_path[len(diam_path)//2]


def best_root2(L):
    n = len(L)
    min_height = inf  # Inicjalizujemy minimalną wysokość jako nieskończoność
    best_root = -1  # Inicjalizujemy najlepszy korzeń jako -1
    height = inf
    # Przeszukujemy graf zaczynając od każdego wierzchołka jako korzenia
    for root in range(n):
        visited = [False] * n
        queue = deque([(root, 0)])  # Kolejka BFS, każdy element to para (wierzchołek, długość ścieżki)

        while queue:
            vertex, height = queue.popleft()
            visited[vertex] = True
            if height > min_height:
                break  # Jeśli długość ścieżki jest większa niż aktualne minimum, przerywamy

            for neighbor in L[vertex]:
                if not visited[neighbor]:
                    queue.append((neighbor, height + 1))

        # Jeśli znaleźliśmy korzeń o mniejszej wysokości, aktualizujemy najlepszy korzeń i minimalną wysokość
        if height < min_height:
            min_height = height
            best_root = root

    return best_root


runtests(best_root1)
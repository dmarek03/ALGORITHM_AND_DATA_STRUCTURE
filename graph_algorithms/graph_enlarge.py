"""
Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź).
Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
poprawność i oszacować złożoność obliczeniową.
Algorytm należy zaimplementować jako funkcję:
def enlarge(G, s, t):
...
która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
nie było ścieżki z s do t to funkcja powinna zwrócić None.
Przykład. Dla argumentów:
G = [ [1, 2],
[0, 2],
[0, 1] ]
s = 0
t = 2
wynikiem jest np. krotka: (0, 2)
"""

# DOMINIK MAREK
# Aby znaleźć najkrótszą śćieżkę po między zadanymi wierzchołkami, przeszukuję graf G stosując algortym BFS, który przy
# wywołaniu z paramterem collect_shortest=True ,również zwróci listę kolejnych wierzchołków w najkrótszej ścieżce
# od s do t . Następnie w pętli sprawdzam czy usunięcie kolejnych krawędzi z znalezionej ścieżki, spowoduje jej
# wydłużenie, jeśli tak to zwracam usuniętą krawędź w przeciwnym przypadku None.
# Złożoność obliczeniowa zaproponwanego algrytmu to O((V+E)^2), gdzie V- liczba wierzchołków, G-liczba krawędzi grafu G.


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
            return path, dist

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dequeue.append((neighbor, path + [neighbor], dist+1))
                visited[neighbor] = True

    return None


def longer(G: list[list[int]], s: int, t: int) -> None | list[int]:
    # tu prosze wpisac wlasna implementacje

    # distance, shortest = BFS(G,s, t, True)
    shortest, distance= shortest_path_between(G, s, t)
    if s not in shortest:
        return None
    n = len(shortest)
    edge = None
    for i in range(0, n-1):
        v1, v2 = shortest[i], shortest[i+1]
        remove_edge(G, v1, v2)
        distance2 = shortest_path_between(G,s, t)[1]
        add_edge(G, v1, v2)
        if distance2 > distance:
            edge = [v1, v2]
            break

    return edge



G = [ [1, 2],
[0, 2],
[0, 1] ]
print(longer(G, 0, 2))
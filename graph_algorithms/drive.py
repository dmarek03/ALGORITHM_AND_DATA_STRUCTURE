"""
[2pkt.] Zadanie 1.
Szablon rozwiązania: zad1_nieparzysty_palindrom.py
Dana jest tablica dwuwymiarowa G, przedstawiająca macierz sąsiedztwa skierowanego grafu ważonego, który odpowiada mapie
drogowej (wagi przedstawiają odległości, liczba -1 oznacza brak krawędzi). W niektórych wierzchołkach są stacje paliw,
podana jest ich lista P. Pełnego baku wystarczy na przejechanie odległości d. Wjeżdżając na stację samochód zawsze jest
tankowany do pełna. Proszę zaimplemntować funkcję jak dojade(G, P, d, a, b), która szuka najkrótszej możliwej trasy od
wierzchołka a do wierzchołka b, jeśli taka istnieje, i zwraca listę kolejnych odwiedzanych na trasie wierzchołków
(zakładamy, że w a też jest stacja paliw; samochód może przejechać najwyżej odległość d bez tankowania).
Zaproponowana funkcja powinna być możliwe jak najszybsza. Uzasadnij jej poprawność i oszacuj
złożoność obliczeniową.
Przykład Dla tablic
G =
[[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]
P = [0,1,3]
funkcja jak dojade(G, P, 5, 0, 2) powinna zwrócić [0,3,2]. Dla tych samych tablic funkcja
jak dojade(G, P, 6, 0, 2) powinna zwrócić [0,1,2], natomiast jak dojade(G, P, 3, 0, 2)
powinna zwrócić None.
"""
from queue import PriorityQueue
from math import inf
from zad1testy import runtests

#
# def relax(u, v, w, distance, parent):
#     if distance[v] > distance[u] + w:
#         distance[v] = distance[u] + w
#         parent[v] = u
#         return True
#     return False
#
#
# def matrix_to_list(matrix: list[list[int]]):
#     n = len(matrix)
#     adjacency_list = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if matrix[i][j] > 0:
#                 adjacency_list[i].append([j, matrix[i][j]])
#     return adjacency_list
#
#
# def dijkstra_algorithm(graph, gas_station, fuel,  source, end):
#     new_graph = matrix_to_list(graph)
#     n = len(new_graph)
#     fuel_status = fuel
#     is_gas_station = [False]*n
#     for s in gas_station:
#         is_gas_station[s] = True
#
#     min_dist = inf
#     queue = PriorityQueue()
#     queue.put((0, source))
#     parent = [None] * n
#     distance = [inf] * n
#     visited = [False] * n
#     distance[source] = 0
#     while not queue.empty():
#         dist, u = queue.get()
#         if is_gas_station[u]:
#             fuel_status = fuel
#         if u == end and fuel_status >= 0:
#             min_dist = dist
#             break
#         for v, w in new_graph[u]:
#             if is_gas_station[v]:
#                 fuel_status = fuel
#             if not visited[v] and fuel_status >= w and relax(u, v, w, distance, parent):
#                 queue.put((dist + w, v))
#                 fuel_status -= w
#         visited[u] = True
#     return parent, min_dist
#
#
# def jak_dojade(graph, gas_station, fuel, s, t):
#     parents, dist = dijkstra_algorithm(graph, gas_station, fuel, s, t)
#     path = []
#     while t is not None:
#         path.append(t)
#         t = parents[t]
#     return (path[::-1], dist) if dist < inf else (None, inf)
#
# runtests(jak_dojade)
#
# G =[[-1, 6,-1, 5, 2],
# [-1,-1, 1, 2,-1],
# [-1,-1,-1,-1,-1],
# [-1,-1, 4,-1,-1],
# [-1,-1, 8,-1,-1]]
# P = [0,1,3]
#
# print(jak_dojade(G, P, 6, 0, 2))


def jak_dojade(G, P, d, a, b):
    n = len(G)
    visited = [False for _ in range(n)]
    petrol = [0 for _ in range(n)]
    weights = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]

    weights[a] = 0
    # visited[a] = True
    petrol[a] = d
    for _ in range(n):

        u = -1
        lowest = float('inf')
        for v in range(n):
            if visited[v] is False and weights[v] < lowest:
                lowest = weights[v]
                u = v
        oil = petrol[u]
        if u in P:
            oil = d
        # check whether weight of node is to big or petrol incoming willbe better
        for v in range(n):
            if visited[v] is False and (weights[v] > weights[u] + G[u][v] or petrol[v] < oil - G[u][v])and G[u][v] <= oil and G[u][v] > 0:
                petrol[v] = oil - G[u][v]
                parent[v] = u
                weights[v] = weights[u] + G[u][v]

        visited[u] = True

    if weights[b] == float('inf'):
        return None

    path = [b]
    while b != a:
        b = parent[b]
        path.append(b)
    path.reverse()
    print(f"Path: {path}")
    return path

runtests(jak_dojade)
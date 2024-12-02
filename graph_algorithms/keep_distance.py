"""
[2pkt.] Zadanie 1.
Szablon rozwiązania: zad1_nieparzysty_palindrom.py
Carol musi przewieźć pewne niebezpieczne substancje z laboratorium x do laboratorium y, podczas
gdy Max musi zrobić to samo, ale w przeciwną stronę. Problem polega na tym, że jeśli substancje
te znajdą się zbyt blisko siebie, to nastąpi reakcja w wyniku której absolutnie nic się nie stanie (ale
szefowie Carol i Max nie chcą do tego dopuścić, by nie okazało się, że ich praca nie jest nikomu
potrzebna). Zaproponuj, uzasadnij i zaimplementuj algorytm planujący jednocześnie trasy Carol
i Maxa tak, by odległość między nimi zawsze wynosiła co najmniej d. Mapa połączeń dana jest
jako graf nieskierowany, w którym każda krawędź ma dodatnią wagę (x i y to wierzchołki w tym
grafie). W jednostce czasu Carol i Max pokonują dokładnie jedną krawędź. Jeśli trzeba, dowolne z
nich może się w danym kroku zatrzymać (wówczas pozostaje w tym samym wierzchołku). Carol i
Max nie mogą równocześnie poruszać się tą samą krawędzią (w przeciwnych kierunkach).
Rozwiązanie należy zaimplementować w postaci funkcji:
def keep_distance(M, x, y, d):
...
która przyjmuje numery wierzchołków x oraz y, minimalną odległość d i graf reprezentowany przez
kwadratową, symetryczną macierz sąsiedztwa M. Wartość M[i][j] == M[j][i] to długość krawędzi
między wierzchołkami i oraz j, przy czym M[i][j] == 0 oznacza brak krawędzi między wierzchołkami.
W macierzy nie ma wartości ujemnych. Funkcja powinna zwrócić listę krotek postaci:
[(x, y), (u1, v1), (u2, v2), ..., (uk, vk), (y, x)]
reprezentującą ścieżki Carol i Max. W powyższej liście element (ui, vi) oznacza, że Carol znajduje
się w wierzchołku ui, zaś Max w wierzchołku vi. Można założyć, że rozwiązanie istnieje.
Przykład. Dla argumentów:
M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
x = 0
y = 3
d = 2
wynikiem jest na przykład lista: [(0, 3), (1, 2), (3, 0) ]
Podpowiedź. Proszę rozważyć nowy graf, być może z dużo większą liczbą wierzchołków niż graf
wejściowy
"""
from Exercise_1_tests import runtests
from math import inf
from queue import Queue


def Floyd_Warshall_algorithm(graph):

    distance = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])
    return distance


def generate_transitions(curr_x, curr_y, M, status, step):
    n = len(M)
    x_states = [i for i in range(n) if M[curr_x][i] < inf]

    y_states = [i for i in range(n) if M[i][curr_y] < inf]

    preferred_states = [[x, y] for x in x_states for y in y_states if status[x][y] is not None and status[x][y] > step]
    print(preferred_states)

    return preferred_states


def find_distance(M, x, curr_x,  y,curr_y,path, status, step):

    if curr_y == x and curr_x == y:
        return path
    next_states = generate_transitions(curr_x, curr_y, M, status, step)
    for i, j in next_states:
        status[i][j] = step


# def keep_distance(M, x, y,d):
#     n = len(M)
#     shortest_paths = Floyd_Warshall_algorithm(M)
#     print(shortest_paths)
#     status = [[None if shortest_paths[i][j] < d else inf for j in range(n)] for i in range(n)]
#     status[x][y] = None
#     path = []
#     step = 1
#     curr_x = x
#     curr_y = y
#     while curr_y != x and curr_x != y:
#         next_states = generate_transitions(curr_x, curr_y, M, status, step)
#         for i, j in next_states:
#             status[i][j] = step
#         print(next_states)
#         print(status)
#         break


# M = [
# [0, 1, 1, 0],
# [1, 0, 0, 1],
# [1, 0, 0, 1],
# [0, 1, 1, 0],
# ]
#
# M = [[inf if M[i][j] == 0 and i != j else M[i][j] for j in range(len(M)) ] for i in range(len(M))]
#
# keep_distance(M , 0, 3, 2)


def bfs(graph, parent, source):
    queue = Queue()
    queue.put(source)
    visited = [False] * len(graph)
    visited[source] = True
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                queue.put(v)
                visited[v] = True
                parent[v] = u


def floyd_warshall_algorithm(graph):
    distances = [[inf] * len(graph) for _ in range(len(graph))]
    for i in range(len(distances)):
        for j in range(len(distances)):
            if i == j:
                distances[i][j] = 0
            elif graph[i][j] != 0:
                distances[i][j] = graph[i][j]
    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distances[u][v] = min(distances[u][v], distances[u][k] + distances[k][v])
    return distances



def keep_distance(M, x, y, d):

    def is_correct_state(prev_x, prev_y, next_x, next_y):
        return (prev_y == next_y and M[prev_x][next_x] != 0) or (prev_x == next_x and M[prev_y][next_y] != 0) or (
                    M[prev_x][next_x] != 0 and M[prev_y][next_y] != 0)

    N = len(M)
    distances = floyd_warshall_algorithm(M)
    states_graph = [[0] * (N * N) for _ in range(N * N)]
    for prev_x in range(N):
        for prev_y in range(N):
            if prev_x != prev_y:
                for next_x in range(N):
                    for next_y in range(N):
                        if distances[next_x][next_y] < d or (next_x == prev_y and next_y == prev_x):
                            continue
                        if is_correct_state(prev_x, prev_y, next_x, next_y):
                            states_graph[prev_x * N + prev_y][next_x * N + next_y] = 1

    parent = [None] * (N * N)
    source = x * N + y
    bfs(states_graph, parent, source)
    result = []
    index = y * N + x
    while index is not None:
        result.append((index // N, index % N))
        index = parent[index]
    result.reverse()
    return result


runtests(keep_distance)
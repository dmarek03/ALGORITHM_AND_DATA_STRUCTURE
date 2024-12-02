# DOMINIK MAREK
# Najpierw przekształcam listę stacji tak aby otrzymać tylko opytmalny rower dla danego wierzchołka
# Następnie przekształcam graf na listę sąsiedztwa.Najpierw za pomocą algorytmu Djikstry obliczam dystans od
# wierzchołka s do każdego innego wierzchołka oraz do wierzchołka t do wszytskich pozostałych.
# Następnie jako min_time ustawiam czas przebięgniecia trasy do s do t. Kolejno iterujac przez stacjce z rowerem
# jeśli mogę dojsc do takiego wierzchołka zarówno z s jak i z t , to jako curr_time obliczam sumę czas dotarcia z s do i
# oraz z t do i , ale w tym przypadku mnożę czas jazdy rowerem przez współczynnik i-tego rowera.
# Następnie aktualizuję zmienną min_time.Finalnie zwracam tą zmienną jako rozwiązanie zadania.

# Złoźoność obliczeniowa O(ElogV)
# Złożoność pamieciowa O(E+V)


from egz1atesty import runtests
from queue import PriorityQueue
from math import inf

def filter_bike(B):
    bike_station =  [(b[0], b[1], b[2]) for b in B if b[1] < b[2]]



    optimal_bike_stations = {}
    for b in bike_station:
        if b[0] not in optimal_bike_stations or (
                b[1] / b[2] < optimal_bike_stations[b[0]][1] / optimal_bike_stations[b[0]][2]):
            optimal_bike_stations[b[0]] = b

    return list(optimal_bike_stations.values())


def create_adj_list(edges):
    n = 0
    for u, v, w in edges:
        n = max(n, u, v)
    n += 1

    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append([v, w])
        graph[v].append([u, w])

    return graph


def dijkstra_algorithm(graph, s):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0, s))
    distances = [inf] * n
    visited = [False] * n
    distances[s] = 0

    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:

           if not visited[v[0]]:
                if distances[v[0]] > distances[u] + v[1]:
                    distances[v[0]] = distances[u] + v[1]
                    queue.put((dist + v[1], v[0]))
        visited[u] = True
    return distances

def armstrong(B, G, s, t):
    bike_station_list = filter_bike(B)


    graph = create_adj_list(G)


    dist1 = dijkstra_algorithm(graph, s)
    dist2 = dijkstra_algorithm(graph, t)

    min_time = int(dist1[t])

    for idx, p, q in  bike_station_list:

        if dist1[idx] < inf and dist2[idx] < inf:
            min_time = min(min_time, int(dist1[idx]) + int(dist2[idx]*p/q))

    return min_time


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True)

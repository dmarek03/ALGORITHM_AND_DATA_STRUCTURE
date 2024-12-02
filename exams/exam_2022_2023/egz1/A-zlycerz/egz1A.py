from egz1Atesty import runtests
from math import inf
from queue import PriorityQueue

"""
Szablon rozwiązania: egz1A.py
Złożoność akceptowalna (+2.0pkt): O(V^3log V )
Złożoność wzorcowa (+2.0pkt): O(V^2log V )
Gdzie V to liczba wierzchołków grafu.
Złycerz (czyli zły rycerz) wędruje po średniowiecznym grafie G = (V, E), gdzie waga każdej
krawędzi to liczba sztabek złota, którą trzeba zapłacić za przejazd nią (myta, jedzenie, itp.). W
każdym wierzchołku znajduje się zamek, który zawiera w skarbcu pewną daną liczbę sztabek
złota. Złycerz może napaść na jeden zamek i zabrać całe jego złoto, ale od tego momentu
zaczyna być ścigany i każdy przejazd po krawędzi jest dwa razy droższy, oraz dodatkowo na
każdej drodze musi zapłacić r sztabek złota jako łapówkę (zatem od tej pory koszt przejazdu
danej krawędzi jest równy dwukrotności wagi tej krawędzi plus wartość r). Co więcej, Złycerz nie
może napaść więcej niż jednego zamku, bo jest trochę leniwy (oprócz tego, że zły). Proszę wskazać trasę Złycerza z 
zamku s do t o najmniejszym koszcie (lub największym zysku, jeśli to możliwe).
Uwaga. Złycerz może przejechać po danej krawędzi więcej niż raz (np. raz jadąc do zamku, który
chce napaść, a potem z niego wracając).
Zadanie polega na implementacji funkcji:
gold( G,V,s,t,r )
która na wejściu otrzymuje: graf G reprezentowany w postaci listowej, tablicę V zawierającą liczby
sztabek złota w kolejnych zamkach, zamek początkowy s, zamek końcowy t oraz wysokość łapówki r.
Funkcja powinna zwrócić najmniejszy koszt drogi uwzględniający ewentualny napad. Jeżeli zysk
z napadu jest większy, od kosztu drogi należy, powstały zysk należy zwrócić jako liczbę ujemną
(przykład).
Przykład. Dla wejścia:
G = [[(1,9), (2,2)], # 0
[(0,9), (3,2), (4,6)], # 1
[(0,2), (3,7), (5,1)], # 2
[(1,2), (2,7), (4,2), (5,3)], # 3
[(1,6), (3,2), (6,1)], # 4
[(2,1), (3,3), (6,8)], # 5
[(4,1), (5,8)] ] # 6
V = [25,30,20,15,5,10,0]
s = 0, t = 6, r = 7
wynikiem jest 6.
Gdyby nie rabować żadnego z zamków, najmniejszy koszt wyniósłby 2 + 1 + 3 + 2 + 1 = 9, droga
[0, 2, 5, 3, 4, 6]. Jednak jeżeli obrabujemy zamek 1 (30 sztabek złota), koszt wyniesie 2 + 1 + 3 + 2 −
30 + 19 + 9 = 6, droga [0, 2, 5, 3, 1, 4, 6]. Gdyby łapówka r wynosiła 10, żadna kradzież nie byłaby
opłacalna, jednak gdyby łapówka r wynosiła 3, wtedy (po obrabowaniu zamku 1), funkcja powinna
zwrócić wartość −3
"""


# COMPLEXITY -> O(EV)-> O(V^3)
def bellman_ford(graph: list[list[tuple[int, int]]], s: int, r: int, robbing: bool):
    n = len(graph)
    weights = [inf] * n
    weights[s] = 0

    for _ in range(n):
        for u in range(n):
            for v, weight in graph[u]:
                if robbing:
                    if weights[u] + 2 * weight + r < weights[v]:
                        weights[v] = weights[u] + 2 * weight + r
                else:
                    if weights[u] + weight < weights[v]:
                        weights[v] = weights[u] + weight
    return weights


# COMPLEXITY->O(E*logV) -> O(V^2logV)
# Wykorzystując algortym djikstry znajduję najpierw najtańśzą drogę do każdego wierzchołka z wiezrchołka startowego bez
# rabowania zamków. Następnie znajduje drogę do każdego wierzchołka z wierzchołka końcowego, jednak tym razem droga ta
# jest wyznaczana w warunkach obrabowania zamku(tj. koszt każdej krawędzi zwiększamy dwukrotnie oraz na przechodząc
# przez każdą krawędź musimy zapłacić okup w wysokości r.Finalnie wyznaczam minimalny koszt przejazdu trasy z s do t.
def dijkstra_algorithm(graph, s, r, robbing):
    n = len(graph)
    queue = PriorityQueue()
    queue.put((0, s))
    distances = [inf] * n
    visited = [False] * n
    distances[s] = 0

    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if robbing and not visited[v[0]]:
                if distances[v[0]] > distances[u] + r + 2*v[1]:
                    distances[v[0]] = distances[u] + r + 2*v[1]
                    queue.put((dist + 2*v[1]+r, v[0]))
            elif not visited[v[0]]:
                if distances[v[0]] > distances[u] + v[1]:
                    distances[v[0]] = distances[u] + v[1]
                    queue.put((dist + v[1], v[0]))
        visited[u] = True
    return distances


def gold(G, V, s, t, r):
    costs_before_robbing1 = dijkstra_algorithm(G, s, r, False)
    #print(f'{costs_before_robbing1=}')
    costs_after_robbing1 = dijkstra_algorithm(G, t, r, True)
    #print(f'{costs_after_robbing1=}')
    return min([costs_before_robbing1[i] + costs_after_robbing1[i]-V[i] for i in range(len(V))])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(gold, all_tests=True)

# from egz1atesty import runtests
# from queue import PriorityQueue
# from math import inf
#
# def filter_bike(B):
#     bikes_station = [(b[0], b[1], b[2]) for b in B if b[1] < b[2]]
#     optimal_bike_stations = {}
#     for b in bikes_station:
#         if b[0] not in optimal_bike_stations or (
#                 b[1] / b[2] < optimal_bike_stations[b[0]][1] / optimal_bike_stations[b[0]][2]):
#             optimal_bike_stations[b[0]] = b
#
#     return list(optimal_bike_stations.values())
#
#
# def create_adj_list(edges):
#     n = 0
#     for u, v, w in edges:
#         n = max(n, u, v)
#     n += 1
#
#     graph = [[] for _ in range(n)]
#     for u, v, w in edges:
#         graph[u].append([v, w])
#         graph[v].append([u, w])
#
#     return graph
#
#
#
# def dijkstra_algorithm(graph, s,bike_station, with_bike):
#     n = len(graph)
#     queue = PriorityQueue()
#     queue.put((0, s))
#     distances = [inf] * n
#     visited = [False] * n
#     distances[s] = 0
#
#
#
#     while not queue.empty():
#         dist, u = queue.get()
#         for v in graph[u]:
#             # if v == t:
#             #     return int(distances[t])
#             if with_bike and not visited[v[0]]:
#                 if bike_station[v[0]] != 0:
#                     bike_factor = bike_station[s]
#                 else:
#                     bike_factor= 1
#                 if distances[v[0]] > distances[u] +v[1]*bike_factor:
#                     distances[v[0]] = distances[u] + v[1]*bike_factor
#                     queue.put((dist + v[1]*bike_factor, v[0]))
#             elif not visited[v[0]]:
#                 if distances[v[0]] > distances[u] + v[1]:
#                     distances[v[0]] = distances[u] + v[1]
#                     queue.put((dist + v[1], v[0]))
#         visited[u] = True
#     return distances
# def armstrong(B, G, s, t):
#     bike_station_list = filter_bike(B)
#     print(f'{bike_station_list=}')
#     graph =  create_adj_list(G)
#     n = len(graph)
#     is_bike_station = [0]*n
#
#     for b in bike_station_list:
#         is_bike_station[b[0]] = b[1]/b[2]
#
#     min_time = inf
#
#
#     # for idx, p, q in bike_station_list:
#     #     bike_factor = p/q
#     #     time_1 = dijkstra_algorithm(graph, s,idx,0, with_bike=False )
#     #
#     #     if time_1 < inf:
#     #         time_2 = dijkstra_algorithm(graph, idx, t, bike_factor, with_bike=True)
#     #
#     #         curr_time  = int(time_1)+ int(time_2) if time_2 < inf else inf
#     #
#     #         if curr_time < min_time:
#     #             min_time = curr_time
#
#     dist1 = dijkstra_algorithm(graph,s, is_bike_station, with_bike=False)
#     dist2 = dijkstra_algorithm(graph, t, is_bike_station, with_bike=True)
#     print(dist1)
#     print(dist2)
#
#     return min(dist2[i] + dist1[i] for i in range(n))
#



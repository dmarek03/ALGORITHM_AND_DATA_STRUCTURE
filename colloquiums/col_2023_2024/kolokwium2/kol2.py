# Dominik Marek
# W celu rozwiązania zadania najpierw przeksztłcam liste krawędzie na graf w postaci listy sąsiedztwa.Nastepnie korzystam
# z algorytmu Dijkstry w celu znalezienia najkrótszej ścieżki do s do t. Jednak aby algorytm spełniał założenia zadania
# wprowadzam następujące modyfikacje:
# - listy distance i visited zostały przedstawione jako listy list (z podlistami o długości 17) tak aby reprezentować
#   dotarcie rycerza do wierzchołka z każdym możliwym zapasem snu (0-16)
# - do kolejki priorytetowej zawsze wkładam krotkę następujących elementów: obecny dystans do wierzchołka u,
#  liczba godzin w drodze przebytą przez rycerza aby dotrzeć do wierzchołka u, wierzchołek u
# - następnie przechodząć przez sąsiadów danego wierzchołka u , inicializuje zmienną current_time_in_travel,
#  reprezentującą obecny czas w podróży, która jest równa czasowi w podróży przebytym do wierzchołka u powiększonemu o czas
#  dostania się do danego sąsiada przetwarzanego wierzchołka
# - jeśli obecny czas w podróży jest większy niż 16, co oznacza, że rycerz musi odpocząć, to wówczas tworzę zmienną
# - additional_sleep = 8(w przeciwynym przypadku jest ona równa zero), która reprezentuje czas odpoczyku przez rycerza,
#  a zmienną current_time_in_travel ustawiam na na wartośc równą czasowi dotarcia do v-tego wierzchołka, gdyż jest to
#   równoważne z odpoczynkiem w u-tym wierzchołku a następnie dotarcia do v -tego wierzchołka
# - następnie relaksuje v -ty wierzchołek sprawdzająć czy dystans dotarcia do v-tego wierzchołka z czasem w podróży
#   równym current_time_in_travel jest większy niż dystans do wierzchołka u plus czas dotarcia z u do v plus zmienna
#   aditional_sleep, która reprezentuje czy musieliśmy po drogdze z u do v spać bądź nie. Jeśli relaksacja zaszła to do
#   kolejki jako in_travel wkładam current_time_in_travel
# - finalnie jeśli wierzchołek wjęty z kolejki to t wówczas zwracam dystans dotarcia do wierzchołka t z czasem w podrózy
#   równym in_travel
#
# Złożoność obliczeniowa: O(ElogV) -> złożoność algorytmu Dijkstry
# Złożoność pamięciowa: O(E) -> lista sąsiedztwa

from kol2testy import runtests
from queue import PriorityQueue
from math import inf
#
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


def dijkstra_algorithm(graph, s, t):
    n = len(graph)
    distance = [[inf]*17 for _ in range(n)]
    visited = [[False]*17 for _ in range(n)]
    distance[s][0] = 0


    pq = PriorityQueue()
    pq.put((0,0, s))

    while not pq.empty():
        dist, in_travel, u =  pq.get()

        if u == t:
            return distance[t][in_travel]


        for v, w in graph[u]:
            current_time_in_travel = in_travel + w
            additional_sleep = 0

            if current_time_in_travel > 16:
                current_time_in_travel = w
                additional_sleep = 8


            if not visited[v][current_time_in_travel] and distance[v][current_time_in_travel] > dist + w + additional_sleep:
                distance[v][current_time_in_travel] =  dist + w + additional_sleep
                pq.put((dist + w + additional_sleep, current_time_in_travel, v))
        visited[u][in_travel] = True

    return min(distance[t])


def warrior( G, s, t):
    adj_list = create_adj_list(G)

    return dijkstra_algorithm(adj_list, s, t)


def create_adj_matrix(edges_list):
    n = 0
    for u, v, w in edges_list:
        n = max(n, u, v)

    n += 1

    graph = [[-1]*n for _ in range(n)]

    for u, v, w in edges_list:
        graph[u][v] = w
        graph[v][u] = w

    return graph





def warrior_2(G, s, t):
    adj_matrix = create_adj_matrix(G)
    n = len(adj_matrix)
    distance = [[inf]*17 for _ in range(n)]
    pq = PriorityQueue()

    distance[s][0] = 0
    pq.put((distance[s][0], s, 0))

    while not pq.empty():

        curr_dist, u, time_in_travel = pq.get()

        for v in range(n):
            if adj_matrix[u][v] > 0:
                new_time_in_travel =time_in_travel +  adj_matrix[u][v]

                if new_time_in_travel > 16:
                    pq.put((curr_dist+8, u, 0))

                else:

                    if distance[v][time_in_travel + adj_matrix[u][v]] > curr_dist + adj_matrix[u][v]:
                        distance[v][time_in_travel + adj_matrix[u][v]]=  curr_dist + adj_matrix[u][v]

                        pq.put((distance[v][time_in_travel+adj_matrix[u][v]], v, time_in_travel+adj_matrix[u][v]))

    return min(distance[t])







runtests(warrior, all_tests=True)




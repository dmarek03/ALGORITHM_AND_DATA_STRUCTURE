# DOMINIK MAREK
# Aby rozwiązać zadanie w pierwszym wywołaniu algorytmu Djikstry znajduję najkrótszą drogę od wierzchołka a do b oraz
# od wierzchołka a do najbliższej osobliwośći. Następnie:
# 1. Jeśli nie udało się znaleźć ani jeden z tych wartośći( funkcja zwróćiła None, None) to oznacza iż droga do a do b
# nie istnieje , więc funkcja zwraca None.
# 2. Jeśli nie udało się dojść do osobliwośći, to funkcja zwraca odległość do a do b, wyznaczoną w pierwszym wywołaniu.
# 3. Jeśli natomiast udało się znaleźć drogę jedynie do osobliwośći, to wywołuję algorytm Djikstry drugi,
# tym razem w argumnetach zmieniając początek z końcem.Kolejno sprawdzam czy tym razem udało się znaleźć drogę od b do
# osobliwośći, jeśli tak to funkcja zwraca sum dróg od a do osobliowści i od b od osobliwośći, w przeciwnym razie None.
# 4.Jeśli znalezione zostały obie drogi,to również wywołuję algorytm Djikstry drugi raz,z zamienionymi agrmuntami a i b,
# i jeśli udało się znaleźć drogę od b do osobliwośći to funkcja zwraca minimum z drogi bez osobliwości oraz sumy dróg
# dróg od a do osobliowści i od b od osobliwośći.
# Złożoność obliczeniowa tego algorytmu to O(mlogn), a złożoność pamięciowa to O(4m), gdzie m to długość listy adj_list,
# a n to liczba planet.


from queue import PriorityQueue
from math import inf


def dijkstra_algorithm(graph, source, end, S, direct_link_known=False, normal_path_needed=True):

    def relax(u, v, distance):
        if distance[v[0]] > distance[u] + v[1]:
            distance[v[0]] = distance[u] + v[1]
            return True
        return False

    n = len(graph)
    in_s = [False] * n
    for s in S:
        in_s[s] = True

    queue = PriorityQueue()
    queue.put((0, source))
    distances = [inf] * n
    max_distance1 = None
    max_distance2 = None
    visited = [False] * n
    distances[source] = 0
    if in_s[source] and in_s[end]:
        return None, 0
    while not queue.empty():
        dist, u = queue.get()
        if u == end and normal_path_needed:
            max_distance1 = dist
            return max_distance1, max_distance2

        if in_s[u] and not max_distance2:
            max_distance2 = dist
            if direct_link_known:
                return max_distance1, max_distance2
        else:
            for v in graph[u]:
                if not visited[v[0]] and relax(u, v, distances):
                    queue.put((dist + v[1], v[0]))

        visited[u] = True
    return max_distance1, max_distance2


def spacetravel(n, E, S, a, b):

    adj_list = [[] for _ in range(n)]
    for e in E:
        adj_list[e[0]].append([e[1], e[2]])
        adj_list[e[1]].append([e[0], e[2]])

    distance1a, distance2a = dijkstra_algorithm(adj_list, a, b, S)

    if distance1a is None and distance2a is None:
        return None
    if distance1a is not None and distance2a is None:
        return distance1a
    if distance1a is None and distance2a is not None:
        distance1b, distance2b = dijkstra_algorithm(adj_list, b, a, S, direct_link_known=True, normal_path_needed=False)
        return distance2a + distance2b if distance2b is not None else None

    if distance1a is not None and distance2a is not None:
        distance1b, distance2b = dijkstra_algorithm(adj_list, b, a, S, direct_link_known=True, normal_path_needed=False)

        distance2 = distance2a + distance2b if distance2b is not None else None

        return distance1a if distance2 and distance1a < distance2 else distance2
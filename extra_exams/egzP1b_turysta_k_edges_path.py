from egzP1btesty import runtests 
from math import inf
from queue import PriorityQueue

# Complexity -> O(nlogn) -> djikstra z ograniczeniami\
# Towrzymy tablice distances i visited, które przechowują informacje na temat kosztu doejchania oraz wizytacji danego
# wierzchołka zaczynając z wierzchołka początkowego i przechodzać przez pokadnie k krawędzi , 0 <= k <=4.
# Następnie korzystamy z algorytmu djikstry, aby z wiezrchołka startowego znaleźć najkrótszą ścieżke do każdego  innego
# wierzchołka, przechodzącą przez dokładnie k krawędzi.
def weighted_undirected_graph_list(edges_list):
    n = 0
    for edge in edges_list:
        n = max(n, edge[0], edge[1])
    n += 1

    adj_list = [[] for _ in range(n)]

    for edges in edges_list:
        adj_list[edges[0]].append([edges[1], edges[2]])
        adj_list[edges[1]].append([edges[0], edges[2]])

    return adj_list


def turysta(G: list, D: int, L: int) -> int:
    # tutaj proszę wpisać własną implementację
    adj_list = weighted_undirected_graph_list(G)
    n = len(adj_list)

    # for i,j in enumerate(G):
    #     print(i,j)

    distances = [[inf for _ in range(5)] for _ in range(n)]
    visited = [[False for _ in range(5)] for _ in range(n)]
    distances[D][0] = 0
    p_queue = PriorityQueue()
    p_queue.put((0, 1, D))

    while not p_queue.empty():
        d, ind, u = p_queue.get()
        if ind < 5:
            for v, w in adj_list[u]:
                if not visited[v][ind] and distances[v][ind] > d + w:
                    distances[v][ind] = d + w
                    p_queue.put((d + w, ind + 1, v))
                    if n < 10:
                        print('---------------------------------')
                        print(*distances, sep='\n')
                        print('---------------------------------')
                        print(*visited, sep='\n')
            visited[u][ind - 1] = True
    if n < 10:
        print(*adj_list, sep='\n')
        print('---------------------------------')
        print(*distances, sep='\n')
        print('---------------------------------')
        print(*visited, sep='\n')

    return int(distances[L][4])


runtests(turysta)


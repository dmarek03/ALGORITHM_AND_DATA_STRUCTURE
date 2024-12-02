# DOMINIK MAREK
from zad5testy import runtests
from queue import PriorityQueue
from math import inf


def dijkstra(graph:list[list[tuple[int, int]]], a: int, b: int, singularities: list[int], using_singularities:bool = False):
    n = len(graph)
    normal_min_dist =  None
    min_dist_to_singularity =  None
    visited = [False]*n
    distance = [inf]*n
    pq = PriorityQueue()
    pq.put((0, a))
    distance[a] = 0


    while  not pq.empty():
        dist, u = pq.get()

        if u == b:
            normal_min_dist = dist
            return  normal_min_dist, min_dist_to_singularity

        if singularities[u] and not min_dist_to_singularity:
            min_dist_to_singularity = dist
            if using_singularities:
                return normal_min_dist, min_dist_to_singularity


        for v, val in graph[u]:
            if not visited[v] and distance[v] > val + distance[u]:
                distance[v] = val + distance[u]
                pq.put((dist + val, v))
        visited[u] = True

    return normal_min_dist, min_dist_to_singularity


def spacetravel( n, E, S, a, b ):

    graph = [[] for _ in range(n)]
    for u, v, val in E:
        graph[u].append([v, val])
        graph[v].append([u, val])


    singularities = [False]*n

    for s in S:
        singularities[s] = True

    if singularities[a] and singularities[b]:
        return 0


    min_d_1, min_d_2 = dijkstra(graph, a, b, singularities)

    if min_d_1 is not None and min_d_2 is None:
        return min_d_1

    if min_d_2 is not None:

        min_d_4 = dijkstra(graph, b, a, singularities, using_singularities=True)[1]

        if min_d_4 is not None:
            return min(min_d_4 + min_d_2, min_d_1) if min_d_1 is not None else min_d_2 + min_d_4
        else:
            return None

    return None


runtests( spacetravel, all_tests = True)
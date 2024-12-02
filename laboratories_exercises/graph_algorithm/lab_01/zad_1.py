from random import randint
from collections import deque
from queue import  Queue
def generate_graph(num_vertex, num_edges):
    graph = [[0] * num_vertex for _ in range(num_vertex)]
    generated_edges = 0

    while generated_edges < num_edges:
        u,v = randint(0, num_vertex-1), randint(0, num_vertex-1)
        if u != v:
            if not graph[u][v]:
                graph[u][v], graph[v][u] = 1, 1
                generated_edges += 1
    return graph



def bfs(graph: list[list[int]]):
    dq = deque()
    dq.append(0)
    n = len(graph)
    colors = [0]*n
    colors[0] = 1
    while dq:
        v = dq.popleft()
        for i in range(n):
            if graph[v][i]:
                if colors[i] == 0:
                    colors[i] = 3 - colors[v]
                    dq.append(i)

                elif colors[i] == colors[v]:
                    return False
    return True




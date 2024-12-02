from collections import deque

# 1 - BFS


def is_bipartite(graph):
    n = len(graph)
    colors = [0]*n
    colors[0] = 1
    dequeue = deque()
    dequeue.append(0)
    while dequeue:
        u = dequeue.popleft()
        for v in graph[u]:
            if colors[v] == 0:
                colors[v] = 3 - colors[u]
                dequeue.append(v)
            elif colors[v] == colors[u]:
                return False
    return True


g1 = [[1, 2, 3],
     [0,4],
     [0,4],
     [0],
     [1, 2]

     ]


g2= [[1, 2, 3],
     [0,2, 4],
     [0,1, 4],
     [0],
     [1, 2]

     ]
print(is_bipartite(g1))
print(is_bipartite(g2))
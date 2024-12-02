from queue import Queue


def has_cycle(graph: list[list[int]], source: int) -> bool:
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    q = Queue()
    visited[source] = True
    q.put(source)
    while not q.empty():
        u = q.get()
        for neighbor in graph[u]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = u
                q.put(neighbor)
            elif parent[u] != neighbor:
                return True
    return False

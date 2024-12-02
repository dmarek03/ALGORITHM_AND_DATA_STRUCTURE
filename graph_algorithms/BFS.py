# Breadth First Search
from queue import Queue
from collections import deque
# 1 ADJACENCY LIST


def BFS_adjacency_list(graph, root):
    queue = Queue()
    visited = [False] * len(graph)
    result = []
    queue.put(root)
    visited[root] = True
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.put(v)
                visited[v] = True
    return result

graph = [
    [1, 8],
    [0],
    [3, 4, 5, 8],
    [2],
    [2, 7],
    [2, 6],
    [5, 8],
    [4, 6],
    [0, 2, 6]
]

result = BFS_adjacency_list(graph, 2)
#print(result)



# 2 MATRIX


def BFS_matrix(graph_matrix, source):
    n = len(graph_matrix)
    queue = Queue()
    visited = [False]*n
    result = []
    visited[source] = True
    queue.put(source)
    while not queue.empty():
        u = queue.get()
        result.append(u)
        for i in range(n):
            if not visited[i] and graph_matrix[u][i] > 0:
                queue.put(i)
                visited[i] = True
    return result


undirected_matrix = [
    [0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
]

#print(BFS_matrix(undirected_matrix, 2))


# 3 BFS - the shortest path in unweighted undirected graph


def shortest_path_between(graph, vertex1: int, vertex2: int):
    if vertex1 == vertex2:
        return [vertex1]
    dist = 0
    num_vertices = len(graph)
    visited = [False] * num_vertices
    dequeue = deque()
    # Adding the starting vertex to deque
    dequeue.append((vertex1, [vertex1], dist))
    # Marking the starting vertex as visited
    visited[vertex1] = True

    while dequeue:
        vertex, path, dist = dequeue.popleft()
        # if lately popped vertex is our destination we return path
        if vertex == vertex2:
            return path, dist

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dequeue.append((neighbor, path + [neighbor], dist+1))
                visited[neighbor] = True

    return None



graph1 = [
    [1, 8],
    [0],
    [3, 4, 5, 8],
    [2],
    [2, 7],
    [2, 6],
    [5, 8],
    [4, 6],
    [0, 2, 6]
]

shortest_path, dist = shortest_path_between(graph1, 0, 6)
print(shortest_path)
print(dist)
print(f"length of path between 2 and 6 = {len(shortest_path)-1}")
# Graph transformation
"""--------------------------MATRIX--------------------------"""

# 1) DIRECTED GRAPH MATRIX


def directed_graph_matrix(E: 'array of edges', n: 'number of vertices'):
    M = [[0] * n for _ in range(n)]
    # Store Nones on the main diagonal
    # for i in range(n):
    #     M[i][i] = 0
    # Store information which vertices are connected with an edge
    for edge in E:
        M[edge[0]][edge[1]] = 1
    return M

E = [(0, 1), (3, 1), (2, 3), (1, 2), (2, 4)]

G = directed_graph_matrix(E, 5)
print(*G, sep='\n')
print("------------------")


# 2) UNDIRECTED GRAPH MATRIX
def undirected_graph_matrix(E: 'array of edges', n: 'number of vertices'):
    M = [[0] * n for _ in range(n)]
    # Store Nones on the main diagonal
    # for i in range(n):
    #     M[i][i] = 0
    # Store information which vertices are connected with an edge
    for edge in E:
        M[edge[0]][edge[1]] = 1
        # We must add symmetric edge
        M[edge[1]][edge[0]] = 1
    return M


G = undirected_graph_matrix(E, 5)
print(*G, sep='\n')
print("------------------")


# 3) WEIGHTED DIRECTED GRAPH MATRIX

def weighted_directed_graph_matrix(E: 'array of edges', n: 'number of vertices'):
    M = [[0] * n for _ in range(n)]

    # Set the diagonal to -1
    for i in range(n):
        M[i][i] = -1

    for edge in E:
        M[edge[0]][edge[1]] = edge[2]

    return M


E = [(0, 1, -5), (3, 1, 10), (2, 3, 7), (1, 2, -3), (2, 4, 0)]
G = weighted_directed_graph_matrix(E, 5)
print(*G, sep='\n')
print("------------------")


# 4) WEIGHTED UNDIRECTED GRAPH MATRIX

def weighted_undirected_graph_matrix(E: 'array of edges', n: 'number of vertices'):
    M = [[0] * n for _ in range(n)]

    # Set the diagonal to -1
    for i in range(n):
        M[i][i] = -1

    for edge in E:
        M[edge[0]][edge[1]] = edge[2]
        # Adding the symmetric egdes
        M[edge[1]][edge[0]] = edge[2]

    return M


E = [(0, 1, -5), (3, 1, 10), (2, 3, 7), (1, 2, -3), (2, 4, 0)]
G = weighted_undirected_graph_matrix(E, 5)
print(*G, sep='\n')
print("------------------")


# 5) WEIGHTED UNDIRECTED GRAPH MATRIX WITHOUT NUMBER OF VERTEXES
def undirected_weighted_graph_matrix(E: 'array of edges'):
    # Find a number of vertices
    n = 0
    for e in E:
        n = max(n, e[0], e[1])
    n += 1
    # Create a graph
    G = [[-1] * n for _ in range(n)]  # -1 means no edge
    for e in E:
        G[e[0]][e[1]] = e[2]
        G[e[1]][e[0]] = e[2]
    return G

G = undirected_weighted_graph_matrix([(0, 1, 3), (1, 2, 2), (0, 6, 2), (6, 7, 1), (6, 5, 3),
                                      (5, 7, 1), (5, 4, 8), (3, 4, 20), (8, 7, 7), (8, 1, 1),
                                      (2, 3, 5), (3, 8, 1), (7, 4, 2)])
s = 0
print(*G, sep='\n')
print("------------------")



"""--------------------------ADJACENCY_LIST--------------------------"""


# 1) DIRECTED GRAPH ADJACENCY LIST

def directed_graph_list(E: 'array of edges', n: 'number of vertices'):
    M = [[] for _ in range(n)]

    for edges in E:
        M[edges[0]].append(edges[1])

    return M


G = directed_graph_list(E, 5)
print(*G, sep='\n')
print("------------------")


# 2) UNDIRECTED GRAPH ADJACENCY LIST

def undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    M = [[] for _ in range(n)]

    for edges in E:
        M[edges[0]].append(edges[1])
        M[edges[1]].append(edges[0])

    return M


G = undirected_graph_list(E, 5)
print(*G, sep='\n')
print("------------------")



# 3) WEIGHTED DIRECTED GRAPH ADJACENCY LIST

def weighted_directed_graph_list(E: 'array of edges', n: 'number of vertices'):
    M = [[] for _ in range(n)]

    for edges in E:
        M[edges[0]].append([edges[1], edges[2]])

    return M

E = [(0, 1, -5), (3, 1, 10), (2, 3, 7), (1, 2, -3), (2, 4, 0), (3, 1, -5), (0, 1, 2), (0, 0, -10)]
G = weighted_directed_graph_list(E, 5)
print(*G, sep='\n')
print("------------------")


# 4) WEIGHTED UNDIRECTED GRAPH ADJACENCY LIST

def weighted_undirected_graph_list(E: 'array of edges', n: 'number of vertices'):
    M = [[] for _ in range(n)]

    for edges in E:
        M[edges[0]].append([edges[1], edges[2]])
        M[edges[1]].append([edges[0], edges[2]])

    return M

E = [(0, 1, -5), (3, 1, 10), (2, 3, 7), (1, 2, -3), (2, 4, 0), (3, 1, -5), (0, 1, 2), (0, 0, -10)]
G = weighted_undirected_graph_list(E, 5)
print(*G, sep='\n')
print("------------------")




"""--------------------------MATRIX TO ADJACENCY_LIST--------------------------"""


def matrix_to_list(matrix:list[list[int]]):
    #  matrix - weighted_undirected_graph or weighted_directed_graph
    n = len(matrix)
    adjacency_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1:
                adjacency_list[i].append([j, matrix[i][j]])
    return adjacency_list


undirected_matrix = [
    [-1, 2, -1, -1, 3],
    [2, -1, 1, 5, -1],
    [-1, 1, -1, 4, -1],
    [-1, 5, 4, -1, 6],
    [3, -1, -1, 6, -1]
]

directed_matrix = [
 [-1, 2, -1, -1, 3],
 [-1, -1, 1, 5, -1],
 [-1, -1, -1, 4, -1],
 [-1, -1, -1, -1, 6],
 [-1, -1, -1, -1, -1]
]


adj_list = matrix_to_list(undirected_matrix)
print(*adj_list, sep='\n')
print("------------------")


"""--------------------------ADJACENCY_LIST TO MATRIX--------------------------"""


def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[-1]*n for _ in range(n)]
    for vertex, neighbors in enumerate(adj_list):
        for neighbor, weight in neighbors:
            matrix[vertex][neighbor] = weight

    return matrix




adj_list1 = [
 [[1, 2], [4, 3]],
 [[0, 2], [2, 1], [3, 5]],
 [[1, 1], [3, 4]],
 [[1, 5], [2, 4], [4, 6]],
 [[0, 3], [3, 6]]
]

matrix1 = adjacency_list_to_matrix(adj_list1)
print(*matrix1, sep='\n')
print("------------------")
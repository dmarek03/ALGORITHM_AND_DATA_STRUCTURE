from egzP7atesty import runtests
from math import inf
# Complexity -> O(sqrt(V)*E)
# Dla każdego studenta sprawdzam czy wedle jego preferencji jest możliwe znalezienie mu wolnego pokoju. Realizowane jest
# to poprzez funkcje students_to_rooms , która rekurencyjnie sprawdza czy można przypisać studenta do jednej z jego
# preferencji lub kogoś kto obecnie zajmuje dany pokój przepisać do innego z jego preferencji.Dodatkowo zliczamy
# studentów, którzy nie podali żadnych prefernecji. Finalnie od liczby wszystkich studentów odejmujemy liczbę
# zadowolonych studentów oraz tych, którzy nie podali żadnych preferencji.


def students_to_rooms(students_preferences: list[list[int]], booked_rooms: list[int], rooms: list[int], students: int) -> bool:
    for p in students_preferences[students]:
        if not booked_rooms[p]:
            booked_rooms[p] = True
            if rooms[p] < 0 or students_to_rooms(students_preferences, booked_rooms, rooms, rooms[p]):
                rooms[p] = students
                return True

    return False


def get_max_number_of_content_students(adj_list: list[list[int]]) -> int:

    n = len(adj_list)
    rooms = [-1] * n
    content_students = 0
    for students in range(n):
        booked_rooms = [False]*n
        content_students += 1 if students_to_rooms(adj_list, booked_rooms, rooms, students) else 0
        if n < 10:
            print(f'{booked_rooms=}')
    return content_students


def create_adj_list(edges_list):
    n = len(edges_list)
    adj = [[] for _ in range(n)]
    empty = 0
    for i in range(n):
        if edges_list[i] == (None, None, None):
            empty += 1
        for x in edges_list[i]:
            if x is not None:
                adj[i].append(x)
    return adj, empty



def adj_list(edges_list):
    s = len(edges_list) * 2
    t = s + 1
    n = t + 1
    n1 = len(edges_list)

    graph = [[] for _ in range(n)]
    empty = 0

    for i in range(n1):
        if edges_list[i] == (None, None, None):
            empty += 1
        for j in range(3):
            if edges_list[i][j] is not None:
                graph[i].append((n1 + edges_list[i][j], 1))  # Adding edge with capacity 1

    for i in range(n1):
        graph[s].append((i, 1))       # Source to each student
        graph[n1 + i].append((t, 1))  # Each content to sink

    return graph, empty, s, t


def add_back_edges(G):
    n = len(G)
    counts = [0] * n  # Numbers of edges in an initial graph (before modification)

    for u in range(n):
        counts[u] = len(G[u])

    for u in range(n):
        for i in range(counts[u]):
            v, _ = G[u][i]
            if not any(x[0] == u for x in G[v]):
                G[v].append((u, 0))  # Add an edge with no capacity

    return counts


def remove_back_edges(G, counts):
    for u in range(len(G)):
        while len(G[u]) > counts[u]:
            G[u].pop()


def ford_fulkerson(G, s, t):
    n = len(G)
    flow = [[0] * n for _ in range(n)]
    visited = [0] * n
    token = 1  # Number of iteration to check which vertices have been visited
    max_flow = 0

    counts = add_back_edges(G)

    def dfs(u, bottleneck):
        visited[u] = token
        if u == t:
            return bottleneck
        for v, capacity in G[u]:
            remaining = capacity - flow[u][v]
            if visited[v] != token and remaining > 0:
                new_bottleneck = dfs(v, min(bottleneck, remaining))
                if new_bottleneck > 0:
                    flow[u][v] += new_bottleneck
                    flow[v][u] -= new_bottleneck
                    return new_bottleneck
        return 0

    while True:
        increase = dfs(s, inf)
        if increase == 0:
            break
        max_flow += increase
        token += 1

    remove_back_edges(G, counts)

    return max_flow

def akademik(tab):
    # graph, empty = create_adj_list(tab)
    #
    # return len(graph) - get_max_number_of_content_students(graph) -


    graph, empty, s, t = adj_list(tab)

    print(f'{graph=}')
    return len(tab) - ford_fulkerson(graph, s, t) - empty


runtests(akademik)

from egz3atesty import runtests
from queue import PriorityQueue
from math import inf
# Dominik Marek
# Najpierw przerabiam macierz na listę sąsiedztwa a następnie za pomocą algorytmu djikstry znajduje najkrótszy czas
# potrzebny do przejechania z zamku s do t. Jeśli znaleziony czas jest większy niż limit czasu w podróży to znaczy, że
# rycerz musiał się gdzieś zatrzymać po drodze, zatem tworze zmienną final_min_time , której przypisuje wynik algorytmu
# djikstry i dopóki znaleziony czas jest większy niż limit czasu w podrózy to pomniejszam go  o ten limit a
# final_min_time zwiększam o 8, bo rycerz musiał nocować.Końcowo zwracam min_time co jest rozwiązaniem naszego zadania.
# Złożoność 0(nlogn) -> djikstra na liście sąsiedztwa , gdyż  liczba krawędzi jest O(n).


def matrix_to_list(matrix: list[list[int]]):
    n = len(matrix)
    adjacency_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                adjacency_list[i].append([j, matrix[i][j]])
    return adjacency_list


def goodknight(G, s, t):
    n = len(G)
    adj_list = matrix_to_list(G)
    # Initialize distances and visited array
    distances = [[inf] * 17 for _ in range(n)]
    visited = [[False] * 17 for _ in range(n)]
    distances[s][0] = 0

    # Priority queue to store (distance, sleep time, node)
    p_queue = PriorityQueue()
    p_queue.put((0, 0, s))

    while not p_queue.empty():
        d, sleep, u = p_queue.get()

        for v, w in adj_list[u]:

            new_sleep = sleep + w
            additional_sleep = 0

            # Check if knight needs to spend additional 8 hours in the castle
            if new_sleep > 16:
                additional_sleep = 8
                new_sleep = w  # Reset the sleep time to the cost of travel to next castle  after
                # spending 8 hours in the current castle

            if not visited[v][new_sleep] and distances[v][new_sleep] > d + w + additional_sleep:
                distances[v][new_sleep] = d + w + additional_sleep
                p_queue.put((d + w + additional_sleep, new_sleep, v))
                #print(*distances, sep='\n')


        visited[u][sleep] = True

    # Find the minimum time to reach the destination t
    min_time = min(distances[t])
    return min_time

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests = True)


G1 = [ [-1, 8, -1, -1, -1, 8, -1, -1, -1], # 0
    [ 8, -1, 1, -1, -1, -1, -1, -1, -1], # 1
    [-1, 1, -1, 8, -1, -1, -1, -1, -1], # 2
    [-1, -1, 8, -1, 4, -1, -1, -1, -1], # 3
    [-1, -1, -1, 4, -1, -1, -1, -1, 5], # 4
    [ 8, -1, -1, -1, -1, -1, 8, -1, -1], # 5
    [-1, -1, -1, -1, -1, 8, -1, 8, -1], # 6
    [-1, -1, -1, -1, -1, -1, 8, -1, 8], # 7
    [-1, -1, -1, -1, 5, -1, -1, 8, -1]]

s1 = 0
t1 = 8

G2 = [ [-1, 8, -1, -1, -1, 8, -1, -1], # 0
    [ 8, -1, 1, -1, -1, -1, -1, -1], # 1
    [-1, 1, -1, 8, -1, -1, -1, -1], # 2
    [-1, -1, 8, -1, 1, -1, -1, -1], # 3
    [-1, -1, -1, 1, -1, -1, 5, 8], # 4
    [ 8, -1, -1, -1, -1, -1, 8, -1], # 5
    [-1, -1, -1, -1, 5, 8, -1, -1], # 6
    [-1, -1, -1, -1, 8, -1, -1, -1] ]

s2 = 0
t2 = 7
print(goodknight(G1, s1, t1))
print(goodknight(G2, s2, t2))
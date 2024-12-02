"""
[2pkt.] Zadanie 1.
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None.
Przykład Dla tablicy
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]
funkcja islands(G1, 5, 2) powinna zwrócić wartość 13.
"""

from queue import PriorityQueue
from math import inf


def relax(distance, u, v, cost, queue):
    if cost == 1:
        if distance[u][0] + cost < distance[v][1]:
            distance[v][1] = distance[u][0] + cost
            queue.put((distance[v][1], v))
        if distance[u][0] + cost < distance[v][2]:
            distance[v][2] = distance[u][0] + cost
            queue.put((distance[v][2], v))
    elif cost == 5:
        if distance[u][1] + cost < distance[v][0]:
            distance[v][0] = distance[u][1] + cost
            queue.put((distance[v][0], v))
        if distance[u][1] + cost < distance[v][2]:
            distance[v][2] = distance[u][1] + cost
            queue.put((distance[v][2], v))
    else:
        if distance[u][2] + cost < distance[v][0]:
            distance[v][0] = distance[u][2] + cost
            queue.put((distance[v][0], v))
        if distance[u][1] + cost < distance[v][1]:
            distance[v][1] = distance[u][1] + cost
            queue.put((distance[v][1], v))


def islands(G, A, B):
    distance = [[inf] * 3 for _ in range(len(G))]
    for i in range(3):
        distance[A][i] = 0
    queue = PriorityQueue()
    queue.put((0, A))
    visited = [False] * len(G)
    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(G)):
            if not visited[v] and G[u][v] != 0:
                relax(distance, u, v, G[u][v], queue)
        visited[u] = True
    return min(distance[B])


G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]
print(islands(G, 5, 2))
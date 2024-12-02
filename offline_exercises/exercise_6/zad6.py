# Dominik Marek
from zad6testy import runtests
from math import inf
from queue import PriorityQueue


"""
Dany jest ważony, nieskierowany graf G oraz dwumilowe buty - specjalny sposób poruszania się
po grafie. Dwumilowe buty umożliwiają pokonywanie ścieżki złożonej z dwóch krawędzi grafu tak,
jakby była ona pojedynczą krawędzią o wadze równej maksimum wag obu krawędzi ze ścieżki. Istnieje jednak ograniczenie 
- pomiędzy każdymi dwoma użyciami dwumilowych butów należy przejść
w grafie co najmniej jedną krawędź w sposób zwyczajny. Macierz G zawiera wagi krawędzi w grafie,
będące liczbami naturalnymi, wartość 0 oznacza brak krawędzi.
Proszę opisać, zaimplementować i oszacować złożoność algorytmu znajdowania najkrótszej ścieżki
w grafie z wykorzystaniem mechanizmu dwumilowych butów.
Rozwiązanie należy zaimplementować w postaci funkcji:
def jumper(G, s, w):
...
która zwraca długość najkrótszej ścieżki w grafie G pomiędzy wierzchołkami s i w, zgodnie z
zasadami używania dwumilowych butów.
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę przedstawić złożoność
czasową oraz pamięciową użytego algorytmu.
"""


def Dijkstra(graph, s, t):
    n = len(graph)
    distance = [[inf] * 2 for _ in range(n)]
    distance[s][0] = 0
    queue = PriorityQueue()
    queue.put((0, (0, s))) # Argument O: current distance , Argument 1: current vertex ,
    # Argument 3: 0 - the vertex was reached without jumping, 1- the vertex was reached with help of special boots
    while not queue.empty():
        value, (state, vertex) = queue.get()
        if vertex == t:
            return distance[t][state]

        # Jeśli dotarliśmy do wierzchołka nie używając dwumilowych butów, to przechodzac przez wszystkie sąsiednie
        # wierzchołki, rozpatrujemy ich sąsiadów aby uzwględnić skok o dwie krawędzie . Następnie jak wagę podwójnej krawędzi
        # bierzemy większą wagę z krawędzi między wierzchołkiem do którego dotarlismy a wierzchołkiem będącym końcowym
        # wierzchołkiem ścieżki o długości 2 wychodzącej z rozpatrywanego wierzchołka. Następnie następuje relaksacja
        # dystansu do wierzchołka odległego o 2 od rozpatrywanego wierzchołka z użyciem butów.
        if state == 0:
            for a in range(n):
                if graph[vertex][a] > 0:
                    for b in range(n):
                        if graph[a][b] > 0:
                            edge_value =  max(graph[a][b], graph[vertex][a])

                            if distance[b][1]  > distance[vertex][0] + edge_value:
                                distance[b][1] =  distance[vertex][0] + edge_value
                                queue.put((distance[vertex][0] + edge_value, (1, b)))

        # Jeśli dochodząc do wierzchołka użylismy specjalnych butów to dystans do kolejnych wierzchołków wychodzących
        # z rozpatrywanego wierzchołka rożważamy relaksację dwóch możliwych dystansów a więc dojście do niego
        # uwzględiając dystans do wcześniejeszego wierzchołka zarówno z użyciem butów oraz bez nich.
        for a in range(n):
            if graph[vertex][a]:

                if distance[a][0] > graph[vertex][a] + distance[vertex][0]:
                    distance[a][0] =  graph[vertex][a] + distance[vertex][0]
                    queue.put((graph[vertex][a] + distance[vertex][0], (0, a)))

                if distance[a][0] > graph[vertex][a] + distance[vertex][1]:
                    distance[a][0] = graph[vertex][a] + distance[vertex][1]
                    queue.put((graph[vertex][a] + distance[vertex][1], (0, a)))


    # Finalnie zwracam minimalny dystans z wierzchołka początkowego do wierzchołka końcowego, zarówno z użyciem
    # dwumilowych butów oraz bez nich

    return min(distance[t][0], distance[t][1])


def jumper(G, s, w):

    return Dijkstra(G,s, w)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True)
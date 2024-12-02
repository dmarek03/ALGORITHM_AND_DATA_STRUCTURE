"""
[2pkt.] Zadanie 2.
Szablon rozwiązania: zad2_snow.py
Dany jest graf nieskierowany G = (V, E), gdzie każdy wierzchołek z V ma przypisaną małą literę z
alfabetu łacińskiego, a każda krawędź ma wagę (dodatnią liczbę całkowitą). Dane jest także słowo
W = W[0], . . . ,W[n − 1] składające się małych liter alfabetu łacińskiego. Należy zaimplementować
funkcję letters(G,W), która oblicza długość najkrótszej ścieżki w grafie G, której wierzchołki
układają się dokładnie w słowo W (ścieżka ta nie musi być prosta i może powtarzać wierzchołki).
Jeśli takiej ścieżki nie ma, należy zwrócić -1.
Struktury danych. Graf G ma n wierzchołków ponumerowanych od 0 do n − 1 i jest reprezentowany jako para (L, E). L to
lista o długości n, gdzie L[i] to litera przechowywana w wierzchołku i. E jest listą krawędzi i każdy jej element jest
trójką postaci (u, v, w), gdzie u i v to wierzchołki połączone krawędzią o wadze w.
Przykład. Rozważmy graf G przedstawiony poniżej:
W reprezentacji przyjętej w zadaniu mógłby być zapisany jako:
# 0 1 2 3 4 5
L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
Rozwiązaniem dla tego grafu i słowa W = "kto" jest 4 i jest osiągane przez ścieżkę 1 − 4 − 3. Inna
ścieżka realizująca to słowo to 1 − 4 − 2, ale ma koszt 8.
"""
from zad2testy import runtests
from queue import PriorityQueue
from math import inf

class VInfo:

    def __init__(self, vertex, letter_index):
        self.letter_index = letter_index
        self.vertex = vertex

    def is_last_letter(self, word):
        return self.letter_index == len(word) - 1

def relax(u, v, distance):
    if distance[v[0]] > distance[u] + v[1]:
        distance[v[0]] = distance[u] + v[1]
        return True
    return False

def dijkstra_algorithm(graph, W, letters):
    n = len(letters)

    queue = PriorityQueue()

    for i in range(n):
        if letters[i] == W[0]:
            queue.put(0, VInfo(i, 0))


    distance = [inf] * len(graph)
    visited = [None] * len(graph)

    for v in queue:
        distance[v] = 0

    while not queue.empty():
        dist, vinfo = queue.get()
        #dist, u = queue.get()
        if vinfo.is_last_letter(W):
            return distance

        for v in graph[vinfo.vertex]:
            if letters[v] == W[vinfo.letter_index + 1] and not visited[v[0]] and relax(vinfo.vertex, v, distance):
                queue.put((dist + v[1], VInfo(v[0], vinfo.letter_index + 1)))
        visited[vinfo.vertex] = VInfo(vinfo.vertex, vinfo.letter_index)

    return -1



def letters(G, W):
    letters, edges = G
    n = len(edges)
    new_graph = [[] for _ in range(len(letters))]
    for i in range(n):
        new_graph[edges[i][0]].append([edges[i][1], edges[i][2]])
        new_graph[edges[i][1]].append([edges[i][0], edges[i][2]])





G =[["k","k","o","o","t","t"] , [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]]

print(letters(G, [2]))

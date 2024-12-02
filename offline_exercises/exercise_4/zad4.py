#  Dominik Marek
"""
Dany jest nieskierowany graf G = (V, E), którego wierzchołki reprezentują punkty nawigacyjne nad
Bajtocją, a krawędzie reprezentują korytarze powietrzne między tymi punktami. Każdy korytarz
powietrzny ei ∈ E powiązany jest z optymalnym pułapem przelotu pi ∈ N (wyrażonym w metrach).
Przepisy dopuszczają przelot danym korytarzem, jeśli pułap samolotu różni się od optymalnego najwyżej o t metrów.
Graf jest dany w postaci listy krawędzi L = [(u1, v1, p1), (u2, v2, p2), ...(un, vn, pn)],
gdzie: ui, vi ∈ N to numery punktów nawigacyjnych, a pi to optymalny pułap przelotu. Ponieważ
graf jest nieskierowany na liście L umieszczono wyłącznie krotki, w których ui < vi
Proszę zaimplementować funkcję Flight(L,x,y,t), która sprawdza czy istnieje możliwość przelotu z zadanego punktu x ∈ V
do zadanego punktu y ∈ V w taki sposób, żeby samolot nigdy nie
zmieniał pułapu. Algorytm powinien być poprawny i możliwie jak najszybszy. Proszę oszacować
jego złożoność czasową.
Przykład
Dla danych wejściowych:
L = [(0,1,2000),(0,2,2100),(1,3,2050),(2,3,2300),
(2,5,2300),(3,4,2400),(3,5,1990),(4,6,2500),(5,6,2100)]
x = 0
y = 6
t = 60
Poprawną odpowiedzią jest: T rue, lot na pułapie 2045, wiedzie przez punkty 0 1 3 5 6.
W przypadku gdyby t = 50, odpowiedzią powinno być F alse.
"""
from zad4testy import runtests
from collections import deque

# Najpierw  z listy krawędzi tworzę graf w postaci listy adjacencji. Następnie iterujac przez akceptowalne wysokości z
# zakresu v[1] - t do v[1] + t +1, gdzie v[1] to pułap wysokośći między wierzchołkiem startowym a wierzchołkami v z
# nim połączonych, sprawdzam za pomocą bfs czy dla takiej wysokosci możliwy jest przelot x do y. Następnie jeśli dla
# dowolnej wykości z takiego zakresu uda sie nam przeleciec do x do y to zwracam True, w przecuwnym razie False.
# Złoźoność O((E+V)*2t)

def bfs(graph, x, y, t, current_height):
    n = len(graph)
    visited = [False]*n
    visited[x] = True
    dq = deque()
    dq.append(x)

    while dq:
        u = dq.popleft()
        if u == y:
            return True
        for v in graph[u]:
            if abs(v[1] - current_height) <= t and not visited[v[0]]:
                dq.append(v[0])
                visited[v[0]] = True

    return False


def Flight(L,x,y,t):

    num_vertex = max(v[1] for v in L)
    graph = [[] for _ in range(num_vertex+1)]


    for u,v, val in L:
        graph[u].append([v, val])
        graph[v].append([u, val])
    for v in graph[x]:
        for curr_height in range(-t+v[1], v[1] + t+1):
            if bfs(graph, x, y, t, curr_height):
                return True
    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(Flight, all_tests = True)

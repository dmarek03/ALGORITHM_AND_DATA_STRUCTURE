from egzP5btesty import runtests

"""
Szablon rozwiązania
Złożoność akceptowalna (1.5pkt):O(n^2)
Złożoność wzorcowa (+2.5pkt): O(nlogn), gdzie n to liczba sprzedanych biletów
Sieć kolejowa w Polsce w ostatnich latach rozwija się bardzo dynamicznie. W nowej ofercie
biletowej, która została dopuszczona do sprzedaży miesiąc temu, przedstawiona została nowa
mapa dostępnych połączeń. Jako, iż okazały się one atrakcyjne, na każde z nich został zakupiony
przynajmniej jeden bilet. PKP Intercity prowadzi bardzo dokładne statystyki, zapisując informacje
o każdym sprzedanym bilecie. Jako, że spółka posiada wolne środki, planuje potężny remont
jednego z dworców kolejowych, co na pewien okres wykluczy go zarówno z obsługi podróżnych,
jak i pociągów (w skrócie – żaden pociąg nie będzie mógł przez niego przejechać). Samo
tymczasowe wyłączenie dworca nie jest problemem, ponieważ uruchomiona zostanie zastępcza
komunikacja autobusowa, aczkolwiek nie może dojść do sytuacji, w której spowoduje to brak
możliwości przejazdu między innymi dworcami. W związku z tym firma musiała sporządzić listę
potencjalnych dworców, których remont spowoduje taki problem.
Zadanie polega na zaimplementowaniu funkcji:
koleje( B )
która obliczy liczbę dworców na wspomnianej liście, przy następujących założeniach:
 • Tablica B zawiera listę wszystkich sprzedanych biletów od czasu aktualizacji oferty. Każdy
bilet jest w postaci krotki (p, k) gdzie p to indeks stacji początkowej, a k to indeks stacji końcowej.
 • Dla celów oszacowania złożoności obliczeniowej należy przyjąć, że największy indeks stacji
jest mniejszy od łącznej ilości sprzedanych biletów.
Rozważmy następujące dane:
B = [
(3, 1), (0, 1), (4, 2),
(1, 2), (0, 1), (2, 4),
(2, 4), (0, 3), (2, 4),
(1, 0), (2, 1)
]
Wywołanie koleje( B ) powinno zwrócić wynik 2. Po zrzutowaniu każdego zakupionego
biletu jako połączenia (co widać na załączonym obrazku) można zauważyć, że zarówno usunięcie
dworca 1, jak i dworca 2 spowodowałoby problemy z przejazdem. Pozostałe dworce można w
bezpieczny sposób wyremontować
"""
# Complexity -> O(nlogn)
# Za pomocą algorytmu dfs znjdujemy punkty artykulacji w grafie i zwracamy ich ilość.
def find_articulation_points(graph):
    n = len(graph)
    low = [0] * n
    times = [0] * n
    is_art = [False] * n
    time = 0

    def dfs(root, u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time
        out_deg = 0

        for v in graph[u]:
            if v == parent:
                continue
            if not times[v]:
                out_deg += dfs(root, v, u) + u == root
                low[u] = min(low[u], low[v])
                if times[u] <= low[v]:
                    is_art[u] = True
            else:
                low[u] = min(low[u], times[v])

        return out_deg

    # Check all possible starting vertices as a graph doesn't have to be consistent
    for u in range(n):
        if not times[u]:
            is_art[u] = dfs(u, u, -1) > 1

    return [u for u in range(n) if is_art[u]]




# Ważna funkcja zeby pozybyc się wielokrotnych krawędzi
def undirected_unweighted_adj_list(edges_list: list[tuple[int, int]]) -> list[list[int]]:
    for i in range(len(edges_list)):
        if edges_list[i][0] > edges_list[i][1]:
            edges_list[i] = (edges_list[i][1], edges_list[i][0])
    edges_list.sort(key=lambda x: (x[0], x[1]))
    edges_list1 = set(edges_list)
    #print(f'{edges_list1=}')
    n = 0
    for e in edges_list1:
        n = max(n, e[1])
    n += 1

    graph = [[] for _ in range(n)]
    for edge in edges_list1:

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    return graph


def koleje ( B ):
    graph = undirected_unweighted_adj_list(B)
    articulation_points = find_articulation_points(graph)
    # print(*graph, sep='\n')
    # print(f'{articulation_points=}')
    return len(articulation_points)

runtests ( koleje, all_tests=True)
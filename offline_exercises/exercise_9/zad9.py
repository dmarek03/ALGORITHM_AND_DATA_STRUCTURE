from zad9testy import runtests

# def trip(M):
#
#     n, m  =  len(M),  len(M[0])
#
#     dp = [[-1]*m for _ in range(n)]
#
#
#     def dfs(x, y):
#
#         if dp[x][y] != -1:
#             return dp[x][y]
#
#         directions = [(0, 1), (1, 0) , (0, -1), (-1, 0)]
#         max_dist = 1
#
#         for dx, dy in directions:
#             nx =  x  + dx
#             ny = y + dy
#
#             if 0 <= nx < n and 0 <= ny < m and M[nx][ny] > M[x][y]:
#
#                 max_dist = max(max_dist, dfs(nx, ny) +1)
#
#         dp[x][y] = max_dist
#
#         return max_dist
#
#     max_path = 0
#
#     for i in range(n):
#         for j in range(m):
#             max_path = max(max_path, dfs(i, j))
#
#     print(*dp, sep='\n')
#
#     return max_path



"""
Mapa Gór Algorytmicznych to macierz o wymiarach m × n, której każde pole to liczba naturalna
stanowiąca wysokość danego obszaru (co ciekawe, każdy obszar ma inną wysokość). Student chce
się wybrać na wycieczkę po tym paśmie górskim, ale stawia kilka warunków: Po pierwsze, będąc na
danym polu może przejść wyłącznie na inne pole, które dzieli z nim jedną współrzędną (czyli może
się poruszać o jedno pole na prawo, lewo, w górą, lub w dół). Po drugie, może przejść wyłącznie
na pole o wyższej wysokości (wycieczka ma być wyzwaniem). Po trzecie, jego trasa ma być jak
najdłuższa, czyli ma przejść jak najwięcej pól, wliczając w to pole startowe (w końcu im więcej
czasu spędzie się w Górach Algorytmiki, tym lepiej). Student może wyruszyć z dowolnego wybranego
przez siebie pola (po prostu jakoś się tam znajdzie w sobotę rano; nikt nie wie jak to się dzieje).
Zadanie polega na implementacji funkcji:
trip( M )
która na wejściu otrzymuje mapę Gór Algorytmicznych M i zwraca największą liczbę pól, które
może odwiedzić student.
"""

#Początkowo towrzę tablicę dp o rozmiarze n x m wypełnioną jednykami, w której będę przechowywał długości poszczególnych tras.
# Następnie tworzę posortowaną względem wysokosći tablicę krotek postaci (wysokosć , indeks wiersza, indeks kolumny),
# która przechowuje komórki z tablicy M.Kolejno iteruje przez tak przygotowaną listę i dla każdej komórki oblicza 4
# nowe współrzędne odpowiadające możliwym kierunkom ekspansji, następnie sprawdzam czy zgodnie z warunkami zadania
# możemy przejść na pole o nowych współrzędnych.Jeśli tak to aktualizuję wartość w tablicy dp oraz długość najdłuższej ściezki.
# Finalanie zwracam longest_path, która przechowuje długość najdłużeszj możliwej wyprawy
# Złożoność O(nm)

def trip(M):
    if not M or not M[0]:
        return 0

    m, n = len(M), len(M[0])
    dp = [[1] * n for _ in range(m)]  # Inicjalizacja dp, minimalna trasa to 1 (samo pole)

    # Tworzymy posortowaną względem wysokości listę wszystkich pól z ich współrzędnymi i wysokościami
    cells = sorted([(M[i][j], i, j) for i in range(m) for j in range(n)])



    # Definiujemy kierunki poruszania się: prawo, dół, lewo, góra
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    longest_path = 1

    for height, x, y in cells:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and M[nx][ny] > height:
                dp[nx][ny] = max(dp[nx][ny], dp[x][y] + 1)
                longest_path = max(longest_path, dp[nx][ny])


    return longest_path



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = 1 )

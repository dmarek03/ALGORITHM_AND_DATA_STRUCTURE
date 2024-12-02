from egz2btesty import runtests
from math import inf

# Dominik Marek
# Aby rozwiązać zadanie tworzę tablicę dp o rozmiarze n x m, która będzię przechowywać minimalne sumy odległosći
# biurowców od początku do i-tego, zakładając ze i-ty biurowiec ma j-tą działkę.
# Początkowo wypełniam tablice dp wartościami inf oraz dla pierwszego wiersza znajduje jego odległosći od kolejnych
# działek.Następnie iterując po biurowcach począwszy od pierwszego tworzę zmienną min_dist = dp[i-1][i-1]. Następnie
# dla każdego biurowca obliczam minimalną odległosć od każdej działki jak sumę minimalnej odległości z poprzedniego wiersza
# i wartości bezwzględnej różnicy między współrzędną biurowca X[i] a współrzędną działki Y[j]. Kolejno aktualizuje
# min_dist jako minimum między obecną wartością min_dist a minimalną sumą dla  wcześniejszych biurowców, z których
# ostatni ma działke na pozycji j. Finalanie zwracam miniumum z ostatniego wiersza tablicy dp , co jest rozwiązaniem
# naszego zadania.
# Złożoność obliczeniowa to O(n*m)-> wypełnienie tablicy o rozmiarze n x m



def parking(X, Y):
    n = len(X)
    m = len(Y)

    dp = [[inf] * m for _ in range(n)]

    for j in range(m):
        dist = abs(X[0] - Y[j])
        dp[0][j] = dist

    if n <= 10:
        print(*dp, sep='\n')

    for i in range(1, n):
        min_dist = dp[i - 1][i - 1]
        for j in range(i, m):
            dp[i][j] = min_dist + abs(X[i] - Y[j])
            if n <= 10:
                print(f'{min_dist=}')
                print(f'{i=}')
                print(f'{j=}')
                print(f'{abs(X[i] - Y[j])=}')
                print(f'{dp[i][j]=}')
                print(f'{dp[i - 1][j]=}')
                print(*dp, sep='\n')
            min_dist = min(min_dist, dp[i - 1][j])
    if n <= 10:
        print(*dp, sep='\n')

    return min(dp[n-1])



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=False)

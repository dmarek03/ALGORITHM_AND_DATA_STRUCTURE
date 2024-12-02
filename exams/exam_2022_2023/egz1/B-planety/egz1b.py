# Algorytm tworzy tablice kosztow pobytu na danej planecie i posiadając b paliwa i wypelnia ja wartosciami
# nieskonczonymi poza polem 0,0 (bo koszt przebywania na planecie 0 z 0 paliwa wynosi 0). Kazdy wiersz jest wypelniany
# wartosciami minimalnymi kosztu przebywania na planecie i posiadajac b paliwa, obliczanymi nastepujaco:
# Wartoscia pola jest minimum z opcji tankowania na obecnej planecie (za obecny koszt paliwa), badz dotarcia z nadmiarem
# paliwa z poprzedniej planety (tylko jesli jest to mozliwe, tj. nie wymaga tankowania ponad E). Nastepnie sprawdzana
# jest mozliwosc teleportu, wiec pole wskazywane przez cel teleportu, jest nadpisywane wartoscia mniejsza z obecnie
# znajdującej sie na polu, badz wartosci pola i + koszt teleportu. Wynikiem jest koszt dotarcia do planety i z pustym
# bakiem, co jest najtansza opcja, znajdujacy sie w polu F[n-1][0]. Algorytm ma zlozonosc obliczeniową O(nE), gdyz
# jednokrotnie przechodzi przez tablice F o wymiarach n na E.

from egz1btesty import runtests
from math import inf


def planets(D, C, T, E):
    n = len(D)
    dp = [[inf for _ in range(E + 1)] for _ in range(n)]

    dp[0][0] = 0

    for i in range(n):
        i_cost = C[i]
        distance = 0
        if i > 0:
            distance = D[i] - D[i - 1]
            # Wypełnianie tablicy dla pierwszej kolumny -> bierzemy minium z obecnej wartości i kosztu dojechania na
            # poprzednią planetę z nadmiarową ilością paliwa równą odległośći miedzy wcześniejsza a obecną planetą.
            dp[i][0] = min(dp[i][0], dp[i - 1][distance])

        for b in range(1, E + 1):
            # Dla każej planety i danej ilości paliwa po dojechaniu na nią znajdujemy minimum z obecnej wartości tego
            # pola w tablicy oraz  kosztu dojechania na tę plantę z o jeden mniejsza ilością paliwa plus koszt
            # zatankowania jedngo litra paliwa na obecnej planecie
            dp[i][b] = min(dp[i][b], dp[i][b - 1] + i_cost)

            if i > 0 and b + distance <= E:
                # Dla każdej planety poza początkową sprawdzamy czy od obecnej wartości bardziej opłaca się przylecieć
                # na nią z planety wcześniejszej z nadmiarową ilością paliwa, jeśli pozwala na to pojemność baku.
                dp[i][b] = min(dp[i][b], dp[i - 1][b + distance])

        # Sprawdzamy mozliwosc teleportu, wiec pole wskazywane przez cel teleportu, jest nadpisywane wartoscia mniejsza
        # z obecnie znajdującej sie na polu, badz wartosci pola i + koszt teleportu
        t_dest, t_cost = T[i]
        dp[t_dest][0] = min(dp[t_dest][0], dp[i][0] + t_cost)

    print(*dp, sep='\n')

    return dp[n - 1][0]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = 1)

d = [0, 5, 10, 20]
c = [2, 1, 3, 8]
t = [(2, 3), (3, 7), (2, 1), (3, 10)]
e =  10

print(planets(d, c, t, e))
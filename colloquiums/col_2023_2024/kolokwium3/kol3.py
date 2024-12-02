from kol3testy import runtests
from math import inf

#Dominik Marek
# W celu rozwiazania zadania początkowo sprawdzam czy suma wszystkich jabłek w sadzie jest podzielna przez m,
# jeśli tak to zwracam zero, co oznacza, że nie trzeba wycinac żadnego drzewa.W innym przypadku tworzę tablicę dp
# o rozmiarze m, gdzie każdy element dp[j] reprezentuje minimalną liczbę drzew, które trzeba wyciąć, aby pozostała suma
# jabłek na dzewach dzieliła się przez m. Początkowo wszystkie wartości dp[j] ustawiamy na nieskończoność , z wyjątkiem
# dp[0], które jest zerem.Iterujemy przez kolejne wartośći jabłek na drzewach, a następnie tworzymy kopię tablicy dp.
# Dla każdego możliwego stanu j w dp, aktualizujemy wartość new_dp[(j + apples) % m],jak minimum z
# new_dp[(j + apples_num) % m oraz dp[j] + 1 aby odzwierciedlić minimalną liczbę drzew potrzebną do osiągnięcia reszty
# (j + apples) % m.Po zakońćzeniu się wewnętrzenj pętli aktualizuję tablicę dp jak new_dp.
# Na koniec zwracamy wartość dp[total_sum % m] jeśli nie jest ona nieskończonością, wpp  zwracamy n  czyli wycinamy
# wszystkie drzewa. Dp[total_sum % m] reprezentuje  minimalną liczbę drzew do wycięcia, aby suma jabłek
# na pozostałych drzewach była podzielna przez m.
# Złożonośc obliczeniowa : O(nm) - > O (7n^2)  -> O(n^2)
# Złożoność pamieciowa: O(m)
# """



def orchard(T, m):
    n = len(T)
    total_apple_count = sum(T)

    if total_apple_count % m == 0:
        return 0


    dp = [inf] * m
    dp[0] = 0
    dp_2 = [[inf]*m for _ in range(n+1)]
    dp_2[0][0] = 0


    for apples_num in T:
        new_dp = dp.copy()
        #print(f'{dp=}')
        for j in range(m):
            #if total_apple_count < 100:
                # print(f'{(j + apples_num) % m=}')
                # print(f'{dp[j]=}')
                # print(f'{ new_dp[(j + apples_num) % m]=}')
            new_dp[(j + apples_num) % m] = min(new_dp[(j + apples_num) % m], dp[j] + 1)
        dp = new_dp


    for i in range(1, n+1):

        for j in range(m):
            dp_2[i][(j+T[i-1])%m] =  min(dp_2[i][(j+T[i-1])%m], dp_2[i-1][j]+1)
            dp_2[i][j] =  min(dp_2[i][j], dp_2[i-1][j])


    res =  min(dp_2[i][total_apple_count % m] for i in range(n))


    return dp_2[n][total_apple_count % m] if dp_2[n][total_apple_count % m] != inf else n


runtests(orchard, True)
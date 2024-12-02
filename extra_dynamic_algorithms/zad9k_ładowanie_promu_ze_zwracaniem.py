from zad9ktesty import runtests
# Complexity O(n*l1*l2)
# Tworzymy tablicę która przechowuje ilość pojazdów znajdujących się na górnym i na dolnym pokładzie w momencie
# rozpatrywania i-tego pojazdu. Następnie odtwarzając kroki rekurencji dodajemy i-ty pojazd albo do górnego albo do
# dolnego pokładu, w zależnośći od tego, który wynik był bardziej optymalny. Finalnie sprawdzamy na którym pokładzie
# znajduje się ostatni pokład i zwracamy listę aut, które się na nim znajdują.
from math import inf

def f(tab, i, l1, l2, dp):
    if i > len(tab)-1:
        return 0

    if dp[i][l1][l2] != -1:
        return dp[i][l1][l2]

    if tab[i] > l1 and tab[i] > l2:
        dp[i][l1][l2] = 0
        return 0

    if tab[i] > l1:
        dp[i][l1][l2] = f(tab, i + 1, l1, l2 - tab[i], dp) + 1

    elif tab[i] > l2:
        dp[i][l1][l2] = f(tab, i + 1, l1 - tab[i], l2, dp) + 1

    else:
        dp[i][l1][l2] = max(f(tab, i + 1, l1, l2 - tab[i], dp), f(tab, i + 1, l1 - tab[i], l2, dp)) + 1

    return dp[i][l1][l2]


def prom(P, l1, l2):

    n = len(P)
    dp = [[[-1 for _ in range(l2 + 1)] for _ in range(l1 + 1)] for _ in range(n)]
    w = f(P, 0, l1, l2, dp)

    i = 0
    sol = []
    sol2 = []

    while i < n and (l1 >= P[i] or l2 >= P[i]):
        if P[i] > l1:
            w1 = 0
            w2 = 1

        elif P[i] > l2:
            w1 = 1
            w2 = 0
        else:
            w1 = f(P, i + 1, l1 - P[i], l2, dp)
            w2 = f(P, i + 1, l1, l2 - P[i], dp)

        if w1 > w2:
            sol.append(i)
            l1 -= P[i]
        else:
            sol2.append(i)
            l2 -= P[i]
        i += 1

    return sol if w-1 in sol else sol2


runtests(prom)


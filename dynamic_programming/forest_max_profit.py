"""
Ten sposób jest nieco prostszy i lepszy,bo zużywa mniej (stałą ilość) pamięci.Tym razem definiujemy funkcję następująco:
f(i) - maksymalny zysk, jaki uzyksamy, ścinając drzewa spośród tych, które leżą na indeksach 1, 2,..., i-1, i
"""
# Black Forest to las rosnący na osi liczbowej gdzieś w południowej Anglii. Las składa się z n drzew
# rosnących na pozycjach 0, ..., n−1. Dla każdego i ∈ {0, ..., n − 1} znany jest zysk c[i], jaki można
# osiągnąć ścinając drzewo z pozycji i. John Lovenoses chce uzyskać maksymalny zysk ze ścinanych drzew,
# ale prawo zabrania ścinania dwóch drzew pod rząd. Proszę zaproponować algorytm, dzięki któremu John
# znajdzie optymalny plan wycinki.



def max_profit(tab :list[int]) -> int:
    n = len(tab)
    if not n:
        return 0
    if n < 3:
        return max(tab[0], tab[1])

    f1 = max(tab[0], tab[1])
    f2 = tab[0]
    for i in range(2, n):
        print(f'{f1=}')
        print(f'{f2=}')
        f1, f2 = max(f2 + tab[i], f1), f1
    return f1


def deforestation(C):
    DP = [0] * len(C)
    DP[0] = C[0]
    DP[1] = max(C[0], C[1])
    for i in range(2, len(DP)):
        DP[i] = max(DP[i - 2] + C[i], DP[i - 1])
    return DP[-1]

T = [8, 12, 3, 4, 7, 1, 2, 10]

print(max_profit(T))
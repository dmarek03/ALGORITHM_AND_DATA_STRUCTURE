"""
Dany jest zbiór punktów X = {x1, x2, ..} na prostej .Proszę podac algorytm , który znajdje minimalną liczbę przedziałów
dokmniętych , potrzebnych do pokrycia wszytskich punktów z X
"""


def points(X):
    n = len(X)
    X.sort()
    start = X[0]
    cnt = 0
    for i in range(1, n):
        if X[i] >  X[start] + 1:
            start = i
            cnt += 1

    return cnt


"""
Chcać położyć przedział wsytrzyumujemy się do momentu aż natrafimy na punkt na osi, gdyż będzie to rozwiązanie nie gorsze
"""


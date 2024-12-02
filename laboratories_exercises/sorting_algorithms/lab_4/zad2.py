"""
Sortujemy n  liczb, gdzie mamy logn różnych liczb
Rozwiązanie 1:
1) Mamy tablic o dłogości sufit z logn , gdzie trzymam posortowane liczby, które już wystąpiły w tablicy
2) Jeśli chcemy wstawić do tablicy to za pomocą binary search sprawdzamy czy jest juz w tablicy,
   jeśli nie to go wstawiamy

Rozwiązanie 2:
1) Mamy posortowaną tablicę uniq
2) Tworzymy tablicę liczników, w której zliczamy ile razy wystąpiła dana liczba
3) Robimy quicker_sort -> dzielimy tablicę na 3 częsci [< pivot, pivot, > pivot] sortujemy tylko częśc mniejszą i większą
ex: T = [3.9, 5.4, 2.2, 5.4,  3.9, 9.6, 1.4, 2.2]
    uniq : [1.4, 2.2, 3.9, 9.6]
    cnt:    [1,   2,   2,   1]

"""


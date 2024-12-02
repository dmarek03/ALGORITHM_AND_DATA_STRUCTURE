"""
Struktura , która pozwala na wstawianie elementów (insert) oraz usuwanie mediany z listy (remove_median),
operacje mają działąć w czasie  logarytmicznyn:

1.Tworzymy dwa kopce:
a) K1 - elementy mniejsze niż mediana -> max_Heap
b) M - mediana
b) K2 - elemnty większe niż mediana -> min_Heap

2.
a ) Jeśli wstawiana wartość jest mniejsza od mediany to wstawiamy ja do K1, i patrzymy czy liczbe elementów w Kopcach
    jest równa, jeśli nie to naprawiamy kopce.
b) Jeśli wstawiana wartość jest wieksza od mediany to wstawiamy ją do K2 i jesli jest potrzeba to napriawiamy kopce

3.
a) Jeśli mamy nie parzystą liczbę elementów to po prostu usuwamy medianę
b) Gdy mamy parzystą liczbę elementów to usuwamy korzenie z obu kopców.
"""


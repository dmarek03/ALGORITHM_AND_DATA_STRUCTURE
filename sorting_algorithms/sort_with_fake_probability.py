"""
[2pkt.] Zadanie 3.
Szablon rozwiązania: zad3_strong_string.py
Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane z pewnego rozkładu losowego.
Ten rozkład mamy zadany jako k przedziałów
[a1, b1],[a2, b2], . . . ,[ak, bk] takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci
,
a liczba z przedziału jest wybierana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić, liczby ai
, bi są liczbami naturalnymi ze zbioru {1, . . . , N}. Proszę zaimplementować
funkcję SortTab(T,P) sortująca podaną tablicę. Pierwszy argument to tablica do posortowania a
drugi to opis przedziałów w postaci:
P = [(a1, b1, c1), (a2, b2, c2), . . ., (ak, bk, ck)].
Na przykład dla wejścia:
P = [(1,5, 0.75) , (4,8, 0.25)]
T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
po wywołaniu SortTab(T,P) tablica T powinna być postaci:
T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
Algorytm powinien być możliwie jak najszybszy. Proszę podać złożoność czasową i pamięciową
zaproponowanego algorytmu
"""

# Prawdopoodobieństowo to fejk !!!!!!!!!!!!!!!!!!!
# Bo i tak z każdego przedziału mogą być wszystkie albo żadne wartośći


def partition_2(array: list[float], l: int, r: int) -> int:

    pivot = array[r]
    i = l-1

    for j in range(l, r):
        if array[j] <= pivot:
            array[j], array[i+1] = array[i+1], array[j]
            i += 1

    array[i+1], array[r] = array[r], array[i+1]

    return i + 1


def quick_sort(array: list[float], l: int, r: int):
    while l < r:
        pos = partition_2(array, l, r)
        if pos - l <= r - pos:
            quick_sort(array, l, pos-1)
            l = pos+1
        else:
            quick_sort(array, pos, r)
            r = pos - 1


def sort_tab(T, P):
    n = len(T)
    quick_sort(T, 0, n-1)


T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
P = [(1,5, 0.75), (4,8, 0.25)]
sort_tab(T, P)
print(T)


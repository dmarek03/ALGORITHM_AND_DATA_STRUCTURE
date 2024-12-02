"""
Zadanie 1.
Szablon rozwiązania: zad1.py
Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
podać złożoność czasową i pamięciową zaproponowanego algorytmu.
Przykład. Dla tablicy:
T = [
      [ 2, 3, 5],
      [ 7,11,13],
      [17,19,23]
    ]
wynikiem jest, między innymi tablica:
T =  [
       [13,19,23],
       [ 3, 7,17],
       [ 5, 2,11]
       ]
"""
from median_test import random_tests
from random import randint


def create_matrix(size: int, min_val: int, max_val: int) -> list[list[int]]:
    return [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]


def partition(array: list[int], left: int, right: int) -> int:

    pivot = array[right]
    i = left-1

    for j in range(left, right):
        if array[j] <= pivot:
            array[i+1], array[j] = array[j], array[i+1]
            i += 1
    array[i+1], array[right] = array[right], array[i+1]

    return i+1


def quick_select(array: list[int], left: int, right: int, x: int) -> int:

    if left == right:
        return array[left]

    pos = partition(array, left, right)

    if pos == x:
        return array[pos]

    elif pos > x:
        return quick_select(array, left, pos-1, x)

    else:
        return quick_select(array, pos+1, right, x)


def Median(T):
    n = len(T)
    tmp_tab = [t for row in T for t in row]


    pos = n * (n - 1) // 2
    quick_select(tmp_tab, 0, n**2-1, pos+n-1)
    print(f'{tmp_tab=}')
    quick_select(tmp_tab, 0, n**2-1, pos)
    print(f'{tmp_tab=}')
    below_diagonal = tmp_tab[:pos]
    diagonal = tmp_tab[pos: pos + n]
    above_diagonal = tmp_tab[pos + n:]
    # print(f'{below_diagonal=}')
    # print(f'{diagonal=}')
    # print(f'{above_diagonal=}')
    # print(f'{len(below_diagonal)=}')
    # print(f'{len(diagonal)=}')
    # print(f'{len(above_diagonal)=}')

    for i in range(n):
        for j in range(n):
            if i < j:
                T[i][j] = above_diagonal[0]
                del above_diagonal[0]

            if i > j:
                T[i][j] = below_diagonal[0]
                del below_diagonal[0]

            if i == j:
                T[i][j] = diagonal[0]
                del diagonal[0]

    return T


# Przykład użycia
T = [
    [2, 3, 5],
    [7, 11, 13],
    [17, 19, 23]
]

T1 = create_matrix(5, 0, 9)
result = Median(T1)
random_tests(Median, samples=25, size=(1, 50))



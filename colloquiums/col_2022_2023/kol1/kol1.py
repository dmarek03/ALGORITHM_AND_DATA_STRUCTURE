# DOMINIK MAREK
"""
Korzystając z algorytmu quick_select, który znajduję k-największą wartość w danym przedziale, przechodzę po elemnetach
tablicy dopóki i + p < n (n - rozmiar tablicy) i za każdym razem znajduję k największy element z przedziału od i od i+p,
a następnie dodaję go do sumy, którą ostatecznie zwracam. Złożoność algorytmu to 0(nlogn).
"""

from kol1testy import runtests


def partition(array: list[int], left: int, right: int) -> int:
    pivot = array[right]
    i = left
    j = right-1

    while i < j:
        while i < right and array[i] < pivot:
            i += 1

        while j >= left and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i


def quick_select(array, left, right, x):
    if left == right:
        return array[right]

    pos = partition(array, left, right)

    if pos == x:
        return array[pos]

    elif pos > x:
        return quick_select(array, left, pos-1, x)

    else:
        return quick_select(array, pos+1, right, x)


def ksum(T, k, p):
    n = len(T)
    sum1 = 0
    i = 0

    while i + p <= n:
        new_t = T[i:i+p]
        nn = len(new_t)
        sum1 += quick_select(new_t, 0, p-1, nn-k)
        i += 1
    return sum1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True)


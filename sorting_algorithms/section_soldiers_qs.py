"""
# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której podano wzrosty żołnierzy.
# Żołnierze zostaną ustawieni na placu w szeregu malejąco względem wzrostu. Proszę zaimplementować
# funkcję: section(T, p, q) która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q
# włącznie. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić
# 1-2 zdaniowy opis algorytmu oraz proszę oszacować jego złożoność czasową.
"""


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


def section(T, p, q):
    n = len(T)
    quick_select(T, 0, n-1, q)
    quick_select(T, 0, n-1, p)
    print(T)
    return T[p:q+1]


T = [37, 98, 175, 172, 143, 134, 172, 189, 210, 225, 179, 183, 152, 146]

print(section(T, 4, 6))
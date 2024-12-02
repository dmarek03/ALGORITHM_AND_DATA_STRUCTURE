"""
 Magiczne piątki.
Proszę zaimplementować algorytm "magiczne piątki", który dostaję na wejściu tablicę liczb naturalnych A oraz liczbę k
i zwraca liczbę , która po posortowaniu tablicy A była by pod indeksem k. Można założyć ,że wszystkie liczby w tablicy A
są parami różne . Stworzona funkcja powinna nazywać się : linearselect(A, k).
"""

from random import randint, shuffle, seed
from math import ceil


def median(T, p, r):
    for i in range(p+1, r):
        key = T[i]
        j = i-1
        while j >= p and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return (p+r)//2


def partition(T, left, right, pivot):
    T[pivot], T[right] = T[right], T[pivot]
    i = left
    for j in range(left, right):
        if T[j] < T[right]:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[right] = T[right], T[i]
    return i


#[0 1 -1 2 3 4 5 G 8 A F 7 K B E 6 9 C]


def median_medians(A, left, right):
    size = right - left + 1
    index = start = left
    end = right

    for i in range(start, end, 5):
        if i+5 > right:
            q = median(A, i, right)
        else:
            q = median(A, i, i + 5)
        A[index], A[q] = A[q], A[index]
        index += 1

    if ceil(size / 5) < 5:
        pivot = median(A, start, ceil(size / 5) + start)
    else:
        pivot = median_medians(A, start, ceil(size / 5) + start)
    q = partition(A, start, end, pivot)
    return q


def select(T, p, r, k):
    median_idx = median_medians(T, p, r)
    if median_idx == k:
        return T[k]
    elif median_idx < k:
        return select(T, median_idx+1, r, k)
    else:
        return select(T, p, median_idx-1, k)


def linearselect(A, k):
    value = select(A, 0, len(A)-1, k)
    return value


seed(42)

size = 19
for i in range(size):
    A = list(range(size))
    shuffle(A)
    print(A)
    x = linearselect(A, i)
    print(f'{x=}')
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")
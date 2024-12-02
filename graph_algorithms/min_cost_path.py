from min_cost_pah_testy import runtests
from queue import PriorityQueue
from math import inf
"""
Dana jest tablica T zawierająca N liczb naturalnych. Z pozycji a można przeskoczyć na pozycję b
jeżeli liczby T[a] i T[b] mają co najmniej jedną wspólną cyfrę. Koszt takego skoku równy ∣T[a] −
T[b]∣. Proszę napisać funkcję, która wyznacza minimalny sumaryczny koszt przejścia z najmniejszej
do największej liczby w tablicy T. Jeżeli takie przejście jest niemożliwe, funkcja powinna zwrócić
wartość -1.

"""

"""Without any data structures (except mapped numbers)"""


def mapped_numbers(tab):
    n = len(tab)
    numbers = [[]] * n
    for i in range(n):
        digits = [False] * 10
        num = tab[i]
        while num:
            idx = num % 10
            digits[idx] = True
            num //= 10
        numbers[i] = digits
    return numbers


def have_common_digit(tab, i, j):
    # for k in range(10):
    #     if tab[i][k] and tab[j][k]:
    #         return True
    return True if any(tab[i][k] and tab[j][k] for k in range(10)) else False


def minmax(T):
    n = len(T)
    min_i = max_i = n - 1
    for i in range(1, n, 2):
        if T[i] > T[i - 1]:
            if T[i] > T[max_i]:     max_i = i
            if T[i - 1] < T[min_i]: min_i = i - 1
        else:
            if T[i - 1] > T[max_i]: max_i = i - 1
            if T[i] < T[min_i]:     min_i = i
    return min_i, max_i


def dijkstra(T, M, s, t):
    n = len(T)
    weights = [inf] * n
    pq = PriorityQueue()
    pq.put((0, s))

    while not pq.empty():
        min_w, u = pq.get()
        # We will find the minimum total weight path only once so the
        # code below this if statement will be executed only once
        if min_w < weights[u]:
            weights[u] = min_w
            # Break a loop if we found a shortest path to the specified
            # target
            if u == t:
                break
            # Add all the neighbours of the u vertex to the priority queue
            for v in range(n):
                if weights[v] == inf and have_common_digit(M, u, v):
                    pq.put((weights[u] + abs(T[u] - T[v]), v))
    print(f'{weights=}')

    return weights[t] if weights[t] < inf else -1


def min_cost(T):
    T.sort()
    #min_idx, max_idx = minmax(T)
    M = mapped_numbers(T)
    return dijkstra(T, M, 0, len(T)-1)

runtests(min_cost)

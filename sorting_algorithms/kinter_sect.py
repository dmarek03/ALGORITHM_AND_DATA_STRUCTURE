# Dany jest zbiór przedziałów A = {(a[0], b[0]), ..., (a[n−1], b[n−1])}. Proszę zaimplementować funkcję:
# def kintersect(A, k):
#     ...
# która wyznacza k przedziałów, których przecięcie jest jak najdłuższym przedziałem. Zbiór A jest
# reprezentowany jako lista par. Końce przedziałów to liczby całkowite. Można założyć, że k ≥ 1 oraz
# k jest mniejsze lub równe łącznej liczbie przedziałów w A. Funkcja powinna zwracać listę numerów
# przedziałów, które należą do rozwiązania.
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
from kintersect_testy import runtests
# Tworzymy tablicę krotek postaci indeks z początkowej tablicy i współrzędne przedziału. Tę tablicę sortujemy w
# porządku malejącym po końcach przedziałów.Następnie  iterując po przedziałach , ustawiamy i-ty przedział jako
# początkowy i k-1 kolejnych takich , których przecięcie jest największe. Na koniec zwracamy indeksy  k przedziałów z
# początkowej tablicy, których przecięcie jest największe.
# Złożoność O(n^2)


# def kintersect(array, k):
#     n = len(array)
#     interval = [(i, array[i][0], array[i][1]) for i in range(n)]
#     interval.sort(key=lambda x: -x[2])
#     print(f'{interval=}')
#     max_length = 0
#     if k == 1:
#         result = [0]
#         for i in range(n):
#             if interval[i][2] - interval[i][1] > max_length:
#                 max_length = interval[i][2] - interval[i][1]
#                 result[0] = interval[i][0]
#         return result
#     result = []
#     for i in range(n):
#         if n > 50:
#             break
#         current = [interval[i][0]]
#         for j in range(n):
#             if i != j and interval[j][1] <= interval[i][1] < interval[j][2]:
#                 current.append(interval[j][0])
#                 print(f'{i=}')
#                 print(f'{j=}')
#                 print(f'{current=}')
#                 if len(current) == k:
#                     print(f'{i=}')
#                     print(f'{j=}')
#                     print(f'{current=}')
#                     print(f'{interval[j][2]} - {interval[i][1]} = {interval[j][2] - interval[i][1]}')
#                     print(f'{interval[i][2]} - {interval[i][1]} = {interval[i][2] - interval[i][1]}')
#                     # Wiemy, że pod i-tym indeksem mamy przedział,który zaczyna się najpóźniej a pod j-tym indeksem
#                     # przedział, który kończy się najwcześniej, zatem długością przecięcia się naszych zbiorów, bedzie
#                     # minimum z róźnicy pomiędzy końcem j-tego przedziału a początkiem i- tego, a długośćią i-tego
#                     # przedziału
#                     actual_length = min(interval[j][2] - interval[i][1], interval[i][2] - interval[i][1])
#                     if actual_length > max_length:
#                         max_length = actual_length
#                         result = current
#                     break
#
#     return result

import heapq


def kintersect(range_, k):
    n = len(range_)
    asc = [(range_[idx][0], range_[idx][1], idx) for idx in range(n)]

    # Sorting ranges in non-descending order
    asc.sort(key=lambda x: x[0])
    print(asc)

    # Min-heap to store k largest ending
    # point of ranges seen so far
    pq = []

    ans = 0
    result_indices = []

    for i in range(n):
        # Ending point of ith range
        heapq.heappush(pq, (asc[i][1], asc[i][2]))  # Tuple (ending_point, original_index)

        # Ranges having zero intersection
        while pq and pq[0][0] < asc[i][0]:
            heapq.heappop(pq)

        # Size up to k
        while len(pq) > k:
            heapq.heappop(pq)

        # Update answer and indices
        if len(pq) == k:
            if n < 20:
                print(f'{pq=}')
            # Długość ta jest obliczana poprzez różnicę między największym końcem przedziału w min-heapie a
            # początkiem aktualnego przedziału
            current_length = pq[0][0] - asc[i][0] + 1
            print(f'{pq[0][0]=}')
            print(f'{asc[i][0]=}')
            if current_length > ans:
                ans = current_length
                result_indices = [idx for _, idx in pq]


    return result_indices


runtests(kintersect)
"""
[2pkt.] Zadanie 3. Szablon rozwiązania: zad2_snow.py Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a^x
, gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i zwraca tablicę z wynikami
eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność
zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
def fast_sort(tab, a):

"""
import math
import random
from fast_sort_test import runtests


def fast_sort(tab, a):
    n = len(tab)

    buckets = []
    for i in range(n):
        buckets.append([])

    for t in tab:
        # dividing elements to proper buckets(using log to get x value)

        buckets[math.floor(math.log(t, a) * n)].append(t)

    for bucket in buckets:
        insertion_sort(bucket)

    print(f'{buckets=}')

    # concatenation elements from buckets to final list
    return [b for bucket in buckets for b in bucket]


def insertion_sort(array: list[int]):

    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]

            j -= 1

a = 4
tab = [a**(random.random()) for i in range(20)]
print(tab)

print(fast_sort(tab, a))
runtests(fast_sort)




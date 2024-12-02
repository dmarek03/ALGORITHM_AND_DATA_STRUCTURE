"""
We have to sort array of natural numbers from range 1 to n^-1.
To achieve this goal with complexity O(n), we can use radix sort, that make use of
counting sort, which is stable algorythm.
"""


def counting_sort(tab, idx: int, max_range: int):
    n = len(tab)
    count_tab = [0 for _ in range(max_range+1)]
    sorted_tab = [0]*n

    for i in range(n):
        count_tab[tab[i][idx]] += 1

    for i in range(1, max_range+1):
        count_tab[i] += count_tab[i-1]

    for i in range(n-1, -1, -1):
        sorted_tab[count_tab[tab[i][idx]]-1] = tab[i]
        count_tab[tab[i][idx]] -= 1

    for i in range(n):
        tab[i] = sorted_tab[i]


tab = [[1, 2], [2, 4], [100, 3], [99, 1]]
counting_sort(tab, 0, 100)
print(tab)


def normalized_number(number: int, base: int):
    n_number = 0
    i = 1
    while number > 1:
        n_number += (number % base)*i
        i *= 10
        number /= base
    return n_number


def radix_sort(tab):
    n = len(tab)
    normalized_tab = [[p, p//n, p % n] for p in tab]
    print(normalized_tab)
    counting_sort(normalized_tab, 2, n)
    counting_sort(normalized_tab, 1, n)
    print(normalized_tab)
    return [t[0] for t in normalized_tab]

tab = [1, 3, 2, 5, 2, 4, 1,11, 6, 8, 9]
print(radix_sort(tab))


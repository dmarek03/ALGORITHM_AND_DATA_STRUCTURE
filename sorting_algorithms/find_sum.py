"""
# Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba
# z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie
# jak najszybszy. Proszę oszacować jego złożoność obliczeniową.

"""
from math import inf


def merge(tab, p: int, q: int, r: int):
    left_arr = tab[p:q+1]
    right_arr = tab[q+1:r+1]
    left_arr.append(inf)
    right_arr.append(inf)
    i, j, k = 0, 0, 0
    while i < j:
        if left_arr[i] < right_arr[j]:
            tab[k] = left_arr[i]
            i += 1

        else:
            tab[k] = right_arr[j]
            j += 1
        k += 1


def merge_sort(tab, p: int, r: int):
    if len(tab) <= 1:
        return tab
    elif p < r:
        m = (p + r) // 2
        merge_sort(tab, p, m)
        merge_sort(tab, m + 1, r)
        merge(tab, p, m, r)


def check_sum(tab: list[int], x: int) -> bool:

    n = len(tab)
    i = 0
    j = n-1
    while i < j:
        if tab[j] - tab[i] > x:
            i += 1

        if tab[j] - tab[i] < x:
            j -= 1

        if tab[j] - tab[i] == x:
            return True
    return False


def find_all_elements_sum(tab: list[int]) -> bool:
    n = len(tab)
    merge_sort(tab, 0, n-1)

    for t in tab:
        if not check_sum(tab, t):
            return False
        break
    return True


T = [0,0,0,1,2,1, 8, 4, ]
print(find_all_elements_sum(T))

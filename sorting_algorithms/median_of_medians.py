from random import shuffle, seed


def selection_sort(tab: list[int]):
    n = len(tab)

    for i in range(n):
        min_idx = i

        for j in range(i+1, n):
            if tab[min_idx] > tab[j]:
                min_idx = j
        if min_idx != i:
            tab[min_idx], tab[i] = tab[i], tab[min_idx]


def get_median(tab: list[int], left: int, right: int) -> int:
    selection_sort(tab)
    return (left + right)//2


def partition(tab: list[int], left: int, right: int) -> int:

    pivot = tab[left]
    i = left+1

    for j in range(left, right+1):
        if tab[j] < pivot:
            tab[i], tab[j] = tab[j], tab[i]
            i += 1

    tab[i-1], tab[left] = tab[left], tab[i-1]

    return i-1


def median_of_medians(tab: list[int], left: int, right: int, k: int) -> int:
    next_swap_idx = left

    while right-left >= k:

        for end_idx in range(left+k-1, right+1, k):
            curr_median_idx = get_median(tab, end_idx-k+1, end_idx)
            tab[curr_median_idx], tab[next_swap_idx] = tab[next_swap_idx], tab[curr_median_idx]
            next_swap_idx += 1

        if end_idx < right-1:
            remaining_median = get_median(tab, end_idx, right)
            tab[next_swap_idx], tab[remaining_median] = tab[remaining_median], tab[next_swap_idx]
            next_swap_idx += 1

        right = next_swap_idx - 1
        next_swap_idx = left

    last_median = get_median(tab, left, right)
    tab[last_median], tab[left] = tab[left], tab[last_median]
    return tab[left]


def linear_select(tab: list[int], k: int) -> int:
    n = len(tab)
    left = 0
    right = n-1

    while left <= right:
        median_of_medians(tab, left, right, 5)
        pivot_idx = partition(tab, left, right)
        if pivot_idx < k:
            left = pivot_idx + 1

        elif pivot_idx > k:
            right = pivot_idx - 1

        else:
            return tab[k]


seed(42)

size = 19
for i in range(size):
    A = list(range(size))
    shuffle(A)
    #print(A)
    x = linear_select(A, i)
    #print(f'{x=}')
    if x != i:
        print("Blad podczas wyszukiwania liczby", i)
        exit(0)

print("OK")



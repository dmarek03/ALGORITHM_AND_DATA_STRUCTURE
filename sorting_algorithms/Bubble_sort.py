"""
BUBBLE SORT
"""


def bubble_sort(array: list[int]):
    n = len(array)
    swapped = False

    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
        if not swapped:
            return


tab = [1]*10000
tab[500] = 3
bubble_sort(tab)
print(tab)


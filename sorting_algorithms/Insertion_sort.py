"""
INSERTION SORT
"""


def insertion_sort(array: list[int]):

    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
                print(array)


tab = [12,3,4,1,5,0]
insertion_sort(tab)
print(tab)

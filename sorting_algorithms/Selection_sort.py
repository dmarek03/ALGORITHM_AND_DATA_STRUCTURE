"""
SELECTION SORT
"""


def selection_sort(array: list[int]):

    n = len(array)

    for i in range(n):
        # set the minium index as i
        min_idx = i
        # starting the inner loop from the next element
        for j in range(i+1, n):
            # if the element of index j is lower than element of min_idx
            # we set the min_idx as j
            if array[j] < array[min_idx]:
                min_idx = j
        # finally after the inner loop we swap the element of index i with element of min_idx and vice versa
        if min_idx != i:
            array[i], array[min_idx] = array[min_idx], array[i]


tab = [3, 12, 4, 2, 0, 4, 1,1 ,2, 3]
selection_sort(tab)
print(tab)


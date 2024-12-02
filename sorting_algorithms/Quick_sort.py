"""
QUICK SORT
"""


def partition(array: list[int], left: int, right: int):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:
        while i < right and array[i] < pivot:
            i += 1

        while j >= left and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]
    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i


def partition_2(array: list[int], left: int, right: int):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[right] = array[right], array[i+1]
    return i + 1


def quick_sort(array: list[int], left: int, right: int):
    if len(array) < 2:
        return array

    if left < right:
        position = partition_2(array, left, right)
        quick_sort(array, left, position - 1)
        quick_sort(array, position + 1, right)


def quicksort2(array, left, right):
    while left < right:
        q = partition(array, left, right)
        if q - left <= right - q:
            quicksort2(array, left, q - 1)
            left = q + 1
        else:
            quicksort2(array, q, right)
            right = q - 1


def iterative_quicksort(T):
    S = []
    p = 0
    r = len(T) - 1
    S.append((p, r))
    while len(S) > 0:
        (p, r) = S.pop()
        if p < r:
            q = partition(T, p, r)
            if q - p > r - 1:
                S.append((p, q - 1))
                S.append((q + 1, r))
            else:
                S.append((q + 1, r))
                S.append((p, q - 1))
    return T



tab = [3,5,2,1,1,14,123,7,1]
quicksort2(tab, 0, len(tab) - 1)
print(tab)


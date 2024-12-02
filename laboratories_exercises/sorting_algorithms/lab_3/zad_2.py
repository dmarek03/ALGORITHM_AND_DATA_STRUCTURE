"""
Quick sort bez rekurencji
"""


def partition_2(array: list[int], left: int, right: int):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[right] = array[right], array[i+1]
    return i + 1


def iterative_quick_sort(tab, left, right):
    # Wkładamy na stos indeksu wyznaczające zakres sortowania
    stack = [(left, right)]
    while len(stack) > 0:
        (left, right) = stack.pop()
        if left < right:
            pos = partition_2(tab, left, right)

            if left < pos-1:
                stack.append((left, pos-1))

            if pos + 1 < right:
                stack.append((pos+1, right))


tab = [0, 4,2 , 1, 4, 2]
iterative_quick_sort(tab, 0, len(tab)-1)
print(tab)


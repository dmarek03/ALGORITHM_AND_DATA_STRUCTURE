"""
Quick_sort z maksymalnie logn zejść rekurencyjnych
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


def quick_sort(tab, left, right):
    while left < right:
        pos = partition_2(tab, left, right)
        if pos <= (left + right) // 2:
            quick_sort(tab, left, pos-1)
            left = pos + 1
        else:
            quick_sort(tab, pos+1, right)
            right = pos - 1

# Dominik Marek
from zad2testy import runtests


def partition(array: list[int], left: int, right: int) -> int:
    pivot = array[right]
    i = left
    j = right-1

    while i < j:
        while i < right and array[i] < pivot:
            i += 1

        while j >= 0 and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]

    return i


def quick_select(array: list[int], left: int, right: int, x: int) -> int:
    if left == right:
        return array[left]

    pos = partition(array, left, right)
    if x == pos:
        return array[pos]

    elif pos > x:
        return quick_select(array, left, pos-1, x)

    else:
        return quick_select(array, pos+1, right, x)


#

def ksum(T, k, p):
    if p == 1:
        return sum(T)
    n = len(T)
    total_sum = 0
    for i in range(n-p+1):
        tmp_array = T[i:i+p]
        total_sum += quick_select(tmp_array, 0, p-1, p-k)

    return total_sum


#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)

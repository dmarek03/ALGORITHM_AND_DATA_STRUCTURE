"""
2. Proszę zaimplementować funkcję:
int SumBetween(int T[], int from, int to, int n);
Zadaniem tej funkcji jest obliczyć sumę liczb z n elementowej tablicy T, które w posortowanej
tablicy znajdywałyby się na pozycjach o indeksach od from do to (włącznie). Można przyjąć, że
liczby w tablicy T są parami różne (ale nie można przyjmować żadnego innego rozkładu danych).
Zaimplementowana funkcja powinna być możliwie jak najszybsza. Proszę oszacować jej złożoność
czasową (oraz bardzo krótko uzasadnić to oszacowanie).

"""


def partition(array:list[int], left: int, right: int) -> int:
    pivot = array[right]
    i = left
    j = right-1

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


def quick_select(array: list[int], left: int, right: int, x: int) -> int:

    if left == right:
        return array[right]

    pos = partition(array, left, right)

    if pos == x:
        return array[pos]

    elif pos > x:
        return quick_select(array, left, pos-1, x)

    else:
        return quick_select(array,pos+1, right, x)


def sum_between(array: list[int], start: int, stop: int) -> int:
    n = len(array)
    quick_select(array, 0, n-1, stop)
    quick_select(array, 0, n-1, start)
    print(array)
    return sum(array[start:stop+1])


array = [1, 4, 2, 20, 4, 34, 6, 11, 0, 3, 3, 34, 1, 2,3 , 6]

print(array)
print(sum_between(array,3, 6))


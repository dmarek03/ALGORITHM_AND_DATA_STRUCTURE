# DOMINIK MAREK
# Jeśli po sortujemy elementy tablicy nierosnąco a następnie w pętli dopóki t[i] - i > 0 oraz indeks
# jest mniejszy od rozmiaru tablicy, będziemy dodawać kolejne elementy tablicy pomniejeszone odpowiednio o ilośc
# topniejącego śniegu to otrzymamy maksymalną, ilość śniegu, który można zebrać.
# Aby uzysakć optymalną złożoność to dopóki różnica między największym a najmniejszym elementem tablicy jest mniejsza
# n * (log(n)-2) , gdzie n to rozmiar tablicy, korzystam z counting sort a następnie w pętli dopóki ilość śniegu spod
# danego indeksu minus topniejący śnieg jest większa od zera ,znajduję największą sumę, zatem otrzymuję złożoność
# liniową O(2n + m), gdzie m to (max_val - min_val +1),gdy rozstrzał między wartośćiami elementów jest za duży, to aby
# uniknąć błędu z powodu przepełnienia pamięci, korzystam z funkcji max_heap() którą, tworzy prawidłwoy kopiec binarny,
# a następnie w funkcji get_max_sum1(), najpierw buduje kopiec z elementów tablicy, a następnie w pętli przechodząc po
# indeksach tablicy, jeżeli pierwszy element z kopca (największy) pominiejszony o ilość topniejącego śniegu jest większy
# od zera to dodaję go do sumy, i wywołuje funckję max_heap dla kopca o pomniejszonego o jeden element. Jeśli wartość
# spod elementu root_idx minus ilość stopniałego śniegu po i dniach jest mniejsza od zera to wychodzę z pętli i zwracam
# sumę zebranego śniegu.W tym przypadku otrzymuję złożoność  O(nlogn).Zatem dla odpowiednio małego przedziału wartości
# elementów mam złożonośc liniową , a dla pozostałych logarytmiczną.

from zad2testy import runtests
from math import log


def max_heap(array: list[int], heap_size: int, root_idx: int):
    largest = root_idx
    left = 2 * root_idx + 1
    right = 2 * root_idx + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != root_idx:
        array[largest], array[root_idx] = array[root_idx], array[largest]
        max_heap(array, heap_size, largest)


def get_max_sum1(array: list[int]) -> int:
    n = len(array)
    sum1 = 0
    for i in range((n // 2) - 1, -1, -1):
        max_heap(array, n, i)

    for i in range(n):
        if array[0] - i > 0:
            sum1 += array[0] - i
            array[n - i - 1], array[0] = array[0], array[n - i - 1]
            max_heap(array, n - i - 1, 0)

        else:
            break
    return sum1


def get_max_sum2(array):
    n = len(array)
    sorted_array = [0]*n
    range_max = max(array)
    range_min = min(array)
    interval = range_max - range_min + 1
    count_tab = [0]*interval

    for i in range(n):
        count_tab[array[i]-range_min] += 1

    for j in range(1, len(count_tab)):
        count_tab[j] += count_tab[j-1]
    sum1 = 0
    for k in range(n-1, -1, -1):
        sorted_array[count_tab[array[k]-range_min]-1] = array[k]
        count_tab[array[k] - range_min] -= 1

    for i in range(n):
        if sorted_array[n-i-1] - i > 0:
            sum1 += sorted_array[n-i-1] - i
        else:
            break
    return sum1


def snow(S):
    n = len(S)
    value_range = max(S) - min(S) + 1
    return get_max_sum2(S) if value_range < n * (log(n)-2) else get_max_sum1(S)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests=True)


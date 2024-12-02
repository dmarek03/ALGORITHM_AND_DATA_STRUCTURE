"""
[2pkt.] Zadanie 1. Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie jeden raz. Cyfra wielokrotna to
taka, która w liczbie występuje więcej niż jeden raz. Mówimy, że liczba naturalna A jest ładniejsza od liczby naturalnej
B jeżeli w liczbie A występuje więcej cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to
ładniejsza jest ta liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od 455,
liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne. Dana jest tablica T zawierająca liczby
naturalne. Proszę zaimplementować funkcję: pretty_sort(T) która sortuje elementy tablicy T od najładniejszych
do najmniej ładnych. Użyty algorytm powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy
opis algorytmu oraz proszę oszacować jego złożoność czasową.

"""


def count_single_mono_digits(number: int) -> list[int]:
    digits = [0] * 10
    while number > 0:
        digits[number % 10] += 1
        number //= 10

    single_cnt = 0
    mono_cnt = 0
    for d in digits:
        if d == 1:
            single_cnt += 1
        if d > 1:
            mono_cnt += d

    return [single_cnt, mono_cnt]


def counting_sort(array, pos: int):
    n = len(array)
    min_val = min(a[pos] for a in array)
    max_val = max(a[pos] for a in array)
    count_array = [0] * (max_val-min_val+1)
    sorted_array = [0]*n

    for i in range(n):
        count_array[array[i][pos]] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i-1]

    for i in range(n-1, -1, -1):
        sorted_array[count_array[array[i][pos]]-1] = array[i]
        count_array[array[i][pos]] -= 1
    print(sorted_array)
    for i in range(n):
        array[i] = sorted_array[n-i-1]


def pretty_sort(array: list[int]):

    new_t = [[t] + count_single_mono_digits(t) for t in array]

    for i in range(2, 0, -1):
        counting_sort(new_t, i)

    return [t[0] for t in new_t]


print((pretty_sort([12331,1, 2, 3,333, 223343221345424, 34, 1, 11122, 1, 2, 43,5342,  999])))

"""
Dany jest ciąg klocków (a1, b1), . . . (an, bn). Każdy klocek zaczyna się na pozycji ai i ciągnie się do pozycji bi.
Klocki mogą spadać w kolejności takiej jak w ciągu. Proszę zaimplementować funkcję tower(A), która wybiera możliwie
najdłuższy podciąg klocków taki, że spadając tworzą wieżę i żaden klocek nie wystaje poza którykolwiek z wcześniejszych
klocków. Do funkcji przekazujemytablicę A zawierającą pozycje klocków ai ,bi .Funkcja powinna zwrócić maksymalną
wysokość wieży jaką można uzyskać w klocków w tablicy A.
Przykład Dla tablicy A = [(1,4),(0,5),(1,5),(2,6),(2,4)] wynikiem jest 3, natomiast dla
tablicy A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)] wynikiem jest 2.
"""
from klockitesty import runtests


def binary_search(array: list[int], val: int, comparator: callable):
    left_idx = 0
    right_idx = len(array) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if comparator(val, array[mid_idx]):
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array


def longest_seq(array: list[int]):
    n = len(array)
    if len(array) < 2:
        return array

    top = []

    for i in range(n):
        # Dla każdego elementu wykonujemy wyszukiwanie binarne przy użyciu funkcji binary_search. Jeśli zwracany indeks
        # j jest równy długości tablicy top, to oznacza, że bieżący element array[i] jest większy niż wszystkie
        # poprzednie elementy w top, więc dodaje go do top. W przeciwnym razie aktualizuje element top[j] wartością
        # array[i].
        j = binary_search(top, array[i], lambda curr, prev: curr[0] >= prev[0] and curr[1] <= prev[1])
        if j == len(top):
            top.append(array[i])
        else:
            top[j] = array[i]

    return len(top)




def tower(tab: list[int]):
    return longest_seq(tab)





runtests(tower)

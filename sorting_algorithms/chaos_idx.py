"""
Mówimy,że tablica T ma wspołczynnik nieuporządkowania równy k (jest k-Chaotyczna), jeśli spełnione są dwa warunki:

1. tablicę można posortować niemalejąco przenosząc każdy element do elementu A[i] o co najwyżej k pozycji
(po posortowaniu znajduje się on na pozycji różniącej się od i o co najżej o k).

2. tablicy  nie da się posortować niemalęjąco przenosząc każdy element o mniej niż k pozycji.

Proszę zaproponować i zaimplementować algortym,, który otrzymuje na wejściu tablicę liczb rzeczywistych T i zwraca jej
współczynnik nieuporządkowania. Algorytm powinnien być jak najszybszy oraz używać jak najmniej pamięci. Algorytm należy
zaimplementować jako funkcję:

def chaos_index(T):
    ...

przyjmującą tablicę T i zwracającą liczbę całkowitą będącą wyznaczonym współczynnikiem nieuporządkowania.
"""


def partition(tab: list[tuple[int, float]], pos: int, left: int, right: int) -> int:

    pivot = tab[right]
    i = left
    j = right-1

    while i < j:
        while i < right and tab[i][pos] < pivot[pos]:
            i += 1

        while j >= left and tab[j][pos] >= pivot[pos]:
            j -= 1

        if i < j:
            tab[i], tab[j] = tab[j], tab[i]

    if tab[i][pos] > pivot[pos]:
        tab[i], tab[right] = tab[right], tab[i]

    return i


def quick_sort(tab: list[tuple[int, float]], pos: int, left: int, right: int):
    if left < right:
        position = partition(tab, pos, left, right)
        quick_sort(tab, pos, left, position-1)
        quick_sort(tab, pos, position+1, right)


def chaos_index(tab: list[float]) -> int:
    # Zamiana na tablicę tupli (idx, val)
    tab_with_idx = [(k, v) for k, v in enumerate(tab)]
    n = len(tab_with_idx)
    # Sortujemy nową tablicę po wartościach
    quick_sort(tab_with_idx, 1, 0, n-1)
    # Zwaracamy maxa z wartośći bezwzględnej różnicy między nowym a starym indeksem
    return max(abs(tab_with_idx[i][0] - i) for i in range(n))


T = [0, 2, 1.1, 2, -2,8]
print(chaos_index(T))
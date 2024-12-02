from egzP4atesty import runtests
# Complexity -> O(nlogn), gdzie n to liczba połączeń w tablicy T
# Sortujemy mosty najpierw po pierwszej a następnie drugiej współrzednej . Następnie tworzymy nową tablicę z drugimi
# współrzędnymi mostów i wykonujemy na niej algorytm lis. Zwracamy długość tablicy z lis.
"""

Złożoność akceptowalna (1.5pkt):O(n^2)
Złożoność wzorcowa (+2.5pkt):O(nlogn), gdzie n to liczba połączeń w tablicy T

Po dwóch stronach pewnej rzeki znajdują się różne miasta. Zarówno na brzegu północnym, jak i południowym, jest ich
tyle samo. Projekt budżetowy uchwalony na najbliższy rok zakłada zbudowanie pewnej liczby mostów łączących miasta po 
przeciwnych stronach rzeki. Jako, że projekt jest finansowany ze środków Unii Europejskiej, rządowi zależy, aby mostów 
zbudować jak najwięcej. Grupa ekspertów składająca się z inżynierów budowlanych wytypowała pewne połączenia, uznane za 
możliwe do zrealizowania. Oczywiście nie wszystkie z nich można wybudować,ponieważ żadne dwa mosty nie mogą się ze sobą 
przecinać (wykluczamy wszystkie sytuacje, w których jeden most znajdowałby się nad innym tj. nie mogą się przecinać 
także po zrzutowaniu na mapę 2D). Wszystkie mosty muszą być również idealnie proste. W ramach zadania należy 
zaimplementować funkcję:
 def mosty( T )
która oblicza liczbę mostów, które zostaną wybudowane w ramach projektu budżetowego.
 1. Tablica T zawiera listę potencjalnych mostów, wyrażoną w postaci krotek (u, v) gdzie u jest
indeksem miasta na brzegu północnym, a v jest indeksem miasta na brzegu południowym.
 2. Dla celów oszacowania złożoności należy założyć, że całkowita liczba miast może być dużo większa
niż liczba mostów wytypowanych przez inżynierów.
 3. Oznaczenia miast po przeciwnych stronach rzeki nie są ze sobą powiązane, co w szczególności
oznacza, że może wystąpić krotka np. (0, 0)
Rozważmy następujące dane:
T = [ (1, 2), (2, 3), (3, 0) ]
Wywołanie mosty( T )powinno zwrócić wynik 2. Można zbudować mosty pomiędzy miastami
1-2 oraz 2-3. Zbudowanie mostu między miastami 3-0 wyklucza pozostałe dwa ze względu na
przecięcie (patrz rysunek powyżej).
Podpowiedź. Czy można w jakiś sposób przeformułować ten problem?
"""

# Początko sortuje sobie daną tablicę po indeksach miast z połncnej strony, a w przypadku gdy te współrzędne są równo
# to po indeksie miast z południowej strony, tak aby zachować odpowiednia kolejność. Następnie po takim przygotowaniu
# danych, tworzę tablicę złożoną z indeksów miast po południowej stronie brzegu we wcześniej uzyskanuym porządku.
# Wówczas zadania sprowadza się do znalezienia długośći najdłuższego słabo rosnącego podciągu w tej tablicy.
# Złożoność O(nlogn)

def ceil_idx2(array, left, right, key) -> int:
    while right-left > 1:
        m = left + (right-left)//2
        if array[m] >= key:
            right = m
        else:
            left = m

    return right


def ceil_index(array, val) -> int:
    left_idx = 0
    right_idx = len(array) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if val > array[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx


def lis(tab) -> int:
    n = len(tab)
    s = []
    s.append(tab[0])

    for i in range(1, n):
        if tab[i] >= s[len(s)-1]:
            s.append(tab[i])
        else:
            s[ceil_index(s,tab[i])] = tab[i]
    return len(s)


def lis_2(arr) -> int:
    n = len(arr)
    if n < 2:
        return arr
    last = []
    ind = []
    parents = [-1] * n
    for i in range(n):
        j = ceil_index(last, arr[i])
        if j == len(last):
            if j > 0:
                parents[i] = ind[j - 1]
            ind.append(i)
            last.append(arr[i])
        else:
            ind[j] = i
            last[j] = arr[i]
            if j > 0:
                parents[i] = ind[j - 1]

    # Get result
    result = [-1] * len(last)
    j = ind[-1]
    for i in range(len(last) - 1, -1, -1):
        result[i] = arr[j]
        j = parents[j]
    # if len(last) < 10 :
    #     print(f'{result = }')
    return len(last)


def mosty (T):
    T.sort(key=lambda x: (x[0], x[1]))
    new_t = [T[i][1] for i in range(len(T))]
    return lis_2(new_t)

runtests ( mosty, all_tests=True )
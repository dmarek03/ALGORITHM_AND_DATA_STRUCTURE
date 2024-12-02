from egz3btesty import runtests
from math import inf
# Dominik Marek
# Toworze nową tablcie krotek postaci (p[0], p[1], i) , gdzie i to indeks z tablicy początkowej i sortuje tę tablice
# po współrzędnej y przedziałów. Następnie dla każdego przedziału za pomocą wyszukiwania binaranego sprawdzamy czy
# instniej w tablicy przedział niefajny względem niego , używamy do tego funkcji has_common_point i contain. Jeśli taki 
# przedział istnieje to zwracam wspołrzędne i-tego j -tego przedziału patrząc na współrzędne z początkowej tablicy.
# Złożoność O(nlogn) - n razy binary search


def has_common_point(range1, range2):
    return range1[0] <= range2[0] <= range1[1] or range2[0] <= range1[0] <= range2[1]


def contain(range1, range2):
    return range1[0] <= range2[0] and range1[1] >= range2[1] or range2[0] <= range1[0] and range2[1] >= range1[1]


def recursively_binary_search(tab, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        #print(f'{mid=}')
        #print(f'{tab[mid][:2]=}')
        if has_common_point(x, tab[mid]) and not contain(x, tab[mid]):
            #print(f'found')
            return mid

        #print(f'{tab[mid][1]=} {x[1]=}')
        # Jeżeli współrzędna x jest większa niż wspołrzędna y tab[mid] to w lewej połowie tablicy nie ma szans na
        # znalezienie przedziału, który miałby punkt wspołny z obecnie rozpatrywanym
        if tab[mid][1] < x[0]:
            #print(f'x is greater')
            return recursively_binary_search(tab, mid, right, x)
        else:
            #print(f'x is lower')
            return recursively_binary_search(tab, left, mid-1, x)
    return -1


def uncool(P):
    n = len(P)
    new_p = sorted([[p[0], p[1], i] for i, p in enumerate(P)], key=lambda x: x[1])
    #print(f'{new_p=}')
    for i in range(n):
        j = recursively_binary_search(new_p, i+1, n-1, new_p[i][:2])
        #print(f'{j=}')
        if j > 0:
            return [new_p[i][2], new_p[j][2]]



def uncool1(P):
    n = len(P)
    new_p = sorted([[p[0], p[1], i] for i, p in enumerate(P)], key=lambda x: x[0])
    for i in range(n):
        for j in range(n):
            if has_common_point(new_p[i], new_p[j]) and not contain(new_p[i], new_p[j]):
                return [new_p[i][2], new_p[j][2]]


def uncool3(P):


    # Sortujemy przedziały po lewym końcu
    intervals = sorted((a, b, i) for i, (a, b) in enumerate(P))

    active_intervals = []

    for a, b, index in intervals:
        # Usuwamy przedziały, które nie mogą być niefajne
        active_intervals = [x for x in active_intervals if x[0] >= a]

        # Sprawdzamy, czy aktualny przedział jest niefajny z którymkolwiek z aktywnych przedziałów
        for end, start, other_index in active_intervals:
            if not (b < start or end < a or (start <= a and b <= end) or (a <= start and end <= b)):
                return index, other_index

        # Dodajemy obecny przedział do aktywnych przedziałów
        active_intervals.append((b, a, index))
        # Utrzymujemy listę aktywnych przedziałów posortowaną po prawym końcu
        active_intervals.sort()

    return None


def uncool4( P ):
    P = sorted((x, -y, i) for i, (x, y) in enumerate(P))

    interval_queue = [(-1, -1, -1)]
    for a, b, cur_idx in P:
        b = -b

        # Wyjmij pierwszy przedział co ma punkt wspólny z obecnym
        comp_start, comp_end, comp_idx = interval_queue.pop()
        while interval_queue and comp_end < a:
            comp_start, comp_end, comp_idx = interval_queue.pop()

        # Jeśli obecny przedział zawiera się w wyjętym, włóż wyjęty z powrotem aby do niego wrócić
        if b <= comp_end:
            interval_queue.append((comp_start, comp_end, comp_idx))
        # W przeciwnym wypadku jeśli przedział jest niefajny, to go zwróć
        elif a <= comp_end:
            return comp_idx, cur_idx

        # Włóż obecny przedział jako pierwszy następny sprawdzany do kolejki
        interval_queue.append((a, b, cur_idx))




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool3, all_tests=True)

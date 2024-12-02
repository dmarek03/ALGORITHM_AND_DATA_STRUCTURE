"""
Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków, z których inwestor musi
wybrać podzbiór spełniając jego oczekiwania. Każdy budynek reprezentowany jest jako prostokąt o pewnej wysokości h,
podstawie od punktu a do punktu b, oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b).
W takim budynku może mieszkać h ⋅ (b − a) studentów.
Proszę zaimplementować funkcję:
def select_buildings(T, p):
...
która przyjmuje:
• Tablicę T zawierająca opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
z oznaczeniami wprowadzonymi powyżej.
• Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.
Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych
od 0), które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę
studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić
zbiór o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają
punktu wspólnego.
Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja
powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo
uzasadnić jej poprawność i oszacować złożoność obliczeniową.
Przykład. Dla argumentów:
T = [ (2, 1, 5, 3),
(3, 7, 9, 2),
(2, 8, 11, 1) ]
p = 5
wynikiem jest tablica: [ 0, 2 ]
"""

from bulidings_testy import runtests
# Complexity -> O(np + nlogn)
# Rekurencyjnie zwracamy numery budynków z posortowanej tablicy wchodzące w skład najbardziej optymlanego rozwiązania
def get_result(dp, students, parents, cost, buildings, idx, p):
    if idx < 0:
        return buildings
    if idx == 0:
        if p >= cost[0]:
            buildings.append(0)
        return buildings
    # jeśli dla takiej samej ceny p liczba studentów jest taka sam dla budynku i oraz i-1 to znaczy ze i-ty budynek nie
    # należy do naszego rozwiązania, zatem sprawdzamy jak wygląda sytuacja dla wcześniejszego budynku. W przeciwynym
    # przypadku i-ty budynek dodajemy do rozwiązania i wywołujemy funkcję dla rodzica dodanego budynku oraz budżetu
    # pomniejszonego o koszt wybudowania dodanego budynku
    if dp[idx - 1][p] == dp[idx][p]:
        return get_result(dp, students, parents, cost, buildings, idx - 1, p)
    buildings.append(idx)
    return get_result(dp, students, parents, cost, buildings, parents[idx], p - cost[idx])


def find_prev_building(tab, left, r, val):
    while left <= r:
        mid = (left + r) // 2
        if tab[mid][3] < val:
            left = mid + 1
        else:
            r = mid - 1
    return left - 1

# za pomocą binary searcha znajdujemy dla każdego budynku wcześniejszy budynek, na który nie zachodzi
def get_prev_buildings(T):
    n = len(T)
    prev = [-1] * n
    for i in range(n):
        a = T[i][2]
        prev[i] = find_prev_building(T, 0, i, a)
    return prev


def select_buildings(tab, p):
    n = len(tab)
    # tablicę tab przerabiamy tak, aby każda krotka dodatkowo zawierała swój indeks, takby aby po posortowaniu można
    # było finalnie zwrócić pierwotne numery budynków


    tab = [(i, t[0], t[1], t[2], t[3]) for i, t in enumerate(tab)]
    tab.sort(key=lambda x:x[3])
    cost = [0] * n
    num_of_students = [0] * n
    parents = get_prev_buildings(tab)
    dp = [[0] * (p + 1) for _ in range(n)]
    # Dla każdego budynku wyznaczamy liczbę studentów jaką może pomieśći, koszt jego budowy
    for i in range(n):
        idx, h, a, b, c = tab[i]
        num_of_students[i] = (b - a) * h
        cost[i] = c
        # for j in range(i - 1, -1, -1):
        #     if tab[i][2] > tab[j][3]:
        #         parents[i] = j
        #         break
    # Knapsack dla akademików i poszczególnych budżetów
    for i in range(n):
        for j in range(p + 1):
            dp[i][j] = dp[i - 1][j]
            if parents[i] is not None and j >= cost[i]:
                dp[i][j] = max(dp[i][j], dp[parents[i]][j - cost[i]] + num_of_students[i])
            # elif parents[i] is None and j >= cost[i]:
            #     dp[i][j] = max(dp[i][j], num_of_students[i])
    buildings = []
    get_result(dp, num_of_students, parents, cost, buildings, n - 1, p)
    print(f'{buildings=}')
    print(f'{tab=}')
    # dzięki wcześniej przygotowanym krotką odtwarzamy poprawne rozwiązanie
    for i in range(len(buildings)):
        buildings[i] = tab[buildings[i]][0]
    buildings.sort()

    return buildings


def select_buildings1(T, p):
    # Sort buildings by the end point b
    T = sorted(enumerate(T), key=lambda x: x[1][2])
    n = len(T)

    # dp[i][j] will store the maximum number of students that can be housed with budget j using first i buildings
    dp = [[0] * (p + 1) for _ in range(n + 1)]
    # track[i][j] will store the index of buildings selected to achieve dp[i][j]
    track = [[[] for _ in range(p + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        idx, (h, a, b, w) = T[i - 1]
        num_students = h * (b - a)
        for j in range(p + 1):
            # Case 1: Do not take the current building
            dp[i][j] = dp[i - 1][j]
            track[i][j] = track[i - 1][j]

            # Case 2: Take the current building if budget allows
            if j >= w:
                # Find the last building that doesn't overlap
                k = i - 1
                while k > 0 and T[k - 1][1][2] > a:
                    k -= 1

                if dp[k][j - w] + num_students > dp[i][j]:
                    dp[i][j] = dp[k][j - w] + num_students
                    track[i][j] = track[k][j - w] + [idx]

    # Find the solution with the maximum number of students within the budget
    max_students = 0
    best_buildings = []
    for j in range(p + 1):
        if dp[n][j] > max_students:
            max_students = dp[n][j]
            best_buildings = track[n][j]

    return sorted(best_buildings)

runtests(select_buildings)
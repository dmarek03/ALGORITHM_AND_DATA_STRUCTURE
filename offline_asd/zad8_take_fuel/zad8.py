# DOMINIK MAREK
# Aby rozwiązać zadanie wykorzystuję następujący algorytm:
# 1) Początkowo za pomocą funkcji algorytmu dfs, znajduję ilośc paliwa w danej plamie
# 2) Tworzę listę reprezentującą pierwszy wiersz tablicy podanej w zadaniu, jednak w miejsce początku plamy wpisuję
#    wartość całego paliwa, które można z niej zebrać
# 3) Następnie iterując po pierwszym wierszu dodaje do kolejki priorytetowej ilość paliwa znajdującego się w danej
#    plamie ropy, jednak wartość tą przemnażam przez "-1", tak aby na początku kolejki znajdowały się plamy z największą
#    ilością paliwa. W każdej iteracji pętli wartość aktualnego paliwa pomniejszam o jeden. Gdy wartość paliwa osiągnie
#    zero, powiększam(odejmuję , gdyż do kolekji dodałem wartość z minusem) ją o wartość znajdującą się na poczatku
#    kolejki piorytetwoej oraz liczbę przystanków zwiększam o jeden. Mogę to uczynić, gdyż najpierw dodająć plamy do
#    kolejki, mam pewność, że jestem w stanie dojechać do danej stacji, gdy będę chciał zatankować z niej paliwo.

from zad8testy import runtests
from queue import PriorityQueue


def get_fuel(T, row, col, actual_fuel):
    n = len(T)
    m = len(T[0])
    actual_fuel[0] += T[row][col]
    T[row][col] = 0
    new_row = [row - 1, row + 1, row, row]
    new_col = [col, col, col - 1, col + 1]
    nn = len(new_col)
    for i in range(nn):
        if 0 <= new_row[i] < n and 0 <= new_col[i] < m and T[new_row[i]][new_col[i]] != 0:
            get_fuel(T, new_row[i], new_col[i], actual_fuel)
    return actual_fuel[0]


def create_road(tab, m):
    road = [0]*m
    for i in range(m):
        if tab[0][i] > 0:
            fuel = [0]
            road[i] = get_fuel(tab, 0, i, fuel)
    return road


def plan(T):
    stops = 0
    m = len(T[0])
    road = create_road(T, m)
    queue = PriorityQueue()
    total_fuel = 0
    for i in range(m-1):
        if road[i] != 0:
            queue.put(-road[i])
        if total_fuel == 0:
            total_fuel -= queue.get()
            stops += 1
        total_fuel -= 1

    return stops


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)

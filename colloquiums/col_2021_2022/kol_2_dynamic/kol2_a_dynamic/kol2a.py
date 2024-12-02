from kol2atesty import runtests


"""

Ciężarówka o numerze bocznym 1212 musi przejechać z punktu A do punktu B. Na trasie znajduje
się pewna liczba punktów kontrolnych oraz pewna liczba punktów przesiadkowych. Ciężarówką
jedzie dwóch kierowców-zmienników, Jacek i Marian. Z punktu A rusza Jacek, ale kierowcy muszą
się zmieniać najpóźniej na trzecim punkcie przesiadkowym od ostatniej zmiany. Zadanie polega na
takim zaplanowaniu przesiadek, żeby Marian był za kierownicą podczas mijania jak najmniejszej
liczby punktów kontrolnych.
Można sobie wyobrazić, że trasa przebiega po jednowymiarowej linii, gdzie punkt A jest na
pozycji 0 a punkty przesiadkowe i kontrolne mają współrzędne naturalne (większe od zera, parami
różne). Proszę zaimplementować funkcję:
def drivers( P, B )
która na wejściu otrzymuje tablicę P zawierającą współrzędne punktów przesiadkowych i kontrolnych, oraz współrzędną 
punktu B. Każdy element tablicy P to para (x,t), gdzie x to współrzędna
punktu a t ma wartość True jeśli jest to punkt przesiadkowy oraz False jeśli jest to punkt kontrolny.
Tablica P nie musi być posortowana. Funkcja powinna zwrócić indeksy punktów przesiadkowych,
na których kierowcy zamieniają się miejscami. Funkcja powinna być możliwie jak najszybsza.
Rozważmy następujące dane:
p = True
c = False
# 0 1 2 3 4 5 6 7 8 9
P = [(1,c),(3,c),(4,c),(6,c),(8,c),(9,c),(11,c),(13,c),(16,c),(17,c),
(2,p),(5,p),(7,p),(10,p),(12,p),(14,p),(15,p),(18,p)]
# 10 11 12 13 14 15 16 17
B = 20
wywołanie drivers(P, B) może zwrócić tablicę [11,12,15,16], odpowiadające poniższej sekwencji zmian (grube kreski 
odpowiadają punktom przesiadkowym):
"""

from math import inf

JACEK = 0
MARIAN = 1
CONTROL_POINT = False


def drivers(P, B):
    # tu prosze wpisac wlasna implementacje
    n = len(P)
    DP = [[None, None] for _ in range(n)]

    for i in range(n):
        P[i] = (P[i][0], P[i][1], i)
    P.sort(key=lambda x: x[0])

    fill(P, B, DP, 0, JACEK)
    return get_res(P, B, DP)


def fill(P, B, DP, point, driver):
    if DP[point][driver] is not None: return DP[point][driver]

    n = len(P)
    cnt_ctrl = 0
    cnt_chng = 0
    DP[point][driver] = inf

    for i in range(point + 1, n):
        if i == n - 1 or P[i][0] == B:
            if driver == MARIAN:
                if P[i][1] == CONTROL_POINT: cnt_ctrl += 1
                DP[point][driver] = min(DP[point][driver], cnt_ctrl)
            else:
                DP[point][driver] = 0
            break

        if P[i][1] == CONTROL_POINT:
            cnt_ctrl += 1
        else:
            cnt_chng += 1
            if driver == JACEK:
                DP[point][JACEK] = min(DP[point][JACEK], fill(P, B, DP, i, MARIAN))
            else:
                DP[point][MARIAN] = min(DP[point][MARIAN], fill(P, B, DP, i, JACEK) + cnt_ctrl)
            if cnt_chng == 3: break

    return DP[point][driver]


def get_res(P, B, DP):
    n = len(P)
    driver = JACEK
    point = 0
    i = 1
    cnt_ctrl = 0
    res = []

    while i < n and P[i][0] < B:
        if P[i][1] == CONTROL_POINT:
            cnt_ctrl += 1
        else:
            if driver == JACEK and DP[point][JACEK] == DP[i][MARIAN]:
                res.append(P[i][2])
                point = i
                cnt_ctrl = 0
                driver = MARIAN
            elif driver == MARIAN and DP[point][MARIAN] == DP[i][JACEK] + cnt_ctrl:
                res.append(P[i][2])
                point = i
                cnt_ctrl = 0
                driver = JACEK
        i += 1

    return res



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = False )
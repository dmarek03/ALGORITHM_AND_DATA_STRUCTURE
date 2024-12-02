# Dane są lampki o numerach od 0 do n-1. Każda z nich może świecić na zielono, czerwono lub niebiesko
# i ma jeden przełącznik, który zmienia jej kolor (z zielonego na czerwony, z czerwonego na niebieski
# i z niebieskiego na zielony). Początkowo wszystkie lampki świecą na zielono. Operacja (a, b) oznacza
# "wciśnięcie przełącznika na każdej z lampek o numerach od a do b". Wykonanych będzie m operacji.
# Proszę napisać funkcję:
# def lamps(n, L):
#     ...
# która mając daną liczbę n lampek oraz listę L operacji (wykonywanych w podanej kolejności) zwraca
# ile maksymalnie lampek świeciło się na niebiesko (lampki są liczone na początku i po wykonaniu
# każdej operacji).
from lamps_testy import runtests


def lamps(n, T):
    all_lamps = [0 for _ in range(n)]
    print(f'{T=}')
    max_blue = actual_blue = 0
    for i in range(len(T)):
        for j in range(T[i][0], T[i][1] + 1):
            if all_lamps[j] == 0:
                all_lamps[j] = 1
            elif all_lamps[j] == 1:
                all_lamps[j] = 2
                actual_blue += 1
            elif all_lamps[j] == 2:
                all_lamps[j] = 0
                actual_blue -= 1
        max_blue = max(max_blue, actual_blue)
    return max_blue


def lamps1(n, L):
    colors = [0] * n  # Inicjalizujemy listę kolorów wszystkich lampek na zielony (0).
    max_blue_count = 0  # Licznik lampek świecących na niebiesko.
    blue_count = 0

    for a, b in L:
        # Wykonujemy operację (a, b) na lampkach
        for i in range(a, b + 1):
            if colors[i] == 1:
                blue_count += 1
            elif colors[i] == 2:
                blue_count -= 1
            colors[i] = (colors[i] + 1) % 3  # Zmieniamy kolor lampki na kolejny (zielony -> czerwony -> niebieski)

    # Liczymy ile lampek jest na niebiesko (kolor 2)
        if max_blue_count < blue_count:
            max_blue_count = blue_count

    return max_blue_count



runtests(lamps)
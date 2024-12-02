from kol1atesty import runtests

"""
Mówimy,że dwa napisy są sobie równoważne, jeśli albo są identyczne, albo byłyby identyczne gdyby jeden z nich zapisać
od tyłu. Na przykład napisy "kot" oraz "tok" są sobie równoważne podbnie jak "pies" i "pies". Dana jest tablica T
zawierająca n napisów o łacznej długości N (każdy napis zawiera co najmniej jeden znak, więc N >= n ; każdy napis
składa się wyłącznie z małych liter alfabetu łacińskiego) . Siła napisu T[i] jest liczba indeksów j takich,
że napisy T[i] oraz T[j] są sobie równoważne . Napis T[i] jest najsilniejszy , jeśli żaden inny napis nie ma większej
siły. Proszę zaimplementowac funkcję g(T),która zwraca siłę najsilniejszego napisu z tablicy T. Na przykład dla wejścia:
T = ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]
wywołanie g(T) powinno zwrócić 3. Algorytm powinnien być możliwe jak najszybszy. Proszę podać złożoność czasową i
pamięciową zapropnowanego algorytmu.
"""


def to_histogram(word: str) -> list[int]:
    histogram = [0] * 26
    for w in word:
        histogram[ord(w)-97] += 1
    return histogram


def normalize_words(tab: list[str]) -> list[str]:
    return [t[::-1] if ord(t[0]) > ord(t[-1]) else t for t in tab]


def get_max_val(tab: list[list]) -> int:
    max_val = 0

    for t in tab:
        for i in range(26):
            if t[i] > max_val:
                max_val = t[i]
    return max_val


def counting_sort(tab, pos, max_val) -> None:
    n = len(tab)
    count_tab = [0]*(max_val+1)
    sorted_tab = [0]*n

    for i in range(n):
        count_tab[tab[i][pos]] += 1

    for i in range(1, len(count_tab)):
        count_tab[i] += count_tab[i-1]

    for i in range(n-1, -1, -1):
        sorted_tab[count_tab[tab[i][pos]]-1] = tab[i]
        count_tab[tab[i][pos]] -= 1

    for i in range(n):
        tab[i] = sorted_tab[i]


def the_strongest_word(tab: list[str]) -> int:
    tab = normalize_words(tab)
    normalized_tab = [to_histogram(t)+[t] for t in tab]
    max_val = get_max_val(normalized_tab)
    for i in range(25, -1, -1):
        counting_sort(normalized_tab, i, max_val)
    max_power = 1
    current_power = 1

    for i in range(1, len(normalized_tab)):
        if normalized_tab[i-1][-1] == normalized_tab[i][-1]:
            current_power += 1

            if current_power > max_power:
                max_power = current_power

        else:
            current_power = 1

    return max_power


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(the_strongest_word, all_tests=True)

"""
Szukanie różnicy w  posortowanej tablicy
"""


def find_diff(tab, x):
    n = len(tab)
    i = 0
    j = 1

    while j < n:
        if tab[j] - tab[i] == x:
            return i, j

        if tab[j] - tab[i] > x:
            i += 1
        else:
            j += 1


print(find_diff([1, 2, 4, 8], 4))
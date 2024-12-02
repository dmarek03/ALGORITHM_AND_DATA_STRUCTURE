"""
Znajdz min i max listy używając 3n/2 porownań
"""


def min_max(tab: list[int]) -> tuple[int, int]:
    n = len(tab)
    min_val = tab[0]
    max_val = tab[0]

    for i in range(1, n, 2):
        if tab[i] < tab[i-1]:
            curr_min_val, curr_max_val = tab[i], tab[i-1]

        else:
            curr_min_val, curr_max_val = tab[i-1], tab[i]

        min_val = min(min_val, curr_min_val)
        max_val = max(max_val, curr_max_val)

    return min_val, max_val

print(min_max([1, 2, 3,4 ,2 ,1 ,99, 5]))
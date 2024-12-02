"""
QUICK SELECT
"""


def partition(tab: list[int], left: int, right: int) -> int:

    pivot = tab[right]
    i = left - 1

    for j in range(left, right):
        if tab[j] <= pivot:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i+1], tab[right] = tab[right], tab[i+1]

    return i + 1


def quick_select(tab: list[int], left: int, right: int, x: int):
    if left == right:
        return tab[right]

    pos = partition(tab, left, right)

    if pos == x:
        return tab[x]

    elif pos > x:
        return quick_select(tab, left, pos-1, x)

    else:
        return quick_select(tab, pos+1, right, x)


t = [1, 4,0, 23, 45, 2, 0]
print(t)
print(quick_select(t, 0, len(t)-1, 5))
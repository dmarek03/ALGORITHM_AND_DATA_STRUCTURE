"""
Sortowanie proste listy
"""

# Bubble_sort -> O(n^2)


def bubble_sort(tab: list[int]) -> list[int]:
    n = len(tab)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if tab[j] > tab[j+1]:
                swapped = True
                tab[j], tab[j+1] = tab[j+1], tab[j]
        if not swapped:
            return tab
    return tab


print(bubble_sort([1, 24, 2, 4, 2, 4, 1, 1, 0, -45]))

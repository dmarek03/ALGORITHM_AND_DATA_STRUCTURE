"""
Zliczanie liczby inwersji w liście: Istnieje i,j takie, ze  i < j i T[i] > T[j]
Merge sort i potem sprawdzamy czy bierzemy z t1 czy z t2, liczbę inwersji zwiększamy o długość pierwszej tablicy-czyli
tyle ile jest tych inwersji
"""


def merge_sort(tab, inversion):
    if len(tab) > 1:
        n = len(tab)
        left_tab = tab[:n//2]
        right_tab = tab[n//2:]

        merge_sort(left_tab, inversion)
        merge_sort(right_tab, inversion)

        i = j = k = 0

        while i < len(left_tab) and j < len(right_tab):
            if left_tab[i] < right_tab[j]:
                tab[k] = left_tab[i]
                i += 1

            else:
                tab[k] = right_tab[j]
                inversion[0] += len(left_tab)-i
                j += 1
            k += 1

        while i < len(left_tab):
            tab[k] = left_tab[i]
            i += 1
            k += 1

        while j < len(right_tab):
            tab[k] = right_tab[j]
            k += 1
            j += 1

    return inversion[0]


print(merge_sort([1, 20, 6, 4, 5],  [0]))
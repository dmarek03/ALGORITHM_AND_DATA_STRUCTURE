"""
Mamy dany ciąg przedziałów domkniętych szukamy przedziału, w którym zawieraj się najwięcej innych przedziałów
1.Sortujemy
2. F: Liczymy ile przedziałów zaczeło się wczesniej niż i-ty: zliczamy j : aj < bi
3. G:  Liczymy ile przedziałów skończyło się wcześniej niż i-ty : zliczamy j : bj < bi
4. Szukamy max(G(i)-F(i))
5. Sortujemy tablicę początków i końców i szukamy na nich danego odcnika binary searchem
"""


def binary_search(tab, left, right, idx, x):
    if left <= right:
        mid = (left + right) // 2
        print(f'{tab[mid]=}')
        print(f'{x=}')

        if tab[mid] == x:

            return mid

        elif tab[mid][idx] > x[idx]:
            return binary_search(tab, left, mid - 1, idx, x)

        elif tab[mid][idx] < x[idx]:
            return binary_search(tab, mid + 1, right, idx, x)

        else:  # No need to check for equality again, just use else
            if tab[mid][2] > x[2]:
                return binary_search(tab, left, mid - 1, idx, x)
            else:
                return binary_search(tab, mid + 1, right, idx, x)

    # Return -1 if the element is not found
    return -1


def find_strongest_interval(tab: list[list[int]]) -> list[int]:
    n = len(tab)
    tab = [t + [idx] for idx, t in enumerate(tab)]
    print(f'{tab=}')
    x_order = sorted(tab, key=lambda x: x[0])
    y_order = sorted(tab, key=lambda x: x[1])
    print(f'{y_order=}')
    max_cnt = 0
    max_interval = [tab[0][0], tab[0][1]]
    for interval in tab:
        print(f'{interval=}')
        g = binary_search(y_order, 0, n-1, 1, interval)
        f = binary_search(x_order, 0, n-1, 0, interval)
        print(f'{g=}')
        print(f'{f=}')
        print(f'Number of interval contained in current interval =  {max(0, g-f)}')
        if max(g-f, 0) > max_cnt:
         max_cnt = max(g-f, 0)
         max_interval = interval

    print(f'{max_cnt=}')

    return max_interval[:2]


tab = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 1]]
tab1 = [[1, 100], [102, 110], [103, 104],[103, 105],[103, 106] ]
print(find_strongest_interval(tab))


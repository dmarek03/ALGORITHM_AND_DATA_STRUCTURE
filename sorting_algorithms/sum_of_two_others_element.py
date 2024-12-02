'''
] Zadanie 3. Proszę zaproponować algorytm, który dla tablicy liczb całkowitych rozstrzyga czy każda liczba z tablicy
jest sumą dwóch innych liczb z tablicy. Zaproponowany algorytm powinien być możliwie jak najszybszy. Proszę oszacować
jego złożoność obliczeniową.
'''


def sum_of_two_others_element(tab: list[int]):
    n = len(tab)
    is_sum_of_others_element = [False]*n
    tab.sort()
    print(f'{tab=}')
    for e in range(n):
        i = 0
        j = n-1
        while i < j:
            if tab[i] + tab[j] == tab[e]:
                is_sum_of_others_element[e] = True

            if tab[i] + tab[j] < tab[e]:
                i += 1
            else:
                j -= 1
    return is_sum_of_others_element


tab = [1]*10000
print(sum_of_two_others_element(tab))


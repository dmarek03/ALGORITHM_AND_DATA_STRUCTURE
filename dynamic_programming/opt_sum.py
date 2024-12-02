"""
Zadanie 2.
Szablon rozwiązania: zad2_snow.py
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą
być zarówno dodatnie jak i ujemne):
n1 + n2 + ... + nk
Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej
kolejności, by największy co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji
dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy) był możliwie jak
najmniejszy. Aby ułatwić sobie zadanie, asystent nie zmienia kolejności liczb w sumie a jedynie
wybiera kolejność dodawań.
Napisz funkcję opt sum, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie;
zakładamy, że tablica zwiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną wyniku tymczasowego w
optymalnej kolejności dodawań. Na przykład dla tablicy wejściowej:
[1,−5, 2]
funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.Uzasadnij poprawność
zaproponowanego rozwiązania i oszacuj jego złożoność obliczeniową. Nagłówek funkcji opt sum powinien mieć postać:
def opt_sum(tab):
...
"""
from opt_sumtesty import runtests
from math import inf


def copy_tab(tab_1, tab_2, idx):
    min_sum = sum(tab_2[idx:idx+2])
    tab_1[:idx] = tab_2[:idx]
    tab_1[idx] = min_sum
    tab_1[idx+1:] = tab_2[idx+2:]


def opt_sum(tab):
    n = len(tab)
    current_sum = []
    curr_tab = [-inf]*n

    for i in range(n-1):
        min_sum = inf
        first_idx = -1
        for j in range(n-i-1):
            if abs(tab[j] + tab[j+1]) < min_sum:
                first_idx = j
                min_sum = abs(tab[j] + tab[j+1])
        current_sum.append(min_sum)
        copy_tab(curr_tab, tab, first_idx)
        # print(f'{curr_tab=}')
        # print(f'{tab=}')
        curr_tab, tab = tab, curr_tab
    # print(current_sum)
    return max(current_sum)


# tab1 = [-1, -1, -1, -1]
# tab2 = [2, 5, -3, 6]
# copy_tab(tab1, tab2, 1)
# print(f'{tab1=}')
# print(f'{tab2=}')
#
#
#
# copy_tab(tab1, tab2, 0)
# print(f'{tab1=}')
# print(f'{tab2=}')

# t = [1, 5, -2]
# print(opt_sum(t))

# runtests(opt_sum)



def opt_sum2(tab):
    n = len(tab)
    inf = float('inf')
    F = [[inf] * n for _ in range(n)]
    S = [0] * n

    S[0] = tab[0]
    for i in range(1, n):
        S[i] = S[i - 1] + tab[i]

    def recur(i, j):
        print(f'recur({i}, {j})')
        if i == j:
            F[i][j] = 0
            print(*F, sep="\n")
            print("------------")
        elif j - i == 1:
            F[i][j] = abs(tab[i] + tab[j])
            print(*F, sep="\n")
            print("------------")
        elif F[i][j] == inf:
            curr_sum = abs(S[j] - S[i - 1] if i > 0 else S[j])
            for k in range(i, j):
                F[i][j] = min(F[i][j], max(curr_sum, recur(i, k), recur(k + 1, j)))
                print(*F, sep="\n")
                print("------------")
        return F[i][j]

    recur(0, n - 1)

    return F[0][n - 1]


print(opt_sum2([1, -5, 2]))

#[-5 5 -6 5 -4]
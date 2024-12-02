from zad5ktesty import runtests
# f(a, b)[0] - maksymalny wynik dla gracza pierwszego na przedziale [a, b]
# f(a, b)[1] - maksymalny wynik dla gracza drugiego na przedziale [a, b]
# Complexity -> O(n^2)

def f(a, b, tab, dp):
    if a == b:
        return tab[a], 0
    if a + 1 == b:
        return max(tab[a], tab[b]), min(tab[a], tab[b])

    if dp[a][b] != 0:
        return dp[a][b]

    if tab[a] + f(a + 1, b, tab, dp)[1] > tab[b] + f(a, b - 1, tab, dp)[1]:
        dp[a][b] = (tab[a] + f(a + 1, b, tab, dp)[1], f(a + 1, b, tab, dp)[0])
    else:
        dp[a][b] = (tab[b] + f(a, b - 1, tab, dp)[1], f(a, b - 1, tab, dp)[0])

    return dp[a][b]


def garek_recur(array):
    n = len(array)

    # Tworzenie tablicy dp o rozmiarze n x n, wypełnienie jej zerami
    dp = [[0] * n for _ in range(n)]

    return f(0, n - 1, array, dp)[0]


def garek(array):
    n = len(array)

    dp = [[(0, 0)] * n for _ in range(n)]

    # Wypełnienie tablicy dp dla pojedynczych kart
    for i in range(n):
        dp[i][i] = (array[i], 0)

    # Wypełnianie tablicy dp dla kolejnych długości sekwencji
    # Iteruje przez kolejene długosci sekwencji kart
    for len_subarray in range(2, n + 1):
        for i in range(n - len_subarray + 1):
            j = i + len_subarray - 1
            if n < 20:
                print(f'{array=}')
                print(f'{n=}')
                print(f'{len_subarray=}')
                print(f'{i=}')
                print(f'{j=}')
                print(f'{n - len_subarray + 1=}')
                print(f'{i + len_subarray - 1=}')
            take_left = array[i] + dp[i + 1][j][1]
            take_right = array[j] + dp[i][j - 1][1]

            if take_left > take_right:
                dp[i][j] = (take_left, dp[i + 1][j][0])
            else:
                dp[i][j] = (take_right, dp[i][j - 1][0])

    if n < 10:
        print(*dp, sep='\n')

    return dp[0][n - 1][0]


runtests(garek)

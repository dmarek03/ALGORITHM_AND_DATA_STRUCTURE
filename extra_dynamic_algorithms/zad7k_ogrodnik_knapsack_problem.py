from zad7ktesty import runtests
# Complexity -> O(n * max_weight)
# Zadanie polega na przerobieniu tablicy z korzeniami drzew na listę gdzie w pod indeksem będącym początkiem korzenia
# będzie znajdowała sie całkowita ilosć wody jaką potrzebuje drzewo. Następnie korzystając z problemu plecakowego
# znajdujemy maksymlany zysk

# Funkcja do zbierania paliwa z tablic 2D
def get_fuel(T, row, col, actual_fuel):
    n = len(T)
    m = len(T[0])
    actual_fuel[0] += T[row][col]
    T[row][col] = 0
    new_row = [row - 1, row + 1, row, row]
    new_col = [col, col, col - 1, col + 1]
    nn = len(new_col)
    for i in range(nn):
        if 0 <= new_row[i] < n and 0 <= new_col[i] < m and T[new_row[i]][new_col[i]] != 0:
            get_fuel(T, new_row[i], new_col[i], actual_fuel)
    return actual_fuel[0]


def ogrodnik (tab, trees, prices, max_weight):
    weights = []
    for d in trees:
        weights.append(get_fuel(tab, 0, d, [0]))

    if min(weights) > max_weight:
        return 0

    n = len(weights)
    dp = [[0]*(max_weight+1) for _ in range(n)]
    for i in range(weights[0], max_weight + 1):
        dp[0][i] = prices[0]

    for i in range(1, n):
        for w in range(1, max_weight + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= weights[i]:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i]] + prices[i])

    print(*dp, sep='\n')
    print(f'{max_weight=}')
    print(f'{weights=}')
    print(f'{prices=}')
    return dp[n-1][max_weight]


runtests(ogrodnik, all_tests=True)


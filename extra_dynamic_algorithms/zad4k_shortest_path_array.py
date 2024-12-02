from zad4ktesty import runtests
# Shortest path from (0, 0) to (n-1, n-1) and only moves to right and down are allowed.
# Complexity -> O(n^2)
def falisz ( T ):
    n = len(T)

    # Tworzenie tablicy wynikowej dp o takim samym wymiarze jak T
    dp = [[0] * n for _ in range(n)]
    #
    # # Wypełnianie pierwszego wiersza tablicy wynikowej
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + T[0][i]

    # Wypełnianie pierwszej kolumny tablicy wynikowej
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + T[i][0]

    # Wypełnianie reszty tablicy wynikowej
    for i in range(1, n):
        for j in range(1, n):
            # Bierzemy minimum z przyjścia na dane pole albo z góry albo z lewej strony.
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + T[i][j]

    if n < 20:
        print(*T, sep='\n')
        print('---------------------------')
        print(*dp, sep='\n')

    return dp[n - 1][n - 1]


runtests ( falisz )

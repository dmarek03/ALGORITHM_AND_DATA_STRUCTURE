from zad12ktesty import runtests 
from math import inf

# Time complexity -> O(kn^2)

def motorway(tab, k):
    n = len(tab)
    dp_sum = [0]*n
    dp_sum[0] = tab[0]
    for i in range(1, n):
        dp_sum[i] = dp_sum[i-1] + tab[i]

    dp = [[inf]*(k+1) for _ in range(n)]

    # Warunki brzegowe -> wszystkie odcinki maluje jeden malarz
    for i in range(n):
        dp[i][1] = dp_sum[i]
    # Warunki brzegowe -> przypadek gdy jest tylko jeden odcinek do malowania
    for j in range(1, k+1):
        dp[1][j] = tab[0]

    for i in range(1, n):
        for j in range(2, k+1):
            # Przechodzimy przez kolejne możliwe podziały danego fragmentu listy i wybieramy opytmalny koszt dla
            # j-odcinków malowanych przez i-malarzy
            for p in range(i):
                dp[i][j] = min(dp[i][j], max(dp[p][j-1], dp_sum[i] - dp_sum[p]))

    return dp[n-1][k]


runtests(motorway, all_tests=True)

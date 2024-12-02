from zad3ktesty import runtests
from math import inf

def ksuma(T, k):

    n = len(T)
    dp = [inf] * (n + 1)
    dp[0] = 0  # Base case: no elements to cover, sum is 0
    if k == n:
        return min(T)

    if k == 1:
        return sum(T)

    for i in range(1, n + 1):
        # We need to check the minimum value in the window of size k
        min_val = inf
        for j in range(1, k + 1):
            if i - j >= 0:
                min_val = min(min_val, dp[i - j])
        dp[i] = min_val + T[i - 1]

    # The answer will be the minimum value in the last k elements of the dp array
    print(dp)
    return min(dp[n - k + 1:])





runtests ( ksuma )


from zad1ktesty import runtests
# f(a, b) - różnica pomiędzy ilością zer a jedynek na przedziale od a do b.
# Tworzymy tablicę dwuwymiarową dp, która będzie przechowywała różnicę miedzy ilośćią zer a jedynek na przedziale <i,j>.
# Complexity -> O(n^2)


def recur(a, b, text, dp):
    if dp[a][b] != 0:
        return dp[a][b]
    dp[a][b] = dp[a][b-1] + (1 if text[b] == '0' else -1)
    return dp[a][b]


def roznica( S:str ):
    n = len(S)
    max_difference = 0

    if S == '1'*n:
        return -1
    dp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            max_difference = max(max_difference, recur(i, j, S, dp))

    return max_difference


# Complexity -> O(n^2)

def roznica2( S:str ):
    n = len(S)

    if S == '1'*n:
        return -1

    dp = [[0]*n for _ in range(n)]
    max_difference = 0

    for i in range(n):
        for j in range(i+1, n):
            dp[i][j] = dp[i][j-1] + (1 if S[j] == '0' else -1)
            max_difference = max(max_difference, dp[i][j])
    return max_difference



runtests ( roznica2 )
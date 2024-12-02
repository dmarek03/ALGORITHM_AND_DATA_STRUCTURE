from zad8ktesty import runtests
# Complexity-> O(n*m)
# f(a, b) -> ilosc operacji potrzebnych na zamianę word1[:a+1] na word2[:b+1].
# Aby otrzymać poprawne słowo możemy wykonać na każdym razem jedną z trzech operacji:
# - wstawienie litery do naprawianego słowa
# - usunięcie litery z naprawianego słowa
# - zamiana litery w naprawianym słowie


def f(s, t, a, b, dp):
    n = len(s)
    m = len(t)
    if a >= n:
        return m - b
    if b >= m:
        return n - a
    if dp[a][b] != 0:
        return dp[a][b]

    if s[a] == t[b]:
        dp[a][b] = f(s, t, a + 1, b + 1, dp)
    else:
        insert_cost = 1 + f(s, t, a, b + 1, dp)
        delete_cost = 1 + f(s, t, a + 1, b, dp)
        replace_cost = 1 + f(s, t, a + 1, b + 1, dp)
        dp[a][b] = min(insert_cost, delete_cost, replace_cost)

    return dp[a][b]


def repair(word1, word2):
    word1_len = len(word1)
    word2_len = len(word2)
    dp = [[0] * word2_len for _ in range(word1_len)]

    return f(word1, word2, 0,0 , dp)


def repair2(word1, word2):
    n = len(word1)
    m = len(word2)

    # Inicjalizacja tablicy DP z wartościami początkowymi.
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Wypełnienie tablicy DP.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # jeśli oba słowa mają takie same litery na pozycjach i-1 oraz j-1 to koszt takiej zamiany to zero
            cost = 0 if word1[i - 1] == word2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,  # Usunięcie
                           dp[i][j - 1] + 1,  # Wstawienie
                           dp[i - 1][j - 1] + cost)  # Zamiana lub brak zmiany

    if n < 10:
        print(f'{word1=}')
        print(f'{word2=}')
        print(*dp, sep='\n')

    return dp[n][m]


def minimum_distance(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    dp = [[0]*(len1+1) for _ in range(len2+1)]
    for i in range(len1 + 1):
        dp[0][i] = i
    for i in range(len2+1):
        dp[i][0] = i
    for i in range(len2):
        for j in range(len1):
            if string1[j] == string2[i]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j], dp[i][j+1])+1
    return dp[len2][len1]


runtests(minimum_distance)

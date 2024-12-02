from zad6ktesty import runtests 
# Coplexity - > O(n)
# Funkcja znajduje iczbę możliwośći zakodowania danej wiadomośći
def haslo ( S ):
    n = len(S)

    dp = [0] * (n + 1)
    #Pusty ciąg lub ciąg jednoelementowy można zakodować na jeden sposób
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        # Sprawdzamy, czy cyfra na pozycji i - 1 nie jest zerem. Jeśli nie jest zerem, to możemy dodać nowe hasło do
        # dp[i], które jest identyczne jak hasło w dp[i-1]. To dlatego, że nowa cyfra może być zdekodowana jako jedna
        # litera.
        if S[i - 1] != '0':
            dp[i] += dp[i - 1]
        # Tworzymy dwucyfrową liczbę (two_digit) z dwóch poprzednich cyfr. Sprawdzamy, czy ta liczba mieści się w
        # zakresie od 10 do 26 (włącznie). Jeśli tak, to możemy dodać nowe hasło do dp[i], które jest identyczne jak
        # hasło w dp[i-2]. To dlatego, że ta dwucyfrowa liczba może być zdekodowana jako jedna litera.
        two_digit = int(S[i - 2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i - 2]


    return dp[n]

runtests ( haslo )
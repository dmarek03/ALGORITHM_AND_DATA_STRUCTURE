from zad11ktesty import runtests
# W tablicy dp przechowujemy informacje czy za pomocą dostępnych odważników jestesmy wstanie otrzymać i-tą wagę.
# Jeśli dp[i] = 0 to i-tej wagi nie da się osiągnać.
# Jeśli dp[i] != 0 to jesteśy w stanie dostać daną wagę.
# Tablice dp wypełniamy dynamicznie dla każdej wagi z tablicy T przechodzimy w pętli od połowy całkowietej wagi do
# obecnie rozpatrywanej wagi pomniejszonej o jeden. Jeśli jesteśmy w stanie osiągąć  i-weight wagę to znaczy ze przy
# pomocy obecnej wagi osiągniemy również i-tą wagę.
# Następnie szukamy największej wartośći jaką uda nam się osiągnać korzystająć z dostępnych odważników i całkowitą wagę
# pomiejszamy o dwukrotność znalezionej maksymalnej wagi.Wynik tego działania jest ilośćią odwaźników jakie będzie
# trzeba dołożyć aby osiągnąć równowagę.
# Complexity - > O(ns) , gdzie s to suma elementów w tablicy T
def kontenerowiec(T):
    total_weight = sum(T)  # Całkowita waga wszystkich kontenerów

    # Tworzymy tablicę dynamiczną, w której będziemy przechowywać informacje o dostępnych wagach
    dp = [0] * (total_weight // 2 + 1)
    dp[0] = 1  # Brak odważników - waga 0 można zawsze osiągnąć

    # Przechodzimy przez każdy kontener i aktualizujemy tablicę dp
    for weight in T:
        for i in range(total_weight // 2, weight - 1, -1):
            dp[i] = dp[i] + dp[i-weight]

    # Szukamy największej wagi, którą można osiągnąć używając dostępnych wag
    for i in range(total_weight // 2, -1, -1):
        if dp[i]:
            return total_weight - 2 * i  # Zwracamy różnicę wag

runtests ( kontenerowiec )


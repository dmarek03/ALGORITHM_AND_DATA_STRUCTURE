from egz1btesty import runtests

from math import  inf
# DOMINIK MAREK

# W celu roziwązania zadania tworzę tablicę dp o rozmiarze n  x (k+1) wypełnioną na początku wartością  -inf,
# gdzie dp[i][j] reprezentuje maksymalną sumę podciągu kończącego się na indeksie i z dokładnie j usunięciami.Następnie
# dp[0][0] ustawiam na wartośc T[0], a pozostałe elemnty w pierwszym wierszu ustawiam na zero.Kolejeno iteruje przez
# kolejne indeksy w tablicy dp i rozważam 3 możliwośći:
# Jeśli nie usuwam elementu T[i] to aktualizujemy dp[i][j] jako max(dp[i][j], dp[i-1][j] + T[i](czyli dodaje do sumy T[i]))
# Jeśli usuwam element T[i[ wówczas jako dp rozważam max(dp[i][j], dp[i - 1][j - 1](wartość sumy bez T[i]))
# Jeśli rozpoczynam nowy podciąg od T[i] elementu to :
# a) jeśli j == 0 to dp[i][j] = max(dp[i][j], T[i]) -> jeśli usuwamy 0 elementów to rozważamy rozpoczęcie podciągu od T[i] elementu
# b) jeśli j > 0 to   dp[i][j] = max(dp[i][j], 0) -> jeśli mam możliwe usunięcia to rozpatrujemy ropoczęcię podciągu z mpżlwiym usunięciem j elementów
# Następnie aktualizuję zmienną przechowujacą maksymalną sumę k-spoójnego podciągu
# Finalanie po wypełnieniu tablicy dp zwracamy wyżej wspomnianą zmienną co jest rozwiązaniem naszego zadania.
# Złożoność obliczeniowa O(nk) -> wypełnienie tablicy o rozmairze n x k
# Złożoność pamięciowa O(nk) -> tablica dp o rozmiarze n x k
def kstrong(T, k):
    n = len(T)

    if n < 1:
        return 0

    dp = [[-inf] * (k + 1) for _ in range(n)]


    dp[0][0] =  T[0]

    max_sum = T[0]


    for j in range(1, k + 1):
        dp[0][j] = 0


    for i in range(1, n):
        for j in range(k + 1):

            dp[i][j] = dp[i - 1][j] + T[i]


            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1])


            if j == 0:
                dp[i][j] = max(dp[i][j], T[i])
            else:
                dp[i][j] = max(dp[i][j], 0)

            max_sum = max(max_sum, dp[i][j])


    return max_sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True)

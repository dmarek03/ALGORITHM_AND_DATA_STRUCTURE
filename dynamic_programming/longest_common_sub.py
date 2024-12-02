# Mamy dane dwie tablice, A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego
# podciągu. (Klasyczny algorytm dynamiczny O(n**2)).
# Tworzymy tablicę dp, którą wypełniamy dynamicznie , gdzie dp[i][j] - to długosć najdłuższego podciągu dla i elementów
# z pierwszej tablicy i oraz j elementów z drugiej tablicy. Następnie iterujemy przez elementy dwóch tablicy i jesli elementy
# z tablic z pozycji i-1 i oraz j-1 są równe to aktualizujemy wartość w dp[i][j] jako wartość najdłuższego podciągu bez
# obecnie sprawdzanych elementów plus jeden. W przeciwynym przypadku bierzemy maksimum z możliwośći pominięcia albo i-1
# elementu w pierwszej tablicy albo j-1 w drugiej.
# Złożoność O(nm)
def longest_common_subsequence(A, B):
    len_a = len(A)
    len_b = len(B)
    T = [[0] * (len_a + 1) for _ in range(len_b + 1)]
    for i in range(len_a + 1):
        for j in range(len_b + 1):
            if i == 0 or j == 0:
                T[i][j] = 0
            if A[i - 1] == B[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
    return T[len_a][len_b]


A = [1, 5, 4, 2, 0]
B = [4, 5, 2, 0, 9]
print(longest_common_subsequence(A, B))
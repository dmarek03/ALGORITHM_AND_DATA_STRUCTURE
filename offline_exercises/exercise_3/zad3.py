# Dominik Marek
from zad3testy import runtests


def dominance(P):
    n = len(P)
    y_tab = sorted(P, key=lambda x: x[1])
    current_dominance = 0
    max_dominance = 0
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            if y_tab[i][1] > y_tab[j][1] and y_tab[i][0] > y_tab[j][0]:
                current_dominance += 1

        if current_dominance > max_dominance:
            max_dominance = current_dominance
        current_dominance = 0
        if max_dominance > i:
            break

    return max_dominance

# Złożoność obliczeniowa : O(3n) -> O(n)
# Złożoność pamięciowa -> O(2n+2) -> O(n)
def dominance_2(P):
    n = len(P)
    x_tab = [0]*(n+1)
    y_tab = [0]*(n+1)
    # W listach x_tab oraz y_tab zliczam odpowiednio liczbę wystąpień
    # poszczególnych współrzędnych x i y z tablicy wejściowej
    for i in range(n):
        x_tab[P[i][0]] += 1
        y_tab[P[i][1]] += 1
    # W tablicy x_tab pod indeksem i trzymam liczbę punktów o x >= i
    # W tablicy y_tab pod indeksem i trzymam liczbę punktów o y >= i
    for i in range(n-1, -1, -1):
        x_tab[i] += x_tab[i+1]
        y_tab[i] += y_tab[i+1]

    max_dom = 0
    # Dla każedo punktu z tablicy obliczam liczbę punktów, nad którymi dominuje,odejmując od liczby wszystkich punktów
    # liczbę punktów o większej bądz równej współrzędnej x oraz o  większej bądz równej współrzędnej y, co można
    # przeddstawić poniższym wzorem:
    # curr_dom = n - x_tab[P[i][0]] - y_tab[P[i][1]] + 1

    for i in range(n):
        curr_dom = n - x_tab[P[i][0]] - y_tab[P[i][1]] + 1
        if curr_dom > max_dom:
            max_dom = curr_dom
    return max_dom


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(dominance_2, all_tests=True)

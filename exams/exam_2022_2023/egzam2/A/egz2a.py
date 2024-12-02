from egz2atesty import runtests
# Dominik Marek
# Sortuje punkty po drugiej współrzędnej oraz tworzę tablicę pomocniczą do zliczania punktów, które dany punkt dominuje.
# Następnie przechodząc od końca dla każdego punktu sprawdzamy punkty od indeksu i+1 i sprawdzamy czy są one dominowane
# przez punkt na pozycji i. Jeśli tak do powiększam wartość w tablicy tab pod indeksem i. Finalanie zwracam maksimum z
# tablicy count_dominiance,gdzie zliczam ile dominacje dla danego punktu.
# Złożność obliczeniowa -> O(n^2) - dla każdego punktu sprawdzamy n-i-1 punktów. .



def dominance(P):
    P.sort(key=lambda x: x[1])
    n = len(P)
    count_dominance = [0]*n
    P.append((1, 1000))
    for i in range(n-1, 0, -1):
        for j in range(i-1, -1, -1):
            if P[i][0] > P[j][0] and P[i][1] > P[j][1]:
                count_dominance[i] += 1
    return max(count_dominance)



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

    print(f'{x_tab=}')
    print(f'{y_tab=}')
    # W tablicy x_tab pod indeksem i trzymam liczbę punktów o x >= i
    # W tablicy y_tab pod indeksem i trzymam liczbę punktów o y >= i
    for i in range(n-1, -1, -1):

        x_tab[i] += x_tab[i+1]
        y_tab[i] += y_tab[i+1]

    print(f'{x_tab=}')
    print(f'{y_tab=}')

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
runtests( dominance_2, all_tests = False)

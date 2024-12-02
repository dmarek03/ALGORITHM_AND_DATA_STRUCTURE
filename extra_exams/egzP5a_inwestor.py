from egzP5atesty import runtests

"""
Szablon rozwiązania
Złożoność akceptowalna (1.5pkt):O(n^2)
Złożoność wzorcowa (+2.5pkt): O(n), gdzie n to liczba działek
W jednym z kanadyjskich dystryktów, farmerzy uprawiali kukurydzę. Poważny amerykański
inwestor pracujący w jednej z największych firm, postanowił wykupić część tych działek, aby
zamiast kukurydzy, zbudować tam szklarnie do uprawy cytrusów. Zdając sobie sprawę, że wśród
farmerów znajdują się zazdrośnicy, postanowił, że od każdego farmera u którego zainwestuje,
kupi fragment działki o dokładnie takim samym polu powierzchni. Ponadto, aby zminimalizować
koszty przeznaczone na notariusza, zależy mu na tym, aby wszystkie działki, których fragmenty
wykupi, znajdywały się kolejno po sobie w księgach wieczystych. Jako doradca finansowy
inwestora, zostałeś poproszony o obliczenie, jakie jest maksymalne możliwe łączne pole
powierzchni części działek, w które zainwestuje, przy powyższych założeniach.
Zadanie polega na zaimplementowaniu funkcji:
inwestor( T )
która obliczy to największe możliwe łączne pole, przy założeniu, że tablica T zawiera pola
powierzchni działek wyrażone w hektarach oraz, że kolejność elementów w tablicy jest zgodna z
kolejnością występowania tych działek w księgach wieczystych. Dla ułatwienia przyjmujemy, że
nie ma działek o zerowym polu powierzchni.
Rozważmy następujące dane:
T = [2, 1, 5, 6, 2, 3]
Wywołanie funkcji inwestor( T ) powinno zwrócić wynik 10 (Inwestujemy w działki o polach
powierzchni 5 ha oraz 6 ha, wykupując z obydwu po 5 ha)
Podpowiedź. Czy informacja o tym, jakie jest najmniejsze pole spośród pewnego zbioru działek,
posiadana dla każdego dowolnego przedziału (a, b) ułatwiłaby rozwiązanie tego zadania?
"""
# Za pomocą funkcji get_min_area znajujemy minimalne pole na przedziale od a do b
# Następnie sprawdzamy znjadujemy minimalne pola dla każdego przedziału od i do j i wybieramy z nich maksymalne.

def get_min_area(tab: list[int], dp: list[list[int]], a: int, b: int) -> int:
    if a == b:
        dp[a][b] = tab[a]
        return tab[a]

    if dp[a][b] != -1:
        return dp[a][b]
    dp[a][b] = min(get_min_area(tab, dp, a, b-1), tab[b])
    return dp[a][b]


# O(n^2)
def inwestor_1(T):
    max_area = 0
    n = len(T)
    dp = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            max_area = max(max_area, (j-i+1) * get_min_area(T, dp, i, j))
    if n < 30:
        print(*dp, sep='\n')

    return max_area


# Wzorcowa złożoność :
#Wykorzytsujemy stos, aby dla każdego elementu w tablicy znaleźć pierwszy w kolejnośći element mniejszy z prawej i lewej
# strony danego elementu(Chcemy wykonywać to w czasie O(1)
# Zatem:
# 1) ściągamy ze stosu większy element i jako jego prawą mniejszą wartość ustawiamy obecnie przetwarzany element
# 2) jeżeli element po lewej stronie jest równy to przypisujemy mu taką samą lewą wartość jak przetwarzany element
# 3) jeżeli nie jest równy , to jako jego lewą wartość ustawiamy kolejny element ze stosu
# 4) dodajemy przetwarzny element na stos

def get_max_area(tab) -> int:
    s = [-1, 0]
    n = len(tab)
    max_area = 0
    lefts_values = [-1]*n
    rights_values = [n]*n

    for i in range(1, n):
        while s[len(s)-1] != -1 and tab[s[len(s)-1]] > tab[i]:
            rights_values[s[len(s)-1]] = i
            s.pop()

        if tab[i] == tab[i-1]:
            lefts_values[i] = lefts_values[i-1]
        else:
            lefts_values[i] = s[len(s)-1]
        s.append(i)

    for j in range(n):
        max_area = max(max_area, tab[j]*(rights_values[j]-lefts_values[j]-1))
    return max_area

# O(n)
def inwestor_2(T):
    return get_max_area(T)


runtests (inwestor_2, all_tests=True)


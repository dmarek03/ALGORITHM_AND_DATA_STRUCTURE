from kol2btesty import runtests

from math import inf


"""
Kierowca ciężarówki przewozi towary z miasta A do miasta B . W pewnych miejscach trasy przejazdu ajdują sit;'. 
parkingi. Przejeżdżając obok parkingu kierowca może (ale nie musi) się na nim
zatrzymać i odpocząć. Przepisy transportowe narzucają jednak pewne ograniczenia związane z
bezpieczeństwem:
l. Maksymalna liczba kilometrów, którą można przejechać bez zatrzymania wynosi T. Od zasady
tej istnieje jeden wyjątek, opisany w punkcie 2.
2. W trakcie całego przejazdu z A do B kierowca może jeden raz przekroczyć limit T kilometrów jazdy bez zatrzymania. 
Może wówczas prz jechać nie więcej niż 2T kilometrów bez
zatrzymania.
Niestety, parkingi na trasie są płatne. Co więcej, opiaty za postój óżnią się pomiędzy parkingami. 
Kierowca musi więc wybrać miejsca postoju w taki sposób, by przejechać trasę zgodnie z
obowiązującymi przepisami i równocześnie zapłacić możliwie jak najmniej za postoje.
Zaproponuj i zaimplementuj algorytm, który wylicza minimalny koszt przejechania z miasta
A do miasta B zgodnie z opisanymi przepisami transportu towarów. Koszt przejazdu z A do B
definiujemy jako umę opiat za parkowanie w miejscach, w których kierowca si~ zatrzymał (nic
liczymy ceny paliwa; nie bierzemy pod uwagę czasu postoju na parkingu). W miastach A i B oplata
nie jest pobierana. Uzasadnij poprawność zaproponowanego algorytmu i oszacuj jego ożoność
obliczeniową.
Algorytm należy zaimp ementować jako funkcję:
def min_cost( O, C, T, L)
Argumentami funkcji są:
• Tablica O zawierająca pozycje parkingów na trasie z A do B. O [i] to liczba kilometrów
(wzdłuż trasy przejazdu) od A do i-tego parkingu.
• Tablica C zawierająca ceny za postój na poszczególnych parkingach. C [i] to oplata za zatrzymanie na i-tym parkingu.
• Maksymalna liczba kilometrów T, którą można przejechać bez zatrzymywania (z zastrzeżeniem wyjątku opisanego powyżej).
• Długość L trasy (liczba kilometrów od A do B wzdłuż trasy przejazdu).
Wszystkie wartości przekazane w tablicach O i Coraz argumenty Ti L to dodatnie liczby naturalne.
Tablice nie muszą być posortowane. Funkcja min_cost powinna zwrócić jed1u1 li cz ę nat.urnln :
minimalny koszt przejazdu z A do B. Można założyć , że parkingi są tuk rozmieszczone, że da
ię prz jechać z A do B zgodnie z obowiązującymi zasadami. Funkcja powinna być możliwie jak
najszybsza. 
"""

# f(i,w) - minimalnny koszt dotarcia do i-tego miasta pod warunkiem w
# f(0) = 0
# w = 0 -> nie użyliśmy bonusu
# w = 1 -> użyliśmy bonus
#
# f(i,0) = min(f(i-k,0) + C[i] dla O[i]-O[i-k] <= T )
# f(i,1) = min(f(i-k,1) + C[i] dla O[i]-O[i-k] <= T,
#            f(i-k,0) + C[i] dla O[i]-O[i-k] <= 2*T )
#
# Złożoność O(n^2)

def min_cost(O, C, T, L):
    # tu prosze wpisac wlasna implementacje
    OC = []
    OC.append((0, 0))
    OC.append((L, 0))
    for o, c in zip(O, C):
        OC.append((o, c))
    OC.sort(key=lambda x: x[0])
    n = len(OC)

    DP = [[inf] * 2 for _ in range(n)]
    DP[0][0], DP[0][1] = 0, 0

    for miasto in range(1, n):
        for postoj in range(miasto - 1, -1, -1):
            if OC[miasto][0] - OC[postoj][0] > 2 * T: break
            if OC[miasto][0] - OC[postoj][0] <= T:
                DP[miasto][0] = min(DP[miasto][0], DP[postoj][0] + OC[miasto][1])
                DP[miasto][1] = min(DP[miasto][1], DP[postoj][1] + OC[miasto][1])
            else:
                DP[miasto][1] = min(DP[miasto][1], DP[postoj][0] + OC[miasto][1])

    return min(DP[-1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = False )

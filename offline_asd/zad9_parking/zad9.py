from zad9testy import runtests
from queue import PriorityQueue
from math import inf

"""
Kierowca ciężarówki przewozi towary z miasta A do miasta B. W pewnych miejscach trasy prze-
jazdu znajdują się parkingi. Przejeżdżając obok parkingu kierowca może (ale nie musi) się na nim
zatrzymać i odpocząć. Przepisy transportowe narzucają jednak pewne ograniczenia związane z
bezpieczeństwem:
1. Maksymalna liczba kilometrów, którą można przejechać bez zatrzymania wynosi T . Od zasady
tej istnieje jeden wyjątek, opisany w punkcie 2.
2. W trakcie całego przejazdu z A do B kierowca może jeden raz przekroczyć limit T kilo-
metrów jazdy bez zatrzymania. Może wówczas przejechać nie więcej niż 2T kilometrów bez
zatrzymania.
Niestety, parkingi na trasie są płatne. Co więcej, opłaty za postój różnią się pomiędzy parkin-
gami. Kierowca musi więc wybrać miejsca postoju w taki sposób, by przejechać trasę zgodnie z
obowiązującymi przepisami i równocześnie zapłacić możliwie jak najmniej za postoje.
Zaproponuj i zaimplementuj algorytm, który wylicza minimalny koszt przejechania z miasta
A do miasta B zgodnie z opisanymi przepisami transportu towarów. Koszt przejazdu z A do B
definiujemy jako sumę opłat za parkowanie w miejscach, w których kierowca się zatrzymał (nie
liczymy ceny paliwa; nie bierzemy pod uwagę czasu postoju na parkingu). W miastach A i B opłata
nie jest pobierana. Uzasadnij poprawność zaproponowanego algorytmu i oszacuj jego złożoność
obliczeniową.
Algorytm należy zaimplementować jako funkcję:
def min_cost( O, C, T, L )
Argumentami funkcji są:
• Tablica O zawierająca pozycje parkingów na trasie z A do B. O[i] to liczba kilometrów
(wzdłuż trasy przejazdu) od A do i-go parkingu.
• Tablica C zawierająca ceny za postój na poszczególnych parkingach. C[i] to opłata za za-
trzymanie na i-ym parkingu.
• Maksymalna liczba kilometrów T, którą można przejechać bez zatrzymywania (z zastrzeże-
niem wyjątku opisanego powyżej).
• Długość L trasy (liczba kilometrów od A do B wzdłuż trasy przejazdu).
Wszystkie wartości przekazane w tablicach O i C oraz argumenty T i L to dodatnie liczby naturalne.
Tablice nie muszą być posortowane. Funkcja min cost powinna zwrócić jedną liczbę naturalną:
minimalny koszt przejazdu z A do B. Można założyć, że parkingi są tak rozmieszczone, że da
się przejechać z A do B zgodnie z obowiązującymi zasadami. Funkcja powinna być możliwie jak
najszybsza.
Przykład. Dla danych:
O = [17, 20, 11, 5, 12]
C = [9, 7, 7, 7, 3]
T = 7
L = 25
wywołanie min cost(O, C, T, L) powinno zwrócić wartość 10.
Podpowiedź. Zastanów się, jaki jest koszt dojechania do parkingu i mogąc lub nie mogąc wyko-
rzystać wyjątek, o którym mowa w punkcie 2
"""
''' Armatys Konrad 415566
Algorytm:   na początku nie przejmójemy się 2 warunkiem i zapisujemy cenę najtańszej trasy z każdego parkingu do A i B;
            wyznaczamy je idąc od danego miasta(rozważmy miasto A) i idąc od najbliższego miasta x,
            patrzymy wtedy T do tyłu i szukamy najmniejszej ceny i odejmujemy od niej cenę postoju w mieśce x;
            czynność powtarzamy aż nie będziemy mieli wszystkich wart. dla miasta A i potem dla miasta B; * potem 
            próbujemy przejechać z każdego pola o 2T i szukamy najmniejszej wart takiej trasy korzystając z faktu że:
            przed i po wykonaniu przejazdu 2T chcemy jechać najtańszymi trasami o dł. nie większej od T 
            (czyli korzystamy z teg co wcześniej obliczyliśmy); bierzemy najmniejszą z wart. łącznej trasy z 
            wykorzystaniem przejazdu 2T.

            * wiemy że znalezione trasy będą najkrótsze bo możemy jechać max, T, więc patrząc T do tyłu rozważamy 
            wszytskie miasta z których może wieść optymalna trasa i wiemy że te wart. zostały obliczone wcześniej i są 
            poprawne;
Złożoność: O(n*log(n)) - sortowanie i n razy wyciąganie elem. z kolejki (n*log(n))
'''


def min_cost(O, C, T, L):
    ln = len(O) + 2

    P = [(O[i], C[i]) for i in range(len(O))]
    P.append((0, 0))
    P.sort()
    P.append((L, 0))

    cost_a = [inf for _ in range(ln)]
    pro_que_a = PriorityQueue()
    cost_a[0] = 0

    min_val = (cost_a[0], 0)
    for i in range(1, ln):
        while P[i][0] > min_val[1] + T and not pro_que_a.empty():
            min_val = pro_que_a.get()

        cost_a[i] = min_val[0] + P[i][1]
        pro_que_a.put((cost_a[i], P[i][0]))

    cost_b = [inf for _ in range(ln)]
    pro_que_b = PriorityQueue()
    cost_b[ln - 1] = 0

    min_val = (cost_b[ln - 1], L)
    for i in range(ln - 2, -1, -1):
        while P[i][0] <= min_val[1] - T - 1 and not pro_que_b.empty():
            min_val = pro_que_b.get()

        cost_b[i] = min_val[0] + P[i][1]
        pro_que_b.put((cost_b[i], P[i][0]))

    res = inf
    res_que = PriorityQueue()

    min_val = (0, 0)
    for i in range(1, ln):
        while P[i][0] > min_val[1] + 2 * T and not res_que.empty():
            min_val = res_que.get()

        res = min(res, (min_val[1] + 2 * T < L) * cost_b[i] + min_val[0])
        res_que.put((cost_a[i], P[i][0]))

    return res
#F(i,u) - minimalny koszt dojazdu do parking i, mogą lub nie mogąc wykorzystać zasadu 2T i - parking u - uzycie
# zasady 2T (u =1 mozna korzystac, u=0 nie mozna korzystac) F(i,0) = min( F(j,0) + C[i]),
# gdzie j nalezy 0 < O[i] - O[j] < T F(i,1) = min ( min (F(j,0) + C[i]) gdzie j nalezy T <= O[i] - O[j] <= 2T lub
# min (F(j,1) + C[i]) gdzie j nalezy do 0 < O[i] - O[j] < T) Warto dodać parking A oraz B z kosztem 0



def min_cost2(O: list, C: list, T: int, L: int) -> int:
    # O(n^2)
    P = [i for i in zip(O, C)]
    P.append((0, 0))
    P.append((L, 0))
    P.sort(key=lambda x: x[0])
    n = len(P)
    DP = [[inf for _ in range(2)] for _ in range(n)]
    DP[0] = [0, 0]

    for i in range(1, n):
        x0 = x1 = inf
        for j in range(i - 1, -1, -1):
            if P[i][0] - P[j][0] > 2 * T:
                break
            elif P[i][0] - P[j][0] <= T:
                # not using 2T cheat
                x0 = min(DP[j][0], x0)
                x1 = min(DP[j][1], x1)
            else:
                # using 2T cheat
                x1 = min(DP[j][0], x1)
        DP[i] = [x0 + P[i][1], x1 + P[i][1]]

    return DP[-1][1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost2, all_tests=True)
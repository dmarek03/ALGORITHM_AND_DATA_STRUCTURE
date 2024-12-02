from egzP8atesty import runtests
"""
Telewizja Polska część swoich zysków uzyskuje ze sprzedaży czasu reklamowego. Zgodnie z
nowym prawem każdy okres rozliczeniowy będzie obejmował pewną ilość dni, każdorazowo
ustaloną rozporządzeniem. W poprzednich latach dochody te były coraz mniejsze, dlatego w tym
roku prezes spółki postanowił zmienić strategię przetargową tak, aby je zmaksymalizować.
Wiadome jest, że największe zyski przynosi pierwszy blok reklamowy wyświetlany po
wieczornym wydaniu wiadomości. Prezes zadecydował, że w każdym okresie rozliczeniowym
maksymalnie dwie różne firmy będą mogły zdecydować się wyświetlać reklamy w ramach tego
bloku. Dodatkowo, każda z nich musi wskazać jeden określony zakres dni, w którym będą one
transmitowane codziennie. W ramach przetargu zgłosiła się pewna ilość firm, każda z nich
wskazując wybrany przez siebie zakres dni, w których chciałyby wyświetlać swoją reklamę oraz
oferując pewne wynagrodzenie za cały ten czas. Wybrane zostały oczywiście te, które dały łącznie
największy zysk. Prezes spółki chciałby dowiedzieć się, jaki zysk z reklam pierwszego bloku
osiągnie w najbliższym okresie rozliczeniowym.
Zadanie polega na zaimplementowaniu funkcji:
reklamy( T, S, o )
która zwróci zysk, który Telewizja Polska osiągnie z tych reklam, przy następujących założeniach:
 1. Tablica T zawiera okresy, w których firmy byłyby chętne wyświetlać swoje reklamy. Tablica
ma postać [(p0, k0), (p1, k1), ..., (pn-1, kn-1)] gdzie pi oznacza początek zakresu
dni w danym okresie rozliczeniowym, a ki koniec tego zakresu (włącznie) dla firmy i-tej.
 2. Tablica S określa stawki, które zostały zaoferowane przez firmy za cały okres wyświetlania
reklam i ma postać [s0, s1, ..., sn-1] gdzie si to stawka firmy i-tej za okres z tablicy T
 3. Zmienna o to określona rozporządzeniem ilość dni, którą będzie trwał okres rozliczeniowy.

"""

#O(nlogn), gdzie n to liczba firm biorących udział w przetargu

# Binary search right -> znajdujemy indeks x+1 - co gwarantuje ze okres nie będą ze soba kolidowały
def iterative_binary_search(tab: list[int], left: int, right: int, x: int) -> int:

    while left < right:
        mid = (left+right)//2

        if tab[mid] > x:
            right = mid

        else:
            left = mid+1

    return left


def reklamy ( T, S, o ):
    n = len(T)
    p = [[] for _ in range(n)]
    for i in range(n):
        p[i] = [T[i][0], T[i][1],  S[i]]
    p.sort(key=lambda x: x[0])
    result = 0
    m = [0 for _ in range(n)]
    # Do ostatniego indeksu tablicy m przypisujemy wartość ostatneigo okres z tablicy p
    m[n-1] = p[n-1][2]
    # Dla każdego okresu znajdujemy maksymalny zysk, który obliczamy jako maksikum z elementu poprzedniego albo
    # możliwego zysku z i-tego okresu.
    for i in range(n-2, -1, -1):
        m[i] = max(m[i+1], p[i][2])

    # Tworzymy tablicę z początkami okresów, dla ułatwienia podczas korzystania z binary searcha
    s = [p[i][0] for i in range(n)]
    # Dla każdego okresu sprawdzamy czy istnieje inny okres nie zachodzący na obecny okres i jesli taki okres istnieje
    # to sprawdzamy czy suma obcenie rozpatrywanego okresu i znalezionego okresu jest większa niż obecna  wartosć result
    for i in range(n):
        end = p[i][1]
        idx = iterative_binary_search(s, 0, n, end)
        second = 0
        if idx < n and s[idx] != end:
            second = m[idx]
        result = max(result, p[i][2]+second)

    return result


runtests ( reklamy, all_tests=False)
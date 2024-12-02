# DOMINIK MAREK

"""
Celem zadania jest znalezienie w napisie najdłuższego nieparzystego palindromu.Jeśli interesują nas tylko palindromy 
nieparzystej długości to można rozwiązać to zadanie w następujący sposób. Początkowo jak środek naszego palindromu
(i=1) ustawiamy drugą literę naszego napisu(zaczynamy sprawdzanie od palindromu długości trzy, gdyż każda litera jest 
palindromem długości jeden więc nie ma sensu ich sprawdzać). Następnie dopóki środek palindromu jest mniejszy od długości
napisu pomniejszonej o jeden, tworzymy indeksy reprezentujące początek i koniec (start, stop) naszego palindromu, którym 
przypsiujemy odpowiednio wartośći i - 1 oraz i + 1 . Następnie dopóki początek naszego palindromu jest większy bądź 
równy pierwszemu indeksowi naszego napisu a koniec mniejszy od ostatniego oraz litery pod indeksami początek i koniec są 
takie same, tworzmy zmienna reprezentującą długość palindromu(stop - start + 1) i porównujemy ją ze zmienną best_size, 
jeśli jest większa to akutualizujemy zmienną best_size, a następnie działając na zasadzie ekspansji poszerzamy 
sprawdzany "podnapis" poprzez dekrementacje indeksu start i inkrementacje indesku stop. Po zakończeniu wewnętrzenj pętli 
przesuwamy zmienną i (środek palindromu) o jeden i ponownie sprawdzamy czy nowy "podnapis" jest palindromem. 
Stosując ten algorytm znajdziemy wszytkie nieparzyste palindromy i długość najdłuższego z nich. 
Złożoność tego algorytmu wynosi 0(n^2).
"""

from zad1testy import runtests


def ceasar(s):
    n = len(s)
    i = 1
    best_size = 1

    while i < n-1:
        start = i - 1
        stop = i + 1
        while start >= 0 and stop < n and s[start] == s[stop]:

            curr_size = (stop - start) + 1
            if curr_size > best_size:
                best_size = curr_size

            start -= 1
            stop += 1

        i += 1
    return best_size


#zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ceasar, all_tests=True)

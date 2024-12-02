"""
Omówienie algorytmu
f(i,j) - minimalna liczba tankowań, jakie trzeba wykonać, aby dotrzeć do stacji o indeksie i , mając po dojechaniu na tę
stację j litrów paliwa.
Ja wykorzystuję podejście Bottom-up, ponieważ działa ono szybciej i w tym przypadku jest dla mnie bardziej naturalne.
W pierwszym kroku odfiltrowujemy stacje, na których napewno nie zatankujemy, bo odległość do tych stacji od punktu
startowego wynosi l lub więcej, a więc stacje leżą dalej niż punkt docelowy (lub na punkcie docelowym). Ponieważ punkt
docelowy może wypadać gdzieś między stacjami, a w algorytmie musimy jakoś stwierdzić, czy da się do niego dotrzeć,
najłatwiej jest odrzucić stacje, których odległość wynosi przynajmniej l i dodać jedną sztuczną stację końcową w punkcie
o odlełości l od startu, która ma np. 0 litrów paliwa, bo i tak nie zatankujemy na stacji docelowej. W kolejnym kroku,
korzystając z algorytmu dynamicznego, w pętli dla każdej z kolejnych stacji sprawdzamy wszystkie możliwe ilości paliwa,
jakie możemy mieć, wjeżdżając na daną stację i, jeżeli minimalna liczba tankowań dla danej stacji przy odpowiedniej
ilości paliwa jest mniejsza niż ∞ ( oznacza, że nie da się dotrzeć do danej stacji, mając wskazaną liczbę litrów paliwa
- wyjaśnienie później), tankujemy do pełna (lub tyle, ile maksymalnie możemy zatankować na danej stacji, jeżeli paliwa
nie wystarcza, by zatankować do pełna) (zawsze tankujemy jak najwięcej, bo chcemy tankować jak najmniej razy, a
zatankowanie największej możliwej ilości paliwa nam nigdy nie zaszkodzi, bo nie interesuje nas koszt, a jedynie liczba
tankowań) i sprawdzamy wszystkie stacje, do których jesteśmy w stanie dotrzeć po tankowaniu. Dla każdej z tych stacji,
uwzględniamy spalone po drodze paliwo i, jeżeli bieżąca liczba tankowań jest niższa od poprzednio zapisanej liczby
tankowań dla danej stacji przy odpowiedniej liczbie litrów paliwa (z uwzględnieniem spalonego po drodze), to ją
aktualizujemy, a także aktualizujemy rodzica (parę: indeks stacji, z której przyjechaliśmy oraz ilość paliwa, jaką
mieliśmy na tej stacji).

Złożoność
Obliczeniowa:
O(q*n^2)- dla każdej spośród n stacji możemy sprawdzić maksymalnie O(n) kolejnych stacji. Takie sprawdzenie dokonujemy
dla każdej wartości paliwa, z którą dostaliśmy się na daną stację, a mamy ( q+1 )możliwości dla każdej ze stacji.

Pamięciowa: O(nq)

"""
from directortesty import runtests
from math import inf


def get_path(fuels, dp):
    n = len(fuels)
    path = []
    # Look for the final amount of fuel
    best_j = 0
    for j in range(1, len(fuels[0])):
        if fuels[n - 1][j] < fuels[n - 1][best_j]:
            best_j = j
    # Return an empty array if a path doesn't exist
    if fuels[n - 1][best_j] == inf:
        return []
    # Restore a path
    i = n - 1
    j = best_j
    while dp[i][j]:
        i, j = dp[i][j]
        path.append(i)
    path.reverse()

    return path


def prepare_stations(tab, limits, length):
    n = len(tab)

    i = n - 1
    while i >= 0 and tab[i] >= length:
        i -= 1

    tab = tab[:i + 1]
    limits = limits[:i + 1]
    tab.append(length)
    limits.append(0)

    return tab, limits


def iamlate(tab, limits, capacity, length):
    if tab[0] != 0 or not tab:
        return []
    tab, limits = prepare_stations(tab, limits, length)
    n = len(tab)
    fuels = [[inf] * (capacity + 1) for _ in range(n)]
    dp = [[0] * (capacity + 1) for _ in range(n)]
    fuels[0][0] = 0

    for i in range(n):
        for fuel in range(capacity + 1):
            if fuels[i][fuel] == inf:
                continue

            j = i + 1
            new_fuel = min(capacity, fuel + limits[i])

            while j < n:
                dist = tab[j] - tab[i]
                remaining = new_fuel - dist
                if remaining < 0:
                    break
                if fuels[i][fuel] + 1 < fuels[j][remaining]:
                    fuels[j][remaining] = fuels[i][fuel] + 1
                    dp[j][remaining] = [i, fuel]
                j += 1
    return get_path(fuels, dp)


runtests(iamlate)




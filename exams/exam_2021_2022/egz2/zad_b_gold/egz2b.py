from egz2btesty import runtests
# Do rozwiązania zadania stosuje algorytm, który dynamicznie wypełnia tablicę dłgośći n.
# Przechodząć przez kolejne komnaty incijalizuje zmienne :
# * i_gold -> ilośc złota w szkrzyni w danej komnacie
# * chamber -> tablica tupli, zawierających informacje o koszcie przejścia do innej komnaty
# Następnie iteruje przez krotki znajduje się zmiennej chamber oraz tworze zmienną taken_gold, która jest równa
# ilośći złota zanajdującego się w komnacie pomeniejszonej o koszt otwarcia danych drzwi, jesli owa róźnica jest
# mniejsza niż 10 w przeciwnym przypadku 10. Kolejno dla pierwszej komnaty sprawdzam czy z danych drzwi mogę przejść
# dalej, czy jestem w stanie otworzyć komnatę .Jeśli te warunki są spełnione to dla danych drzwi w komnacie to w dp pod
# indeksem równym indeksowi komnaty z danych drzwi podstawiamy ilosć zabranego złota. Jeśli tak to dp[c[1]] jest równa
# maksimum z obecnej wartości oraz wartości złota która mozemy zabrać dla i-tej komnaty powiększonej o ilość
# złota zbranego w celu dojścia do c[1] komnaty.
# Złożoność obliczeniowa tego algorytmu jest równa O(n*chamber) = O(3n) -> O(n),
# gdyż przechodzimy raz przez tablicę o długości n a długość tablicy chamber jest stała i wynosi 3.
# Złożoność pamięciowa to O(n) - tworzymy tablicę dp długośći n.

def magic(castle):
    n = len(castle)
    dp = [-1]*n
    dp[0] = 0
    for i in range(n):
        i_gold = castle[i][0]
        chamber = castle[i][1:]

        for cost, door in chamber:

            taken_gold = min(10, i_gold- cost)
            if door > -1 and i == 0 and (i_gold-taken_gold == cost):
                dp[door] = taken_gold

            elif door > -1 and dp[i] > -1 and (i_gold-taken_gold == cost):
                dp[door] = max(dp[door], dp[i] + taken_gold)
    return dp[n-1]


def better_magic_but_not_mine(castle):
    n = len(castle)
    dp = [-1]*n
    dp[0] = 0
    for i in range(n):
        i_gold = castle[i][0]
        chamber = castle[i][1:]
        print(f'{i_gold=}')
        print(f'{chamber=}')
        # Uproszczone warunki, bo jesli taken_gold będzie nie większe niz 10 to znaczy ze biorąć pewną ilość złota
        # jestesmy w stanie otworzyć dane drzwi
        for cost, door in chamber:
            taken_gold = i_gold - cost
            print(f'{cost=}')
            print(f'{door=}')
            if dp[i] > - 1 and door > -1 and taken_gold <= 10:
                dp[door] = max(dp[door], dp[i] + taken_gold)
                print(f'{dp=}')

    return dp[n-1]



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(better_magic_but_not_mine, all_tests=False)

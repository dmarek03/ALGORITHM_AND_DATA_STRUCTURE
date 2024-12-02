from zad10ktesty import runtests
from math import inf
# Complexity -> O(nsqrt(n))
# Tablicę dp przechowuje informacje na temat minimalenje liczby kwadratów potrzebnych do pokrycia powierzchni i.
# Aktualizacja dp[i]:
#  Dla każdego możliwego boku bok, obliczamy, ile dywanów potrzebujemy do pokrycia pola o powierzchni i - side * side
#  i dodajemy 1 (ponieważ używamy jednego dywanu o boku bok). Porównujemy tę wartość z obecną wartością dp[i] i
#  zachowujemy mniejszą z tych dwóch wartości w dp[i]. To zapewnia, że mamy zawsze najmniejszą możliwą liczbę dywanów
#  potrzebnych do pokrycia pola i.
# Odtwarzając rozwiązanie zaczynamy od wartosći N i sprawdzmy czy w tablicy dp wartosć pod indeksem current_area
# odpowiada wartośći pod indeksem curren_area -side*side powiększonej o jeden, jeśli tak do do rozwiązania dodajemy side
# oraz wartość curren_area pomnniejszamy o pole kwadratu dodanego do rozwiązania.

def dywany(N):
    #print(f'{N=}')
    # Tworzymy tablicę, w której będziemy przechowywać informacje o optymalnych rozwiązaniach
    dp = [inf] * (N + 1)
    dp[0] = 0

    for current_area in range(1, N + 1):
        for side in range(1, int(current_area ** 0.5) + 1):
            dp[current_area] = min(dp[current_area], dp[current_area - side * side] + 1)


    print(f'{dp=}')

    # Odtwarzamy optymalne rozwiązanie
    carpet_measurements = []
    current_area = N
    while current_area > 0:
        for side in range(int(current_area ** 0.5), 0, -1):
            if dp[current_area] == dp[current_area - side * side] + 1:
                carpet_measurements.append(side)
                current_area -= side * side
                break
    return carpet_measurements

runtests(dywany)


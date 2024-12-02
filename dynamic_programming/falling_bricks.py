"""
Zdefiniujmy funkcję:
f(i)- najwyższa "wieża", jaką możemy zbudować, kończąca się na klocku o indeksie
W algorytmie dla każdego kolejnego klocka iterujemy przez wszystkie poprzednie i sprawdzamy, czy dany klocek może upaść
w całości na któryś z poprzednich. Jeżeli może, to wówczas badamy, czy jeżeli stanie się on górnym klockiem z tej wieży
(tzn. jeżelu umieścimy go na badanym klocku), to wzrośnie wysokość tej wieży (to znaczy, czy na tym klocku już wcześniej
nie było innych klocków, jeżeli nie, to wieża będzie wyższa). Odpowiednio zapisujemy wysokość najwyższej wieży, jaką da
się w ten sposób utworzyć, kończącej się na klocku o indeksie .Na koniec wystarczy odjąć od liczby wszystkich klocków
wysokość najwyższej wieży, a otrzymana liczba będzie równa liczbie klocków do usunięcia, bo chcemy usunąć minimalną
liczbę klocków, a to sprowadza się do tego, że chcemy zbudować możliwie najwyższą wieżę.
"""


def count_bricks(t:list[list[int]]) -> int:
    n = len(t)
    fn = [1]*n
    for i in range(1, n):
        for j in range(i):
            if t[i][0] >= t[j][0] and t[i][1] <= t[j][1]:
                fn[i] = max(fn[i], fn[j] + 1)
    print(fn)
    return n - max(fn)

ranges = [
    [0, 5],
    [1, 4],
    [-3, 7],
    [2, 3],
    [2, 6],
    [4, 6],
    [2, 3]
]

print(count_bricks(ranges))


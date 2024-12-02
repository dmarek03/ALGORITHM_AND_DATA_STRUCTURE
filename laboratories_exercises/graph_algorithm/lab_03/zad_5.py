"""
Mamy kantor.Mając pewną kwotę w danej walucie i chcemy kupując kolejne waluty na koniec mieć więcej pieniędzy w
wejściowej walucie.

1.Poszczególne kursy traktujemy jako graf ważony, skierowany.
2. Szukamy cyklu, w którym mnożąc wejściową wartośc przez kolejne krawędzie dostać wartość większą.
3. Logarytmujemy wagi krawędzi
4.Szukamy takiego cylku, którego y > 0 (czyli dajemy minus przed wynikiem ostatecznym)

"""
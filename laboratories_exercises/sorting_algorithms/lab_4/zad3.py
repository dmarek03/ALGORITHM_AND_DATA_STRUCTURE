"""
Mamy tablicę zawierającą n różnych liczb , chcemy znaleźć takie dwie liczby, że między nimi nie ma żadnego elementu a
ich różnica jest maksymalna

T= [7, 5, 8, , 12, 95]
Buckets:
[7, 5, 8, 12]   []      [95]
   (5-35)    (36-70)   (71-95)

Tablice dzielimy na n kubełków:

Jesli po podziale na kubełki mam jakiś pusty kubełek to jako różnię obliczamy
min(następny_kubełek) - max(wczesniejszy_kubełek)

Jeśli żaden z n kubełków nie jest pusty to mamy posortowane liczby więc bierzemy przechodzimy liniowo i szukamy
najwięszkej różnicy
"""


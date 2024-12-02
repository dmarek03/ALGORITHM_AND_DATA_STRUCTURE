"""
Graf ze stacjami benzynowymi. Każda krawędź to ilośc kilometrów między dwoma miastami, w każdym mieście jest
stacja paliw o danej cenie paliwa. Proszę  napisać algortym , który znajdzie trasę miedzy dwoma miastami o najniższym
koszcie przejazdu.

Spalamy 1l/1km

Bak ma pojemność D = 10l.

1.Rozmnażamy każdy wierzchołek na i podwierzchołków ,gdzie i = 0, 1, 2, ...D
2.Algorytm dijkstry na rozmnożonym grafie
"""
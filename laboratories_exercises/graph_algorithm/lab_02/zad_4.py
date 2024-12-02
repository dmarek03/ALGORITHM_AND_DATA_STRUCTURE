"""
Przewodnik chce przewieść grupę k turystów z miasta A do B. Między różnymi miastami jeżdzą autobusy o różnej pojemności.
Mamy listę krotke (x, y, c), gdzie mamy x i y to miastą miedzy którymi jedzie autobus o pojemności c.Przewodnik musi
wyznaczyć wspólną trasę dla wszytskich i musi ich podzielic na pewne grupy.Podać algortym na ile najmniej grup,
trzeba podzielić turystów.

1. Sortujemy krawędzie od największych do najmniejszych wag
2. Wybieramy drogę miedzy A i B idącą po największych krawędziach
3. Liczbę turystów dzielimi przez najmniejsza wagę i zaokrąglamy w góre.
1.Szukamy najmniejszego drzewa rozpinającego
2.

"""
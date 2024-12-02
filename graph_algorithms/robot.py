# Robot porusza się po dwuwymiarowym labiryncie i ma dotrzeć z pocycji A = (x[a], y[a]) na pozycję
# B = (x[b], y[b]). Robot może wykonać następujące ruchy:
#   1) ruch do przodu na kolejne pole,
#   2) obrót o 90 stopni zgodnie z ruchem wskazówek zegara,
#   3) obrót o 90 stopni przeciwnie do ruchów wskazówek zegara.
# Obrót zajmuje robotowi 45 sekund. W trakcie ruchu do przodu robot się rozpędza i pokonanie pierwszego
# pola zajmuje 60 sekund, pokonanie drugiego 40 sekund, a kolejnych po 30 sekund na pole. Wykonanie
# obrotu zatrzymuje robota i następujące po nim ruchy do przodu ponownie go rozpędzają. Proszę
# zaimplementować funkcję:
# def robot(L, A, B):
#     ...
# która oblicza ile minimalnie sekund robot potrzebuje na dotarcie z punktu A do punktu B (lub zwraca
# None jeśli jest to niemożliwe).
# Funkcja powinna być możliwie jak najszybsza. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.
# Labirynt. Labirynt reprezentowany jest przez tablicę w wierszy, z których każdy jest napisem
# składającym się z k kolumn. Pusty znak oznacza pole po którym robot może się poruszać, a znak ’X’
# oznacza ścianę labiryntu. Labirynt zawsze otoczony jest ścianami i nie da się opuścić planszy.
# Pozycja robota. Początkowo robot znajduje się na pozycji A = (x[a], y[a]) i jest obrócony w prawo
# (tj. znajduje się w wierszu y[a] i kolumnie x[a], skierowany w stronę rosnących numerów kolumn).
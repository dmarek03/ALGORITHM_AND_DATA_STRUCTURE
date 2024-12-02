from egzP6btesty import runtests

"""
W magicznej krainie istnieje nieskończona szachownica, w
której pola określna się przez współrzędne całkowite
(również ujemne). Dodatkowo każde pole posiada
żarówkę, która zmienia swój stan od razu, kiedy jakaś
figura szachowa robi ruch na to pole. Początkowo każde
pole na szachownicy było zgaszone, gdy nagle Konik
Szachowy Garek został zrzucony z odrzutowca na pole o
współrzędnych (0, 0) – oczywiście, w wyniku zrzucenia
żarówka na polu (0, 0) zapaliła się. Garek zdezorientowany
tą sytuacją zaczął wykonywać losowe ruchy dokładnie w
taki sposób, jak na skoczka przystało. Skoczek może
wykonać każdy z ośmiu skoków pokazany na rysunku z
równym prawdopodobieństwem.
Zadanie polega na zaimplementowaniu funkcji:
jump( M )
która zwraca liczbę zapalonych żarówek, po wykonaniu wszystkich ruchów znajdujących się w
tablicy M. Tablica M zawiera listę oznaczeń tak jak na powyższym rysunku, a i-ty element w tej
tablicy odpowiada za (i+1)-ty ruch Garka.
"""

# Complexity -> O(n), gdzie n to liczba skoków Garka
# Tworzymy słownik i dodajemy do niego współrzędne startowe, następnie iterujac przez ruhcy skoczka odpowiednio
# aktualizujemy jego wspołrzędne i sprawdzamy czy dane współrzędne figurują w słowniku pod danym kulczem.Jeśli tak ,
# to usuwamy je, w przeciwynm przypadku dodajemy je do słownika.Na koniec zwracamy liczbę elementów w słowniku.
def jump(move: list[str]):
    x, y = 0, 0

    filed_set = {}
    filed_set.update({f'{x},{y}': (x, y)})

    for el in move:
        if el == 'UL':
            x, y = x-1, y+2
        elif el == 'UR':
            x, y = x+1, y+2
        elif el == 'RU':
            x, y = x+2, y+1
        elif el == 'RD':
            x, y = x+2, y-1
        elif el == 'DR':
            x, y = x+1, y-2
        elif el == 'DL':
            x, y,  = x-1, y-2
        elif el == 'LD':
            x, y = x-2, y-1
        elif el == 'LU':
            x, y = x-2, y+1

        temp = filed_set.get(f'{x},{y}')
        if temp:
            filed_set.pop(f'{x},{y}')
        else:
            filed_set.update({f'{x},{y}': (x, y)})
    return len(filed_set)

runtests(jump, all_tests =True)

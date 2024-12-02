from egz1btesty import runtests
from collections import deque


"""
Dane jest drzewo binarne opisane przez następujące klasy:
class Node:
def __init__( self ):
self.left = None # lewe poddrzewo
self.right = None # prawe poddrzewo
self.x = None # pole do wykorzystania przez studentów
Mówimy, że takie drzewo jest ładne jeśli wszystkie jego liście znajdują się na jednym poziomie.
Szerokością ładnego drzewa jest jego liczba liści a wysokością poziom, na którym te liście się znaj-
dują (korzeń jest na poziomie 0, jego dzieci na poziomie 1, jego wnuki na poziomie 2 itd.). Zadanie
polega na zaimplementowaniu funkcji:
def widentall( T )
która dla danego drzewa T zwraca minimalną liczbę krawędzi, które trzeba usunąć, żeby powstało
ładne drzewo, którego szerokość jest jak największa i którego wysokość jest największa wśród drzew
o maksymalnej szerokości. Usunięcie krawędzi odcina całe poddrzewo poniżej tej krawędzi.
"""

# Złożoność obliczeniowa: O(n)

# Opis algorytmu:

# Pole x klasy Node to 3-elementowa tablica, zawierająca po koleji:
# poziom na którym znajduje się wierzchołek, wskaźnik na rodzica (parent), informację czy wierzchołek jest potrzebny
# czy nie (czy możemy go usunąć)

# Kroki:
# 1) Zaczynamy od wyliczenia wysokości całego drzewa przechodząc po każdym wierzchołku,
# przy okazji aktualizujemy zawartość pola x każdego Node'a. -> O(n)
# 2) Tworzymy tablicę Levels i uzupełniamy ją o informację o szerokości drzewa dla każdego z poziomów -> O(n)
# 3) Obliczamy maksymalną szerokość drzewa, szukając max'a w tablicy Levels -> O(n)
# 4) Obliczamy najwyższy poziom drzewa, na którym szerokość jest równa maksymalnej szerokości drzewa -> O(n)
# 5) Usuwamy krawędzie do dzieci wierzchołków o wysokości height, a liście drzewa o wysokości mniejszej niż height
# dodajemy do kolejki To_remove. Dodatkowo oznaczamy wierzchołki, których nie możemy usunąć, idąc od wierzchołka
# nieusuwalnego w stronę korzenia, przez parent'y. Przez dany wierzchołek możemy przejść tylko raz, bo zostanie on
# oznaczony i następnym razem drogę zablokuje stosowny if, dlatego złożoność O(n) -> O(n)
# 6) Usuwamy odnogi wierzchołków zapisanych w kolejce, wykorzystując informację, który może być usunięty, a który nie.
# Złożoność O(n) z tego samego powodu co wyżej - nie przejdziemy 2 razy przez ten sam wierzchołek -> O(n)


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # pole do wykorzystania przez studentow


def wideentall(tree):
    # 1) Liczymy wysokość całego drzewa i aktualizujemy zawartość pola x - O(n)
    max_height = 0
    height = 0
    tree.x = [0, None, True]
    d_queue = deque()
    d_queue.append(tree)
    # Znajdujemy wysokość drzewa oraz dla każdego wierzchołka ustawiamy pole x jak tablicę, zawierającą informację o
    # wysokości na jakiej znajduje się wierzchołek, jego rodzicu oraz czy można go usunąc czy nie.
    while d_queue:
        node = d_queue.popleft()
        max_height = max(max_height, node.x[0])

        if node.left is not None:
            node.left.x = [node.x[0] + 1, node, False]
            d_queue.append(node.left)

        if node.right is not None:
            node.right.x = [node.x[0] + 1, node, False]
            d_queue.append(node.right)

    max_height += 1

    # 2) Uzupełniamy tablicę levels - O(n)

    levels = [0 for _ in range(max_height)]

    d_queue.append(tree)
    # Dla każdego poziomu drzewa znajdujemy jego szerokość
    while d_queue:
        node = d_queue.popleft()
        levels[node.x[0]] += 1

        if node.left is not None:
            d_queue.append(node.left)

        if node.right is not None:
            d_queue.append(node.right)

    # 3) Obliczamy max_width - O(n)

    max_width = max(levels)

    # 4) Obliczamy height - O(n)
    # Znajdujemy wysokość najszerszego poziomu
    for i in range(max_height - 1, -1, -1):
        if levels[i] == max_width:
            height = i
            break

    # 5) Usuwamy część I - O(n)
    removed = 0

    d_queue.append(tree)
    to_remove = deque()

    while d_queue:
        node = d_queue.popleft()

        if node.x[0] == height:  # nie dodajemy dzieci

            if node.left is not None:
                node.left = None
                removed += 1

            if node.right is not None:
                node.right = None
                removed += 1

            node.x[2] = True
            while node.x[1] is not None:
                node = node.x[1]
                if node.x[2] is True:
                    break
                node.x[2] = True

        else:  # dodajemy dzieci

            if node.left is not None:
                d_queue.append(node.left)

            if node.right is not None:
                d_queue.append(node.right)

            if node.left is None and node.right is None:  # Dodajemy wierzchołek do kolejki, żeby usunąć odnogę
                to_remove.append(node)

    # 6) Usuwamy odnogi wierzchołków zapisanych w kolejce - O(n)
    while to_remove:
        node = to_remove.popleft()
        if node.x[2] is None:
            continue

        while node.x[1] is not None:
            node.x[2] = None
            node = node.x[1]

            if node.x[2] is True:
                removed += 1
                break

            if node.x[2] is None:
                break

    return removed


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=True)

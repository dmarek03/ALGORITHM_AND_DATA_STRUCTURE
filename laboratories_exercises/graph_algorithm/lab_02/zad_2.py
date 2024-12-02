"""
Stwierdzenie czy graf zawiera dobry początek.
Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli każdy inny wierzchołek w tym grafie jest osiągalny
ścieżką wychodzącą z tego wierzchołka .


1.Szukamy podgrafów złożonych z silnych spójnych składowowych
2.Sortujemy topologicznie uzyskane podgrafy
3.Sprawdzamy dla pierwszego wierzchołka dfs czy da się osiągnać wszytskie inne wierzchołki


1.Szukamy wierzchołka z największym czasem przetworzenia
2. Dla tego wierzchołka sprawdzamy DFS czy da się osiągnac wszytskie inne wierzchołki
"""
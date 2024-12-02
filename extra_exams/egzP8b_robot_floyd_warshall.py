from egzP8btesty import runtests
import copy
from math import inf

"""
Szablon rozwiązania
Złożoność akceptowalna (1.5pkt):O(n^3logn)
Złożoność wzorcowa (+2.5pkt):O(n^3), gdzie n to liczba punktów na hali
Pewna duża amerykańska firma technologiczna postanowiła zorganizować wyścigi
autonomicznych robotów. Wyścigi odbyły się na potężnej prostokątnej hali, która dla tego celu
została w pełni opróżniona. Na podłodze zostały umieszczone naklejki w dwóch kolorach. Białe
oznaczają punkty zmiany kierunku, a szare to punkty kontrolne (które oczywiście jednocześnie
pełnią również role punktów białych). Roboty wyposażone są w kamery oraz dobre oświetlenie,
co pozwala im rozpoznać, że znajdują się na punkcie danego koloru. Ze względu na zastosowane
technologie, autonomiczne roboty po najechaniu na punkt, wybierają kolejny punkt swojej trasy,
a następnie zmieniają swój kierunek oraz decydują o odległości, którą przebędą (tj. jeżeli określą
następny punkt, to wszystkie punkty na trasie do niego zostaną zignorowane). Między dwoma
punktami zawsze poruszają się w linii prostej. W trakcie trasy muszą odwiedzić one wszystkie
punkty kontrolne w określonej przez organizatora kolejności, przebywając łącznie jak najkrótszy
dystans. Rozwiązanie zadania byłoby oczywiste, gdyby nie to, że na hali zostały rozmieszczone
przeszkody. Do pamięci robota została wgrana przygotowana mapa w postaci grafu ważonego i
musi zdecydować on o kolejności odwiedzenia punktów.
Zadanie polega na zaimplementowaniu funkcji:
def robot( G, P )
która oblicza dystans, który pokona robot, przy następujących założeniach.
 1. Graf ważony G jest wyrażony jako lista sąsiedztwa, dla każdych dwóch punktów u oraz v,
pomiędzy którymi nie znajduje się żadna przeszkoda, oddalonych od siebie o x cm, lista G[u]
będzie zawierała krotkę (v, x) oraz lista G[v] będzie zawierała krotkę (u, x)
 2. Tablica P zawiera listę szarych punktów, ich numeracja odpowiada wierzchołkom z grafu G,
w kolejności, w której muszą zostać odwiedzone. Robot zaczyna swoją trasę w pierwszym
punkcie, a kończy w ostatnim. Wierzchołki w tablicy P są unikalne.
 3. Można założyć, że przeszkody zostały umieszczone w taki sposób, że dana przeszkoda
wyklucza poruszanie się tylko między jedną parą punktów na hali, a także, że ich ilość jest
marginalna względem ilości wszystkich możliwych par punktów.
Rozważmy następujące dane:
G = [
 [(1, 3), (2, 3)],
 [(0, 3), (4, 4)],
 [(0, 3), (3, 1), (4, 4)],
 [(2, 1), (4, 2)],
 [(1, 4), (2, 4), (3, 2)]
]
P = [0, 3, 4]
Wywołanie robot( G, P )powinno zwrócić wynik 6 (Odwiedzamy punkty 0 – 2 – 3 – 4 )
"""

# COMPLEXITY O(V^3)
# Za pomocą algorytmu floyda_warshalla znajdujemy najkrótsze ścieżki między każdą parą wierzchołków. Następnie
# przechodząc przez listę obowiązkowych punktów P sumuje wartośći pomiedzy koljenymi punktami.Finalna suma jest
# rozwiązaniem zadania


def floyd_warshall_algorithm(matrix):
    n = len(matrix)

    # Create a copy of a graph as we have to have lengths
    # of edges stored at the beginning of an algorithm
    W = copy.deepcopy(matrix)

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]

    return W


def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    matrix = [[inf]*n for _ in range(n)]
    for vertex, neighbors in enumerate(adj_list):
        for neighbor, weight in neighbors:
            matrix[vertex][neighbor] = weight

    return matrix


def robot( G, P ):
    matrix = adjacency_list_to_matrix(G)
    distances = floyd_warshall_algorithm(matrix)
    min_dist = 0

    for i in range(len(P)-1):
        min_dist += distances[P[i]][P[i+1]]
    return min_dist

    
runtests(robot, all_tests = True)

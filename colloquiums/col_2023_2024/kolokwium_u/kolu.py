from kolutesty import runtests
from collections import deque, defaultdict

def create_adj_list(edges_list, n):

    graph = [[] for _ in range(n)]


    for u, v in edges_list:
        graph[v].append(u)

    return graph

def dfs(graph, source, visited, result):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result)
    # Inserting the processed vertex at the top of the results list
    result.insert(0, source)


def topological_sort(graph:list[list[int]]):
    n = len(graph)
    visited = [False] * n
    result = []
    for u in range(n):
        if not visited[u]:
            dfs(graph, u, visited, result)
    return result



def projects1(n: int, L):



    graph = create_adj_list(L, n)

    res = topological_sort(graph)



    dist = [0]*n
    for vertex in res:
        for neighbour in graph[vertex]:


            dist[neighbour] = max(dist[neighbour], dist[vertex]+1)

    return max(dist)+1



def projects(n, L):

    graph = defaultdict(list)
    in_degree = [0] * n

    # Tworzymy z listy zadań graf w postaci listy krawędzi oraz tworzymy listę in_degree,gdzie
    # in_degree[i] oznacza liczbę zadań, które muszą byc wykonane przed rozpoczęciem i-tego zadania
    for p, q in L:
        graph[q].append(p)
        in_degree[p] += 1

    # Kolejka do BFS z początkowymi wierzchołkami o zerowym in_degree
    queue = deque([i for i in range(n) if in_degree[i] == 0])

    # Zmienna do śledzenia liczby jednostek czasu
    time_units = 0


    # Następnie dopóki będą jeszcze zadania do wykonania, znajduję liczbę projektów możliwych
    # do wykonania w danej jednostce czasu jako obecny rozmiar kolejki.Następnie po kolejki pobieramy projekty z kolejki
    # i dla każdego przetwarzanego projektu zmniejszamy o jeden wartośći w tablicy in_degree dla jego sąsiadów.Jesli
    # wartość  w tablicy in_degree dla , któregoś z sąsiadów osiągnie wartość zero(co znaczy,że wszystkie zadania,
    # które nalezało wykonac przed nim zostały realizowane) to dodajemy go do kolejki, aby zostało przetworzone w
    # kolejnej jednostce czasu . Po przetworzeniu wszystkich zadań z danej jednostki czasu, zwiększamy zmienną
    # zliczającą czas potrzebny do wykonania wszystkich zadań.
    # Po prztowrzeniu wszystkich zadań zwracamy obliczony czas realizacji zadań.
    while queue:
        # Zmienna do śledzenia liczby projektów w bieżącej warstwie BFS
        num_projects = len(queue)

        # Przetwarzanie bieżącej warstwy BFS
        for _ in range(num_projects):
            project = queue.popleft()

            # Przetwarzanie sąsiadów bieżącego projektu
            for neighbor in graph[project]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Zwiększenie liczby jednostek czasu po przetworzeniu bieżącej warstwy
        time_units += 1

    return time_units



runtests( projects1, all_tests = True )

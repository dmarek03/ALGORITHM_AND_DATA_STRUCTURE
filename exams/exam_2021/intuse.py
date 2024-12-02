
# Dany jest zbiór przedziałów domkniętych I = {[a1, b1], ..., [an, bn]} gdzie każdy przedział zaczyna
# się i kończy na liczbie naturalnej (wliczając 0). Dane są także dwie liczby naturalne x i y. Dwa
# przedziały można skleić (czyli zamienić na przedziały będące ich sumą mnogościową) jeśli mają
# dokładnie jeden punkt wspólny. Jeśli pewne przedzoały można posklejać tak, że powstaje z nich
# przedział [x, y] to mówimy, że są przydatne. Proszę napisać funkcję:
# def intuse(I, x, y):
#     ...
# która zwraca listę numerów wszystkich przydatnych przedziałów. Zbiór I jest reprezentowany jako
# lista par opisujących przedziały. Proszę oszacować złożoność czasową i pamięciową użytego algorytmu.

# Complexity O(nlogn)
def binary_search(tab, x):
    left = 0
    right = len(tab) - 1
    while left <= right:
        mid = (left + right) // 2
        if tab[mid] == x:
            return mid
        elif tab[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def dfs(graph, visited, u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)


def intuse(intervals, x, y):
    tab = []
    for i in range(len(intervals)):
        tab.append(intervals[i][0])
        tab.append(intervals[i][1])
    tab.sort()
    print(f'{intervals=}')
    vertices = [tab[0]]
    idx = 0
    for i in range(1, len(tab)):
        if tab[i] != vertices[idx]:
            vertices.append(tab[i])
            idx += 1
    result = []
    print(f'{vertices=}')
    if binary_search(vertices, x) == -1 or binary_search(vertices, y) == -1:
        return result
    x_graph = [[] for _ in range(len(vertices))]
    y_graph = [[] for _ in range(len(vertices))]
    for i in range(len(intervals)):
        value_1 = binary_search(vertices, intervals[i][0])
        value_2 = binary_search(vertices, intervals[i][1])
        print(f'{value_1=}')
        print(f'{value_2=}')

        x_graph[value_1].append(value_2)
        y_graph[value_2].append(value_1)
    print(f'{x_graph=}')
    print(f'{y_graph=}')
    x_visited = [False] * len(vertices)
    dfs(x_graph, x_visited, binary_search(vertices, x))
    y_visited = [False] * len(vertices)
    dfs(y_graph, y_visited, binary_search(vertices, y))
    for i in range(len(intervals)):
        value_1 = binary_search(vertices, intervals[i][0])
        value_2 = binary_search(vertices, intervals[i][1])
        if x_visited[value_1] and y_visited[value_2]:
            result.append(i)
    return result



intervals = [(3, 4), (2, 5), (1, 3), (4, 6), (1, 4)]
x1 = 1
y1 = 6

print(intuse(intervals, x1, y1))

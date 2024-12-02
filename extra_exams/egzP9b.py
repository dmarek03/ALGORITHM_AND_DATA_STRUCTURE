from egzP9btesty import runtests

# Złożoność O(ElogE)
# Najpierw usuwam z grafu G wszytskie krawędzie, które są remontowane.Następnie na tak przygotowanym grafie znajduje
# cykl Eulera , co jest rozwiązaniem tego zadania.


def remove_edges(G, R):
    new_G = [adj_list.copy() for adj_list in G]
    for u in range(len(R)):
        for v in R[u]:
            if v in new_G[u]:
                new_G[u].remove(v)
    return new_G


def find_eulerian_cycle(graph):
    n = len(graph)
    in_degree = [0] * n
    out_degree = [0] * n
    for u in range(n):
        for v in graph[u]:
            out_degree[u] += 1
            in_degree[v] += 1

    # Sprawdzenie czy każdy wierzchołek ma równe stopnie wejściowe i wyjściowe
    for i in range(n):
        if in_degree[i] != out_degree[i]:
            return []

    stack = [0]
    current_path = []

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            stack.append(v)
        else:
            current_path.append(stack.pop())

    return current_path[::-1]


def dyrektor(G, R):
    new_G = remove_edges(G, R)
    return find_eulerian_cycle(new_G)


runtests(dyrektor, all_tests=True)
class Node:
    def __init__(self):
        self.left = None  # Lewe poddrzewo
        self.right = None  # Prawe poddrzewo
        self.x = None  # Pole do wykorzystania przez studentów

def minEdgesToRemove(root):
    if not root:
        return 0, 0

    # Rekurencyjnie znajdujemy minimalną liczbę krawędzi do usunięcia
    # w lewym i prawym poddrzewie.
    left_min, left_height = minEdgesToRemove(root.left)
    right_min, right_height = minEdgesToRemove(root.right)

    # Minimalna liczba krawędzi do usunięcia w bieżącym poddrzewie.
    current_min = min(left_min + right_height, right_min + left_height)

    # Wysokość bieżącego poddrzewa.
    current_height = 1 + max(left_height, right_height)

    return current_min, current_height
A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G


print(f'{minEdgesToRemove(A)=}')



def findEdgesToRemove(root):
    if not root:
        return []

    edges_to_remove = []

    def dfs(node):
        nonlocal edges_to_remove
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        if left_height + right_height == 0:
            return 1  # Oznacza, że to jest liść, nie usuwamy go.

        if left_height > right_height:
            edges_to_remove.append((node, node.left))

        else:
            edges_to_remove.append((node, node.right))


        return 1 + max(left_height, right_height)

    dfs(root)
    return [(parent.x, child.x) for parent, child in edges_to_remove]

A = Node()
B = Node()
C = Node()
A.left = B
A.right = C
D = Node()
E = Node()
B.left = D
B.right = E
F = Node()
E.right = F
G = Node()
F.right = G

print(f'{findEdgesToRemove(A)=}')
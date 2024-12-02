from egzP4btesty import runtests
"""
Dane jest drzewo BST opisane przez następujące klasy:
 class Node:
def __init__( self, key, parent ):
 self.left = None # lewe poddrzewo
 self.right = None # prawe poddrzewo
 self.parent = parent # rodzic
 self.key = key # wartość wierzchołka
 self.x = None # pole do wykorzystania przez studentów
Mówimy, że wierzchołek takiego drzewa jest ładny jeżeli jego wartość jest średnią arytmetyczną
wartości jego poprzednika oraz następnika. (Poprzednikiem wierzchołka nazywamy największy
wierzchołek w drzewie BST mniejszy od niego, a następnikiem najmniejszy wierzchołek większy
od niego. Oczywiście jako „najmniejszy”/”największy” rozumiemy wierzchołek o najmniejszej lub
odpowiednio największej wartości). Zadanie polega na zaimplementowaniu funkcji:
 def averagesum( T, root )
która dla danego drzewa o korzeniu root oraz tablicy wierzchołków T będących pewnymi
wierzchołkami tego drzewa, zwraca sumę wartości wszystkich ładnych wierzchołków tego
drzewa, jednocześnie będących elementami tablicy T. Można założyć, że wierzchołki o wartości
najmniejszej oraz największej nie znajdują się w tablicy T, oraz, że nie zawiera ona powtórzeń. .
"""

#O(qh), gdzie n to całkowita liczba wierzchołków drzewa BST,h to jego wysokość, a q to rozmiar tablicy T.
# Za pomocą funkcji node_prev oraz node_next dla każdego wierzchołka z drzewa sprawdzamy czy zachodzi, że jest on sumą
# swojego porzednika i następnika. Jeśli tak do dodajemy go do naszje sumy, którą finalanie zwracamy.
class Node:
    def __init__(self, key, parent):
        self.left = None
        self.right = None
        self.parent = parent
        self.key = key
        self.x = None


def walk(root: Node, tab):
    if root.left:
        walk(root.left, tab)
    tab.append(root.key)

    if root.right:
        walk(root.right, tab)


def iterative_binary_search(tab, left: int, right: int, x: int) -> int:

    while left <= right:
        mid = (left+right)//2

        if tab[mid] == x:
            return mid

        if tab[mid] > x:
            right = mid-1

        elif tab[mid] < x:
            left = mid+1

    return -1


def sol(root, T):
    tab = []
    walk(root, tab)
    n = len(tab)
    pretty_root_sum = 0

    for el in T:
        x = iterative_binary_search(tab, 0, n-1, el.key)
        if tab[x-1] + tab[x+1] == 2 * tab[x]:
            pretty_root_sum += tab[x]

    return pretty_root_sum


def max_val(root):
    curr = root
    while curr:
        if not curr.right:
            break
        curr = curr.right
    return curr


def min_val(root):
    curr = root
    while curr:
        if not curr.left:
            break
        curr = curr.left
    return curr


def node_prev(root):
    if root.left:
        return max_val(root.left)
    p_root = root.parent
    while p_root:
        if root != p_root.left:
            break
        root = p_root
        p_root = p_root.parent
    return p_root


def node_next(root):
    if root.right:
        return min_val(root.right)
    n_root = root.parent
    while n_root:
        if root != n_root.right:
            break
        root = n_root
        n_root = n_root.parent
    return n_root


def sol1(root, T):

    pretty_root_sum = 0

    for el in T:
        prev_el = node_prev(el)
        next_el = node_next(el)
        if prev_el.key + next_el.key == 2 * el.key:
            pretty_root_sum += el.key

    return pretty_root_sum


runtests(sol, all_tests=True)

"""
Zadanie offline 1.
Szablon rozwiązania: zad1_nieparzysty_palindrom.py
Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
def __init__(self):
self.val = None # przechowywana liczba rzeczywista
self.next = None # odsyłacz do nastepnego elementu
Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1, a2, . . . , an
(lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi,
że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej
o najwyżej k. Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest
1, 0, 3, 2, 4, 6, 5, a (n − 1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności.
Proszę zaimplementować funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p.
Funkcja powinna zwrócić wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy
oraz używać jak najmniej pamięci (w sensie asymptotycznym, mierzonym względem długości n listy
oraz parametru k). Proszę skomentować jego złożoność czasową dla k = Θ(1), k = Θ(log n) oraz
k = Θ(n).
"""



def __init__(self):
    self.val = None
    self.next = None


def sorted_insert(head, new_node):
    # Checking if the list exist or whether we can swap present head
    if head is None or head.val >= new_node.val:
        new_node.next = head
        head = new_node
    else:

        actual = head
        # Going through the list until we find a correct place for the new value
        while actual.next is not None and actual.next.val < new_node.val:
            actual = actual.next
        # Adding the new node in a correct place
        new_node.next = actual.next
        actual.next = new_node

    return head


def insertion_sort(head):
    is_sorted = None
    current = head

    while current is not None:
        # making a temp variable to increment the current
        nxt_node = current.next
        # Creating a sorted list
        is_sorted = sorted_insert(is_sorted, current)
        current = nxt_node

    head = is_sorted

    return head


def SortH(p, k):
    return k if p == 0 else insertion_sort(p)










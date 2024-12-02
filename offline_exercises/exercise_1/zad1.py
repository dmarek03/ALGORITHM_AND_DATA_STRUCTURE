from zad1testy import Node, runtests
# DOMINIK MAREK
# W celu posortowania k-chaotycznej listy odsyłaczowej korzystam z algortymu sortowania przez wybieranie,
# z jedną modyfikacją polegającą na tym że dla każdego elementu listy odsyłaczowej przeglądam dokładnie k kolejnych
# węzłów , gdyż z defincji zadania wynika, ze elementy mogą być maksymalnie oddalone o k pozycji względem
# pozycji w liście posortowanej.
# Złożoność obliczeniowa 0(nk) co dla poszczególnych wartości k daje następujące złożoności:
# 1) Dla k = 0(1) => 0(n)
# 2) Dla k = 0(logn) => 0(nlogn)
# 3) Dla k = 0(n) => 0(n^2)

def print_list(p):
    tab = [0] * get_length(p)
    i = 0
    while p.next:
        tab[i] = p.val
        p = p.next
        i += 1
    tab[-1] = p.val
    print(f'{tab=}')


def get_length(p: Node) -> int:
    if p is None:
        return 0
    if p.next is None:
        return 1
    cnt = 1

    while p.next:
        cnt += 1
        p = p.next

    return cnt


def normalized_linked_list(p: Node):
    s = p
    if s is None:
        return [p]
    node_tab = [0]*get_length(s)

    i = 0

    while s.next:
        node_tab[i] = s
        s = s.next
        i += 1

    node_tab[-1] = s

    return node_tab


def tab_to_linked_list(tab):
    s = tab[0]
    tmp = s
    for t in tab[1:]:
        s.next = t
        s = t
    s.next = None
    return tmp


def swap_values(tab, p):
    temp = p
    for t in tab:
        p.val = t
        p = p.next

    return temp


def selection_sort(tab, k):
    n = len(tab)
    for i in range(n):
        min_val_idx = i

        for j in range(i+1, min(n, i+k+1)):
            if tab[j].val < tab[min_val_idx].val:
                min_val_idx = j

        if min_val_idx != i:
            tab[min_val_idx], tab[i] = tab[i], tab[min_val_idx]


def selectionSort(head, k):
    temp = head

    while head:

        min_node = head
        r = head.next
        i = 0

        while r and i <= k:
            if min_node.val > r.val:
                min_node = r

            r = r.next
            i += 1

        if min_node != head:
            x = head.val
            head.val = min_node.val
            min_node.val = x
        head = head.next

    return temp


def SortH(p, k):
    return selectionSort(p, k) if k > 0 else p


runtests(SortH, all_tests=True)
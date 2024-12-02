"""
Sortowanie listy odsyłaczowej -> selection_sort

"""
from dataclasses import dataclass


@dataclass
class Node:
    next = None
    val = None


def selection_sort(p: Node):
    if p.next is None or p is None:
        return p
    guard = Node()
    result = guard
    j = Node()
    j.next = p
    while j is not None:
        min_val_node = j
        p = j
        while p.next is not None:
            if p.val < min_val_node.next.val:
                min_val_node = p
            p = p.next
        guard.next = min_val_node.next
        min_val_node.next = min_val_node.next.next
        guard = guard.next
        guard.next = None

    return result.next



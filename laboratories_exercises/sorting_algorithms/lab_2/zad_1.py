"""
Merge sort na lista jednokierunkwoych, wykorzystując istniejące już posorotwane serie naturalne O(nlogn)
Odcinamy dwie serie naturalne i scalamy i potem birzemy kolejne dwie i powtarzamy czynność => O(logn)
"""

class Node:
    def __int__(self):
        self.val = None
        self.next = None


def merge(head1, head2):
    guard = Node()
    tail = guard

    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
        else:
            tail.next = head1

        head1 = head1.next
        head2 = head2.next

    tail.next = head1 if head1 else head2

    return guard.next


def splitList(head):
    tmp = head
    while tmp.next and tmp.val < tmp.next.val:
        tmp = tmp.next

    head2 = tmp.next
    tmp.next = None
    return head, head2


def merge_sort(head):
    flag = True
    while flag:
        flag = False
        tail = sorted_tail = Node()
        while head:
            part1, head = splitList(head)
            if not head:
                tail.next = part1

            else:
                part2, head = splitList(head)
                tail.next = merge(part1,part2)
                while tail:
                    tail = tail.next

        head = sorted_tail.next

    return head


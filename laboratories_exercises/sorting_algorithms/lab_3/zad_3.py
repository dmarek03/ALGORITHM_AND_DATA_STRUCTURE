"""
Wstawianie do minHeap
"""


class Heap:
    def __int__(self, max_size):
        self.max_size = max_size
        self.T = [None] * max_size
        self.size = 0

    @staticmethod
    def heap_add(H, x):
        if H.size < H.max_size:
            decrease_key(H.T, H.size, x)
            H.size += 1


def parent(idx: int) -> int:
    return abs(idx-1)//2

# Działa tylko gdy element pod indeksem i jest większy od
def decrease_key(tab,i,x):
    p = parent(i)
    tab[i] = x
    while tab[p] > tab[i]:
        tab[p], tab[i] = tab[i], tab[p]
        i = p
        p = parent(i)

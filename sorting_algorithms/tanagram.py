from tanagram_test import runtests


def into_histogram(text: str) -> list[int]:
    histo = [0] * 26
    for t in text:
        histo[ord(t)-97] += 1
    return histo


def get_min_max(tab) -> tuple[int, int]:
    min_val = min(ord(t[0]) for t in tab)
    max_val = max(ord(t[0]) for t in tab)
    return min_val, max_val


def counting_sort(tab, fn):
    min_val, max_val = get_min_max(tab)
    n = len(tab)
    count_tab = [0]*(max_val-min_val+1)
    sorted_tab = [0]*n

    for i in range(n):
        count_tab[fn(tab[i])-min_val] += 1

    for i in range(1, len(count_tab)):
        count_tab[i] += count_tab[i-1]

    for i in range(n-1, -1, -1):
        sorted_tab[count_tab[fn(tab[i])-min_val]-1] = tab[i]
        count_tab[fn(tab[i])-min_val] -= 1

    for i in range(n):
        tab[i] = sorted_tab[i]


def tanagram(x: str, y: str, t: int) -> bool:

    if len(x) != len(y):
        return False

    n = len(x)

    t1 = [[s, i] for i, s in enumerate(x)]
    t2 = [[s, i] for i, s in enumerate(y)]

    counting_sort(t1, fn=lambda z: ord(z[0]))
    counting_sort(t2, fn=lambda z: ord(z[0]))

    for i in range(n):
        if t1[i][0] != t2[i][0] or abs(t1[i][1]-t2[i][1]) > t:
            return False
    return True


runtests(tanagram)



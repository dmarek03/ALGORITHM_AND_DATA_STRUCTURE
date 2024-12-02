"""
Lider ciągu
"""


def find_leader(tab):
    n = len(tab)
    max_el = max(tab) + 1
    count = [0] * max_el
    for i in range(n):
        count[tab[i]] += 1

    for i in range(max_el):
        if count[i] > n//2:
            return i
    return None


def leader_2(tab: list[int]) -> int:
    leader = tab[0]
    cnt = 1
    for t in tab:
        if t == leader:
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            leader = t
    new_cnt = 1
    for t in tab:
        if t == leader:
            new_cnt += 1

    return leader if new_cnt > (len(tab) // 2) else None

print(leader_2([2, 4,3, 3, 3, 3]))


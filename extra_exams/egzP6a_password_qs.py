from egzP6atesty import runtests
import re
# Complexity ->O(nk), gdzie n to liczba haseł, a k to max. długość hasła
# Za pomocą funkcji quick_select znajdujemy najsłabsze hasło spełniające założenia bezpieczeństwa.
def partition(tab: list[str], left: int, right: int) -> int:

    pivot = tab[right]

    i = left - 1

    for j in range(left, right):
        if comparator(tab[j], pivot) < 0:
            i += 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i+1], tab[right] = tab[right], tab[i+1]

    return i + 1


def count_letters(text: str) -> int:
    return len(re.sub(r'\d?', '', text))


def comparator(pas1: str, pas2: str):
    if len(pas1) == len(pas2):
        return count_letters(pas1) - count_letters(pas2)
    return len(pas1) - len(pas2)


def quick_select(tab: list[str], left: int, right: int, x: int):
    if left == right:
        return tab[right]

    pos = partition(tab, left, right)

    if pos == x:
        return tab[x]

    elif pos > x:
        return quick_select(tab, left, pos-1, x)

    else:
        return quick_select(tab, pos+1, right, x)


def google( H, s ):

    password = quick_select(H, 0, len(H)-1, len(H)-s)
    # print(f'{H=}')
    # print(f'{password=}')
    return password



runtests (google, all_tests=1)

# H = ['aba', 'abc', 'ab1', 'abab', 'a1a1', 'aa12a']
# s = 3
# print(google(H, s))
#
# print(comparator('abab', 'a1a1'))
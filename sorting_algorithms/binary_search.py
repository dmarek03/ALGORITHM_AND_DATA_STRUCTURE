"""
BINARY SEARCH
"""
import random


def recursively_binary_search(tab: list[int], left: int, right: int, x: int) -> int:

    if left < right:

        mid = (left + right)//2

        if tab[mid] == x:
            return mid

        if tab[mid] > x:
            return recursively_binary_search(tab, left, mid-1, x)

        if tab[mid] < x:
            return recursively_binary_search(tab, mid+1, right, x)

    return -1


def iterative_binary_search(tab: list[int], left: int, right: int, x: int) -> int:

    while left <= right:
        mid = (left+right)//2

        if tab[mid] == x:
            return mid

        if tab[mid] > x:
            right = mid-1

        elif tab[mid] < x:
            left = mid+1

    return -1


T = sorted([random.randint(10, 100) for _ in range(20)])

print(T)

print(recursively_binary_search(T, 0, len(T)-1, 13))
print(iterative_binary_search(T, 0, len(T)-1, 11))
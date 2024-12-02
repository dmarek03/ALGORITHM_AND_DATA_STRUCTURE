"""
RADIX SORT
"""
from random import randint

def counting_sort(T, k):
    sorted_array = [0]*len(T)
    count_array = [0]*10
    for i in range(len(T)):
        index = (T[i] // k) % 10
        count_array[index] += 1
    for i in range(1, 10):
        count_array[i] += count_array[i-1]

    for j in range(len(T)-1, -1, -1):
        index = (T[j] // k) % 10
        sorted_array[count_array[index]-1] = T[j]
        count_array[index] -= 1

    for i in range(len(T)):
        T[i] = sorted_array[i]


def radix_sort(T):
    maximum = max(T)
    i = 1
    print(f'{T=}')
    while maximum//i > 0:
        counting_sort(T, i)
        print(f'{T=}')
        i *= 10


T = [randint(1, 100) for _ in range(10)]

radix_sort(T)
print(T)
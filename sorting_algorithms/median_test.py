import random
from collections import defaultdict

T1 = [[1, 2], [3, 4]]
T2 = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
T3 = [[2, 5, 2, 5], [2, 5, 5, 2], [2, 5, 2, 2], [2, 5, 5, 5]]
T4 = [[43, 74, 53, 97], [80, 61, 61, 19], [61, 73, 89, 93], [42, 17, 89, 80]]

TESTS = [T1, T2, T3, T4]


def isok(T):
    N = len(T)
    for r in range(1, N):
        for c in range(r):
            for d in range(N):
                if T[r][c] > T[d][d]: return False
                if T[c][r] < T[d][d]: return False
    return True


def printT(T):
    N = len(T)
    for row in T: print(row)
    print()


def runtests(f):
    OK = True
    for T in TESTS:
        print("----------------------")
        print("Dane:")
        printT(T)
        f(T)
        print("Wynik:")
        printT(T)

        if not isok(T):
            print("Blad!")
            OK = False
    print("----------------------")

    if OK:
        print("OK!")
    else:
        print("Bledy!")


def random_matrix(n, range_=(0, 100)):
    return [[random.randint(*range_) for _ in range(n)] for _ in range(n)]


def random_tests(fn, size=(1, 20), range_=(0, 100), samples=10):
    passed = 0
    for i in range(1, samples + 1):
        n = random.randint(*size)
        matrix = random_matrix(n, range_)
        init_counts = defaultdict(int)
        for row in matrix:
            for val in row:
                init_counts[val] += 1
        print(f'===== Test #{i}: =====')
        print(f'Input array ({n} x {n}):')
        print(*matrix, sep='\n', end='\n\n')
        fn(matrix)
        final_counts = defaultdict(int)
        for row in matrix:
            for val in row:
                final_counts[val] += 1
        no_dropped_values = init_counts == final_counts
        is_correct = isok(matrix) and no_dropped_values
        passed += is_correct
        print('Result array:')
        print(*matrix, sep='\n', end='\n\n')
        print('Is correct?:', is_correct)
        if not is_correct:
            print('Dropped values?:', not no_dropped_values)
        print(f'Tests already passed: {passed}/{i}', end='\n\n\n')
    print('\n===== Final results: =====')
    print(f'Total tests passed: {passed}/{samples}')
# zad1testy.py
from rectangletesty import *

# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

TESTS = [
    # 0
    {
        "arg": [[(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]],
        "hint": 2
    },
    # 1
    {
        "arg": [[(6, 4, 7, 5), (2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7)]],
        "hint": 0
    },
    # 2
    {
        "arg": [[(2, 3, 10, 6), (3, 1, 8, 8), (5, 4, 9, 7), (1, 1, 2, 2)]],
        "hint": 3
    },
    # 3
    {
        "arg": [[(1, 2, 6, 11), (3, 2, 7, 4), (4, 1, 5, 3), (1, 5, 11, 6)]],
        "hint": 3
    },
    # 4
    {
        "arg": [[(4, 3, 7, 8), (5, 2, 10, 6), (4, 3, 9, 6), (1, 4, 6, 7), (3, 1, 8, 8), (2, 4, 7, 6), (3, 3, 8, 9),
                 (1, 3, 7, 9), (3, 2, 10, 9), (2, 3, 7, 10)]],
        "hint": 1
    },
    # 5
    {
        "arg": [[(4, 2, 19, 19), (5, 5, 19, 15), (4, 5, 20, 19), (2, 5, 16, 15), (5, 3, 17, 19), (2, 2, 18, 16),
                 (5, 5, 6, 6), (3, 4, 15, 16), (3, 2, 18, 18),
                 (4, 1, 15, 15), (3, 4, 19, 15), (1, 3, 17, 16), (4, 3, 20, 18), (2, 3, 19, 19), (2, 4, 18, 20),
                 (2, 1, 19, 16), (4, 1, 18, 19), (3, 1, 15, 16),
                 (5, 2, 18, 17), (3, 4, 15, 20), (4, 3, 16, 20), (5, 4, 19, 16), (3, 2, 18, 19), (3, 4, 19, 20),
                 (1, 5, 17, 19), (3, 3, 16, 20), (1, 2, 15, 17),
                 (2, 5, 19, 19), (4, 3, 15, 16), (5, 4, 19, 15), (2, 5, 18, 17)]],
        "hint": 6
    },
    # 6
    {
        "arg": [[(1, 5, 18, 15), (1, 3, 20, 16), (2, 4, 20, 20), (1, 3, 19, 19), (2, 1, 17, 16), (5, 5, 20, 15),
                 (4, 5, 20, 17), (2, 4, 18, 16), (2, 3, 15, 17),
                 (2, 5, 18, 20), (3, 4, 19, 16), (3, 3, 20, 17), (5, 1, 19, 17), (4, 3, 18, 18), (3, 1, 17, 18),
                 (5, 2, 19, 20), (1, 1, 18, 19), (2, 3, 19, 18),
                 (2, 2, 16, 17), (3, 2, 19, 18), (1, 2, 18, 16), (1, 4, 18, 20), (3, 3, 16, 17), (5, 1, 19, 18),
                 (4, 5, 17, 19), (1, 4, 18, 20), (3, 1, 16, 19),
                 (2, 4, 16, 17), (3, 2, 20, 15), (5, 4, 19, 18), (2, 3, 15, 17), (1, 4, 19, 20), (3, 2, 20, 20),
                 (4, 4, 20, 20), (3, 3, 20, 17), (2, 4, 15, 16),
                 (4, 3, 15, 18), (5, 4, 17, 18), (1, 3, 16, 18), (3, 5, 15, 19), (4, 1, 15, 17), (2, 4, 17, 19),
                 (1, 1, 17, 19), (1, 5, 17, 17), (3, 4, 20, 15),
                 (2, 1, 16, 15), (3, 1, 17, 20), (3, 5, 20, 20), (2, 3, 19, 16), (3, 4, 16, 15), (4, 4, 15, 19),
                 (1, 2, 20, 18), (4, 2, 15, 17), (1, 5, 20, 15),
                 (3, 4, 17, 17), (2, 1, 20, 16), (3, 4, 20, 15), (3, 3, 16, 19), (1, 5, 19, 18), (3, 1, 17, 19),
                 (1, 2, 20, 20), (3, 5, 15, 16), (4, 1, 18, 15),
                 (4, 2, 17, 20), (4, 4, 15, 16), (5, 1, 16, 15), (1, 1, 19, 17), (5, 5, 16, 17), (3, 4, 15, 16),
                 (4, 3, 15, 16), (5, 2, 15, 15), (2, 3, 20, 18),
                 (2, 5, 20, 16), (2, 5, 20, 18), (3, 1, 16, 20), (1, 2, 20, 17), (1, 2, 16, 16), (1, 2, 20, 18),
                 (1, 3, 16, 18), (3, 4, 18, 16), (4, 3, 15, 18),
                 (3, 3, 16, 17), (5, 3, 20, 20), (2, 3, 16, 16), (4, 1, 20, 19), (3, 1, 17, 18), (3, 2, 19, 16),
                 (2, 5, 20, 16), (4, 4, 15, 18), (4, 4, 18, 16),
                 (5, 2, 19, 15), (2, 4, 16, 16), (5, 1, 19, 17), (4, 1, 15, 16), (5, 1, 16, 17), (4, 1, 16, 19),
                 (2, 5, 17, 18), (4, 2, 20, 19), (1, 2, 3, 15), (1, 3, 16, 15)]],

        "hint": 98
    },

]


def printarg(I):
    print("Prostokaty: ", limit(I, 120))


def printhint(hint):
    print("Przykladowy wynik:", limit(hint, 120))


def printsol(sol):
    print("Uzyskany wynik   :", limit(sol, 120))


def check(I, hint, sol):
    if hint == sol:
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False


def runtests(f):
    internal_runtests(printarg, printhint, printsol, check, TESTS, f)
#Exercise_2_tests.py
# from signal import signal, alarm, SIGALRM
from testy import *




# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]



TESTS = [
# 0
  {
    "arg" :[ 8, [(0,4),(2,6)] ],
    "hint": 3
  },
# 1
  {
    "arg" :[ 10, [(0,4),(2,6),(1,6),(2,5),(7,9),(1,7),(1,7),(1,7)] ],
    "hint": 4
  },
# 3
  {
    "arg" :[ 10000, [(x,x+1) for x in range(9998)] ],
    "hint": 9997
  },

# 3
  {
    "arg"  : [10, [(7, 8), (2, 5), (2, 5), (6, 8), (5, 8), (9, 9), (7, 7), (1, 3), (9, 9), (7, 9)]],
    "hint" : 6
  },
# 4
  {
    "arg"  : [16, [(5, 6), (1, 1), (1, 4), (13, 13), (9, 11), (0, 2), (8, 9), (13, 14), (2, 5), (11, 14), (1, 1), (8, 10), (11, 11), (14, 15), (11, 12), (10, 11)]],
    "hint" : 7
  },
# 5
  {
    "arg"  : [20, [(11, 13), (4, 4), (2, 3), (5, 5), (14, 18), (9, 13), (7, 10), (9, 11), (7, 10), (9, 11), (14, 14), (5, 9), (16, 19), (6, 10), (16, 19), (14, 18), (16, 18), (4, 7), (8, 12), (2, 3)]],
    "hint" : 13
  }
]


def printarg(n, L):
    print("Lampki    : ", n)
    print("Liczba op.: ", len(L))
    print("Operacje  : ", limit(L))


def printhint(hint):
    print("Oczekiwany wynik:", hint)


def printsol(sol):
    print("Uzyskany wynik  :", sol)


def check(n, L, hint, sol):
    if sol == hint:
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False


def runtests(f):
    internal_runtests(printarg, printhint, printsol, check, TESTS, f)
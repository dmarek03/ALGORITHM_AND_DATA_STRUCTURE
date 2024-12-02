# Exercise_2_tests.py
# from signal import signal, alarm, SIGALRM
from testy import *


class Node:
    def __init__( self ):   # stwórz węzeł drzewa
        self.edges   = []     # lista węzłów do których są krawędzie
        self.weights = []     # lista wag krawędzi
        self.ids     = []     # lista identyfikatorów krawędzi
        self.sum_of_edges = 0

    def addEdge( self, x, w, id ): # dodaj krawędź z tego węzła do węzła x
        self.edges.append( x )       # o wadze w i identyfikatorze id
        self.weights.append( w )
        self.ids.append( id )

    def __str__( self ):
        s = "["
        for i in range(len(self.edges)):
            s += "[%d,%d,%s]" % (self.ids[i], self.weights[i], str(self.edges[i]))
            s += ","
        s+= "]"
        return s


def list2tree( L ):
    X = Node()
    for CH in L:
        Y = list2tree(CH[2])
        X.addEdge( Y, CH[1],CH[0] )

    return X



# format testów
# TESTS = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]

A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
A.addEdge(B, 6 , 1 )
A.addEdge(C, 10, 2 )
B.addEdge(D, 5 , 3 )
B.addEdge(E, 4 , 4 )



X = Node()
for i in range(10):
    Y = Node()
    X.addEdge( Y, i, i )



TESTS = [
    # 0
    {
        "arg" :[ A ],
        "hint":[ 1 ]
    },
    # 1
    {
        "arg" :[ X ],
        "hint":[ 9 ]
    },
    # 2   len(T) = 6
    {
        "arg": [list2tree( [[1,156,[]],[2,829,[]],[5,420,[[4,370,[[3,287,[]],]],]],[6,376,[]],] )],
        "hint": [5]
    },
    # 3   len(T) = 7
    {
        "arg": [list2tree( [[6,583,[[2,623,[[1,651,[]],]],[5,508,[[4,373,[[3,513,[]],]],]],]],[7,154,[]],] )],
        "hint": [5]
    },
    # 4   len(T) = 229
]
def printarg( T ):
    print("Drzewo        : ",limit(T))

def printhint( hint ):
    print("Możliwe wyniki:", limit(list2str(hint)) )

def printsol( sol ):
    print("Uzyskany wynik:", sol )


def check( T, hint, sol ):
    if sol in hint:
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False


def runtests( f ):
    internal_runtests( printarg, printhint, printsol, check, TESTS, f )
"""
Szablon rozwiązania: zad1.py
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie.
Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.
Podpowiedź. Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
(Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).
"""
from queue import PriorityQueue
from frog_testy import runtests
from math import inf
# jak istniej rozwiąznie to git
def zbigniew(array):
    steps = 0
    pq = PriorityQueue()
    energy = 0
    n = len(array)
    for i in range(n-1):
        print(f'{i=}')
        if array[i] > 0:
            pq.put(-array[i])
        if energy == 0:
            energy -= pq.get()
            steps += 1
        energy -= 1
    print(f'ala')
    return steps


def zbigniew2(A):
    count = 0
    for i in range(len(A)):
        count += A[i]
    DP = [[inf] * (count + 1) for _ in range(len(A))]
    DP[0][A[0]] = 0
    for i in range(len(A)):
        for j in range(count):
            if DP[i][j] != inf:
                k = i + 1
                while k < len(A) and j >= k - i:
                    index = i + j + A[k] - k
                    DP[k][index] = min(DP[k][index], DP[i][j] + 1)
                    k += 1
    min_jumps = min(DP[-1])
    return  min_jumps if min_jumps < inf else -1

runtests(zbigniew)

print(zbigniew([1, 0, 0]))
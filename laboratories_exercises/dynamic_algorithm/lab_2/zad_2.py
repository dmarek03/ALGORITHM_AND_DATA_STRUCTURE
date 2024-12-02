"""
Traktor jedzie od A do B i spala jedne litra paliwa na kilomter trasy. W baku mieści się L litów paliwa. Na trasię
zajdują się stacje.Podać algorytmy:


a) minimalzujemy liczbę tankowań.
b)minimalizujemy koszt przejazdu, może tankować dowolną ilośc paliwa
"""

def standard_tank(S, L, B):
    S = [0] + S + [B]
    n = len(S)

    for i in range(1, n):
        if S[i]-S[i-1] > L:
            return -1

    cnt = 0
    prev = -1


    for i in range(1, n):
        if L >= S[i] - S[prev]:
            continue

        else:
            cnt += 1
            prev = i-1
    return  cnt
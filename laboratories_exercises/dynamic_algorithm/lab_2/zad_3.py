"""
Mamy dany zbiór zadań T = {t1, t2, ..}.Każde zadanie ti dodatkowo posiada:termin wykonania d(ti) oraz zysk g(ti)
za jego wykonanie.Wykonanie każdego zadania trwa jednostkę czasu.Jeśli zadanie ti zostanie wykonane przed przekroczeniem
swojego terminu d(ti) to dostajemy za nie nagrodę (gi)
"""


def task(T):
    n = len(T)
    T.sort(key = lambda x: -x[1])

    max_deadline = 0

    for dl, pr in T:
        max_deadline = max(max_deadline, dl)


    S = [False for _ in range(max_deadline+1)]

    res = []

    for dl,pr in T:
        for i in range(dl, -1, -1):
            if not S[i]:
                S[i] = True
                res.append((dl, pr))

    return res
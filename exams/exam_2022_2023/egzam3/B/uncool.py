from egz3btesty import runtests

def has_common_point(range1, range2):
    return range1[0] <= range2[0] <= range1[1] or range2[0] <= range1[0] <= range2[1]


def contain(range1, range2):
    return range1[0] <= range2[0] and range1[1] >= range2[1] or range2[0] <= range1[0] and range2[1] >= range1[1]


def uncool(P):
    n = len(P)
    new_p = sorted([[p[0], p[1], i] for i, p in enumerate(P)], key=lambda x: x[0])
    for i in range(n-1, -1, -1):
        for j in range(n):
            if has_common_point(new_p[i], new_p[j]) and not contain(new_p[i], new_p[j]):
                return [new_p[i][2], new_p[j][2]]

#runtests(uncool2, all_tests=True)
from collections import deque

def point_to_key(point):
    return point[0],  0 if point[1][1] > point[0] else 1, point[1]


def uncool1(P):
    n = len(P)
    points = []
    for i in range(n):
        points.append([P[i][0], P[i], i])
        points.append([P[i][1], P[i], i])

    points.sort(key=point_to_key)
    print(f'{points=}')
    q = deque()
    for p in points:
        print(f'{p=}')
        if p[0] < p[1][1]:
            q.append(p)
            print(f'PUT: {p=}')
        else:
            elm = q.pop()
            print(f'GET:{elm=}')
            if elm[1] != p[1] and not contain(elm[1], p[1]):
                return (elm[-1], p[-1])


runtests(uncool1, all_tests=True)
# points jak klase

P1 = [[2, 100], [3,99], [1, 2]]
# # print(uncool(P)), 99], [1, 2]]
# #
P = [[1, 10], [3, 6], [4, 8], [12, 14]]


#print(uncool1(P1))
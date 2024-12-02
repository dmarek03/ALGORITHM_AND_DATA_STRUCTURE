"""
Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prostokątów, rury nie maja
objetosci (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego górnego
rogu i prawego dolnego rogu. Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda
rurami spłynęła do najniźszych pojemników). Proszę zaproponować algorytm Obliczający ile pojemników
zostało w pełni zalanych.
"""


def fill_containers(T, total_water):
    max_y = 0
    for i in range(len(T)):
        max_y = max(max_y, T[i][1])
    count_x = [0] * (max_y + 1)
    for i in range(len(T)):
        for j in range(T[i][3] + 1, T[i][1] + 1):
            count_x[j] += (T[i][2] - T[i][0])
    height = 0
    while total_water > 0:
        total_water -= count_x[height]
        height += 1
    if total_water != 0:
        height -= 1
    filled_containers = 0
    for i in range(len(T)):
        if T[i][1] <= height:
            filled_containers += 1
    return filled_containers

def max_heap(array: list[int], heap_size: int, root_idx: int):

    largest = root_idx
    left = 2 * root_idx + 1
    right = 2 * root_idx + 2
    #  checking if left child exits and if left child is greater than root
    if left < heap_size and array[left] > array[largest]:
        largest = left
    #  checking if right child exits and if left right is greater than root
    if right < heap_size and array[right] > array[largest]:
        largest = right
    # changing root if needed
    if largest != root_idx:
        array[largest], array[root_idx] = array[root_idx], array[largest]
        max_heap(array, heap_size, largest)  # heapify the root

    print(array)


def heapsort(array: list[int]):
    n = len(array)
    for i in range((n//2)-1, -1, -1):
        # building the max heap
        max_heap(array, n, i)

    for i in range(n-1, 0, - 1):
        # extract the last element
        array[i], array[0] = array[0], array[i]
        max_heap(array, i, 0)


def HowManyFilled(A,water):
    n=len(A)
    T=[0 for _ in range(2*n)]
    for i in range(n):
        cur=A[i]
        w=cur[1][0]-cur[0][0]
        T[2*i]=(cur[1][1],w)
        T[2*i+1]=(cur[0][1],-1*w)
    heapsort(T)
    cur_water=0
    counter=0
    active_width=T[0][1]
    l=T[0][0]
    for element in T[1:]:
        h=element[0]
        w_ch=element[1]
        cur_water+=active_width*(h-l)
        if cur_water>water:
            break
        if w_ch<0:
            counter+=1
        active_width+=w_ch
        l=h
    return counter



T = [(1, 8, 2, 5), (2, 4, 3, 1), (5, 6, 10, 4), (9, 7, 11, 0), (3, 8, 2, 3), (1, 3, 2, 2), (2, 4, 1, 3)]
#testy
A=[((1,18),(6,15)),((5,13),(9,7)),((10,15),(16,10)),((4,6),(12,3)),((14,8),(19,2))]
print(HowManyFilled(A, 60))
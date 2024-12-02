"""
HEAP SORT
"""


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


def heap_sort(array: list[int]):
    n = len(array)
    for i in range((n//2)-1, -1, -1):
        # building the max heap
        max_heap(array, n, i)

    for i in range(n-1, 0, - 1):
        # extract the last element
        array[i], array[0] = array[0], array[i]
        max_heap(array, i, 0)



tab = [4, 3, 1, 5, 2, 1, 0, 9]
heap_sort(tab)
print(tab)

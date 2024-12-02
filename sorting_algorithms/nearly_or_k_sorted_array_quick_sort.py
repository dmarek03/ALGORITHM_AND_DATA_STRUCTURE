"""
NEARLY OR K-SORTED ARRAY QUICK_SORT APPROACH
"""

def special_partition(array: list[int], left: int, right: int, k: int) -> int:

    mid = (right+left)//2
    i = max(left, mid-k)
    last = min(right, mid+k)
    #array[mid], array[last] = array[last], array[mid]
    for j in range(i, last):
        if array[j] < array[last]:
            array[j], array[i] = array[i], array[j]
            i += 1

        j += 1

    array[last], array[i] = array[i], array[last]

    return i


def quick_sort(array: list[int], left: int, right: int, k: int):

    if left < right:
        pos = special_partition(array, left, right, k)
        quick_sort(array, left, pos-1, k)
        quick_sort(array, pos+1, right, k)

#
# array = [3, 3, 2, 1, 6, 4, 4, 5, 9, 7, 8, 11, 12]
# quick_sort(array, 0, len(array)-1, 3)
# print(array)


"""
HEAP_SORT APPROACH
"""


def heapify(arr, heap_size, root_idx):
    smallest = root_idx
    left = 2 * root_idx + 1
    right = 2 * root_idx + 2

    if left < heap_size and arr[left] < arr[smallest]:
        smallest = left

    if right < heap_size and arr[right] < arr[smallest]:
        smallest = right

    if smallest != root_idx:
        arr[root_idx], arr[smallest] = arr[smallest], arr[root_idx]

        heapify(arr, heap_size, smallest)


def build_heap(arr):
    n = len(arr)

    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)


def sort_almost_sorted(arr, k):
    # building a heap of k-first elements
    heap = arr[:k+1]
    build_heap(heap)
    n = len(arr)
    result = [0] * n
    i = k + 1
    j = 0
    m = 0
    # seeing the elements of heap
    while j <= k:
        # adding the smallest element to final list
        result[m] = heap[0]
        m += 1
        # adding the another elements to heap if exists
        if i < n:
            heap[0] = arr[i]
            # incrementing the idx of next element in start list
            i += 1
            # calling heapify for a heap with new element
            heapify(heap, k + 1, 0)
        # all element of start list are in the heap
        else:
            # swapping the root element with the last a calling heapify for smallest heap
            heap[0] = heap[-1]
            j += 1
            heapify(heap, k - j + 1, 0)

    return result


# przykładowe użycie
arr = [3, 3, 2, 1, 6, 4, 4, 5, 9, 7, 8, 11, 12]
sorted_arr = sort_almost_sorted(arr, 3)
print(sorted_arr)
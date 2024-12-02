from kolutesty import runtests


def ice_cream_1( T ):
    max_sum = 0
    n = len(T)
    i = 0
    T.sort(reverse =True)
    while i < n and T[i] - i > 0:
        max_sum += T[i] - i
        i += 1
    return max_sum


def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left = 2*i + 1
    right = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr)
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_extract_max(arr):
    n = len(arr)
    if n == 0:
        return 0
    # Move max to end
    arr[0], arr[n-1] = arr[n-1], arr[0]
    max_value = arr.pop()  # Remove the last element
    # Heapify the root
    max_heapify(arr, len(arr), 0)
    return max_value

def ice_cream_2(T):
    # Convert array to max heap
    build_max_heap(T)

    max_volume = 0
    minute = 0

    while T:
        # Extract the maximum element (max heap root)
        current_max = heap_extract_max(T)

        if current_max > minute:
            # We can only eat the remaining ice cream before it melts
            max_volume += current_max - minute
            minute += 1  # Move to the next minute

    return max_volume



def find_avg(A, p, r):
    # Znalezienie indeksu elementu najbliższego średniej wartości w przedziale [p, r]
    suma = sum(A[p:r+1])
    avg = suma / (r - p + 1)
    best_index = p
    best_diff = abs(A[p] - avg)
    for i in range(p+1, r+1):
        current_diff = abs(A[i] - avg)
        if current_diff < best_diff:
            best_diff = current_diff
            best_index = i
    return best_index

def partition(A, p, r):
    # Podział tablicy na dwie części w oparciu o element piwot
    i = find_avg(A, p, r)
    A[i], A[r] = A[r], A[i]  # Przenieś piwot na koniec
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]  # Przenieś piwot na właściwe miejsce
    return i + 1

def select(A, k, p, r):
    # Quickselect do znalezienia k-tego najmniejszego elementu w przedziale [p, r]
    while p <= r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            p = q + 1
        else:
            r = q - 1
    return -1

def find_last(A):
    # Znalezienie punktu granicznego
    n = len(A)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        threshold = n - mid
        val = select(A, mid, 0, n - 1)
        if val >= threshold:
            right = mid - 1
        else:
            left = mid + 1
    return left

def ice_cream(T):
    last = find_last(T)
    n = len(T)
    collected = 0
    for i in range(last, n):
        collected += T[i] - (i - last)
    return collected




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ice_cream, all_tests=True)




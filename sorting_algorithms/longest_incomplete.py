"""
Zadanie 3.
Szablon rozwiązania: zad3.py
Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
zawsze prawidłowa.)

"""


def longest_incomplete(array, k):
    if k < 2:
        return 0
    # Store unique values in an array (they must be sorted)
    unique = []
    for val in array:
        idx = binary_search(unique, val)
        if idx < 0:
            insert_element(unique, val)

    # If we have less unique values than a value of k, the whole
    # array fulfills conditions
    if len(unique) < k:
        return len(array)

    # Create counters array
    counters = [0] * len(unique)
    # Find the first subsequence of k-1 unique values
    # (as we look for the longest subsequence, we will always
    # take k-1 values)
    remaining = k - 1
    i = 0
    while i < len(array) and remaining > 0:
        idx = binary_search(unique, array[i])
        counters[idx] += 1
        if counters[idx] == 1:
            if remaining == 0:
                break
            remaining -= 1
        i += 1

    # Look for a longest subsequence of a number of unique values
    # not greater than k (this will usually be a subsequence
    # of k-1 unique values)
    max_length = i
    j = 0
    while i < len(array):
        idx_i = binary_search(unique, array[i])
        # If we found a new value, we have to advance a j pointer till
        # we drop one of values
        counters[idx_i] += 1
        if counters[idx_i] == 1:
            while j <= i:
                idx_j = binary_search(unique, array[j])
                counters[idx_j] -= 1
                j += 1
                if counters[idx_j] == 0:
                    break
        else:
            curr_length = i - j + 1
            if curr_length > max_length:
                max_length = curr_length
        i += 1

    return max_length


def binary_search(arr, el):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] == el:
            return mid_idx
        if el > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1
    return -1

    #return left_idx if left_idx < len(arr) and arr[left_idx] == el else -1


def insert_element(arr, val):
    arr.append(val)
    if len(arr) > 1:
        # Move all elements that are greater than a value inserted to the right
        idx = len(arr) - 1
        while idx > 0 and arr[idx - 1] > val:
            arr[idx] = arr[idx - 1]
            idx -= 1
        # Place our value on the final position
        arr[idx] = val

def longest_incomplete1(A, k):
    if not A or k == 0:
        return 0

    longest_length = 0
    current_length = 0
    count = {}

    left = 0

    for right in range(len(A)):
        num = A[right]

        if num not in count:
            count[num] = 0

        if count[num] == 0:
            k -= 1

        count[num] += 1

        while k < 0:
            left_num = A[left]
            count[left_num] -= 1

            if count[left_num] == 0:
                k += 1

            left += 1

        current_length = right - left + 1
        longest_length = max(longest_length, current_length)

    return longest_length




A = [1, 100, 5, 1, 5, 1, 1, 5, 1, 100, 1, 5, 1, 5, 1, 1, 1]
k = 3

print(longest_incomplete1(A, k))
print(longest_incomplete1(A, 4))  # Takes the whole array
print(longest_incomplete1(A, 2))
print(longest_incomplete1(A, 1))  # Returns 0 as the only one possibility for a value lower than 1 is 0
print(longest_incomplete1(A, 2131321))
print(longest_incomplete1(A, -4821904))
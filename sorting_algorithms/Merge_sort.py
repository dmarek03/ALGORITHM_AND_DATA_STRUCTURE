"""
MERGE SORT
"""


def merge_sort(tab: list[int]):
    if len(tab) > 1:
        left_array = tab[:len(tab)//2]
        right_array = tab[len(tab)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0
        j = 0
        k = 0

        while i < len(left_array) and j < len(right_array):

            if left_array[i] <= right_array[j]:
                tab[k] = left_array[i]
                i += 1

            else:
                tab[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            tab[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            tab[k] = right_array[j]
            k += 1
            j += 1


tab = [1, 2,4 ,6 ,2 ,4 , 2, 6, 2, 56, 5]
merge_sort(tab)
print(tab)

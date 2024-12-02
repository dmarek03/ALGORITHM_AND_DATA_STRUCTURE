"""
Counting sort
"""


def counting_sort(array: list[int]):
    n = len(array)
    min_val = min(array)
    max_val = max(array)
    count_array = [0] * (max_val - min_val + 1)
    sorted_array = [0] * n

    for i in range(n):
        count_array[array[i] - min_val] += 1

    for j in range(1, len(count_array)):
        count_array[j] += count_array[j-1]

    print(count_array)

    for k in range(n-1, -1, -1):
        sorted_array[count_array[array[k] - min_val] - 1] = array[k]
        count_array[array[k] - min_val] -= 1

    for i in range(n):
        array[i] = sorted_array[i]


tab = [5, 4,1, 2,3,9,5 , 5, 5,5, 3, 2, 1]

counting_sort(tab)
print(tab)



# def counting_sort(array, pos: int):
#     n = len(array)
#     count_array = [0] * 27
#     sorted_array = [0] * n
#
#     for i in range(n):
#         count_array[array[i][pos]] += 1
#
#     for i in range(1, 27):
#         count_array[i] += count_array[i-1]
#
#     for i in range(n-1, -1, -1):
#         sorted_array[count_array[array[i][pos]]-1] = array[i]
#         count_array[array[i][pos]] -= 1
#
#     for i in range(n):
#         array[i] = sorted_array[i]

# ''''''ala
# '''''alab
# lllllaads

# max_len = max([len(t) for t in new_t])
    # print("Tablica[ " + str(n) + "], max len: " + str(max_len))
    # new_t2 = ["`" * (max_len - len(t)) + t for t in new_t]
    # new_t2 = [[ord(x) - 96 for x in t] for t in new_t2]
    #
    # for i in range(max_len-1, -1, -1):
    #     # print(i)
    #     counting_sort(new_t2, i)

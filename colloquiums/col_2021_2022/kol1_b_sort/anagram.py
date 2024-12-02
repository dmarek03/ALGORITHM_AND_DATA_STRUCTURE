# Początkowo zamieniam wszystkie wyraz na tablice , które przechowują informację z  ilu jakich liter składa się wyraz.
# Następnie radix sortem sortuje tablicę przechowującą histogramy wyrazów, tak aby wyraz o takich samych literach
# znajdowały się na koljenych indeksach i następnie przechodząc przez tą tablicę , znajduję najdłuższy spójny podciąg
# identycznych wierszy.

from kol1btesty import runtests
def counting_sort(array, pos: int, max_val: int):
    n = len(array)
    count_array = [0] * (max_val + 1)
    sorted_array = [0]*n

    for i in range(n):
        count_array[array[i][pos]] += 1

    for j in range(1, len(count_array)):
        count_array[j] += count_array[j-1]

    for k in range(n-1, -1, -1):
        sorted_array[count_array[array[k][pos]] - 1] = array[k]
        count_array[array[k][pos]] -= 1

    for i in range(n):
        array[i] = sorted_array[i]


def into_histogram(text: str) -> list[int]:
    histo = [0] * 26
    for i in text:
        pos = ord(i) - 97
        histo[pos] += 1

    return histo


def get_max(tab: list[list[int]]) -> int:
    max_val = 0

    for i in range(len(tab)):
        for j in range(26):
            if tab[i][j] > max_val:
                max_val = tab[i][j]
    return max_val



def anagram(T):

    new_t = [into_histogram(n) for n in T]
    #print(*new_t, sep='\n')
    max_val = get_max(new_t)
    print(max_val)
    # print(f'{max_val=}')
    # print('----------------')
    # print(f'{len(T)=}')
    for i in range(26):
        counting_sort(new_t, i, max_val)
        # print(*new_t, sep='\n')
        # print('---------------------------------------')
    n = len(new_t)

    max_ans = 1
    best_ans = 1
    for i in range(n-1):
        if new_t[i] == new_t[i + 1]:
            max_ans += 1
            if max_ans > best_ans:
                best_ans = max_ans
        else:
            max_ans = 1
    return best_ans


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(anagram, all_tests=True)
#
tab = ['aaaa', 'bbbb', 'cc', 'dddd', 'hubert']
print(anagram(tab))


# DOMINIK MAREK
# Celem zadania jest znalezienie najśilniejszego napisu. Zatem zaczynam od przejścia po tablicy i jeżeli pierwsza połowa
# napisu jest lesksykograficznie "większa" od drugiej to dany napis odwracam. Złożoność tej opracji wynosi O(N), gdzie
# N to łączna długość napisów w tablicy. Następnie sortuję już przygotowaną tablicy algorytmem merge_sort w czasie
# O(logn) i przechodzę po posortowanej tablicy szukająć najdłuższego spoójnego podciągu takich samych wyrazów, na końcu
# zwracam siłę najsliniejszego napisu. Końcowa złożoność jest równa O(N + nlogn)
from zad3testy import runtests


def normalize_strings(array: list[str]) -> list[str]:
    return [x[::-1] if x[:len(x)//2] > x[(len(x)//2):] else x for x in array]


def merge_sort(tab: list[str]):
    n = len(tab)
    if n > 1:
        left_array = tab[:n//2]
        right_array = tab[n//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        n1 = len(left_array)
        n2 = len(right_array)

        i = 0
        j = 0
        k = 0

        while i < n1 and j < n2:

            if left_array[i] < right_array[j]:
                tab[k] = left_array[i]
                i += 1

            else:
                tab[k] = right_array[j]
                j += 1

            k += 1

        while i < n1:
            tab[k] = left_array[i]
            i += 1
            k += 1

        while j < n2:
            tab[k] = right_array[j]
            k += 1
            j += 1


def strong_string(T):

    n = len(T)
    new_t = normalize_strings(T)
    merge_sort(new_t)
    cnt = 1
    best_cnt = 1

    for i in range(n-1):

        if new_t[i] == new_t[i+1]:
            cnt += 1
            if cnt > best_cnt:
                best_cnt = cnt
        else:
            if cnt < n - i:
                cnt = 1
            else:
                break

    return best_cnt


#  zmien all_tests na True zeby uruchomic wszystkie testy
runtests(strong_string, all_tests=True)
#
# T = ["pies","otk","mysz", "kot", "kogut", "tok", "seip", "kot", "ipes", "kot", "kto", "tko","pies", "pies", "seip","ipes", "epsi"]
# t = [1,5,0,23,3,1]
# new_t = normalize_strings(T)
# merge_sort(new_t)
# print(new_t)
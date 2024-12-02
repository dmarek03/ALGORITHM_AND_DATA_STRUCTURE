from kol1testy import runtests
# Dominik Marek
# W celu rozwiązania zadań dla każdego elementu z tablicy iteruję przez elementy znadujące się przed nim w tablicy,
# a następnie liczam ile jest elementów mniejszych od naszego elementu (zmienna current_rank). Po przejściu wewnętrzenj pętli
# sprawdzam czy obliczona obecna ranga jest większą od posiadanje dotychczas maksymalnej rangi.
# Jeśli tak to aktualizuję zmienną max_rank.Po obliczeniu rangi dla wszystkich elementów z tablicy zwracam zmienna max_rank,
# która jest równa wartości największej rangi dla elementów z tablicy wejściowej
# Złożoność obliczeniowa O(n^2) -> dla każdego elementu z n-elementowej tablicy spradzam i elementów , gdzie i jest z zakresie od 0..n
# Złożoność pamięciowa O(1)

def merge_sort(T, ans):
    if len(T) <= 1:
        return T
    left_tab = T[:len(T) // 2]
    right_tab = T[len(T) // 2:]
    merge_sort(left_tab, ans)
    merge_sort(right_tab, ans)
    i, j, idx = 0, 0, 0

    while i < len(left_tab) and j < len(right_tab):
        if left_tab[i][0] < right_tab[j][0]:
            T[idx] = left_tab[i]
            i += 1
        else:
            T[idx] = right_tab[j]
            ans[right_tab[j][1]] += i
            j += 1
        idx += 1

    while i < len(left_tab):
        T[idx] = left_tab[i]
        i += 1
        idx += 1

    while j < len(right_tab):
        T[idx] = right_tab[j]
        ans[right_tab[j][1]] += i
        j += 1
        idx += 1




def maxrank(T):
    ans = [0 for _ in range(len(T))]
    tmp = [(t, i) for i, t in enumerate(T)]
    if len(T) < 100:
        print(f'{tmp=}')
    merge_sort(tmp, ans)
    if len(T) < 100:
        print(f'{tmp=}')
        print(f'{ans=}')
    return max(ans)
runtests( maxrank, all_tests = True)

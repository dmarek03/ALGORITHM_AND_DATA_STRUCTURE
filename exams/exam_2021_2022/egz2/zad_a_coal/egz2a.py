from egz2atesty import runtests

# Tworzę tablicę długosći n reprezentująca kontenery. Dla każdego transportu szukam pierwszego kontenru do którego
# zmiesći i zamapiętuję indeks tego kontenera.Na końcu zwracam indeks kontenera do którego poszedł ostatni transport.
def coal(A, T):
    n = len(A)
    containers = [0]*n
    recently_updated = -1
    for a in A:
        for i in range(n):
            if a + containers[i] <= T:
                containers[i] += a
                recently_updated = i
                break

    return recently_updated


#Inicjalizujemy drzewo przedziałowe o rozmiarze 2**p, gdzie p spełnia zależność 2**(p-1) > n, w którym każda wartosc
# wynosi T, co odpowiada pojemnosći magazynu.Ustawiamy self.M jako 2 ** (p - 1), co jest indeksem pierwszego liścia w
# drzewie segmentowym.
# Metoda upade aktualizuje ilość wolnych miejsc w magazynie po zajęciu w nim pewnej ilości miejsc.Działa ona w
# astępujący sposób zmniejsza ilość wolnych miejsc w tym magazynie o wartość val, a następnie aktualizuje wartości
# węzłów rodziców, aby odzwierciedlały one aktualny stan drzewa segmentowego.
# Metoda query zwraca indeks pierwszego magazynu , który ma conajmniej val wolnych miejsc.
# W funkcji coal najpierw tworzymy dzewo segmentowe, a następnie iterując przez kolejne transporty za pomocą metody query
# znajdujemy indeks pierwszego wolnego magazynu dla danego transportu, następnie aktulizujemy stan tego magazynu i pod
# zmienną przechowującą indeks ostatnio załadowanego magazynu podstawianym indeks obecnie przetwarzanego magazynu.
# Finalanie zwracamy zmienną last_idx co jest roziwązaniem naszego zadania
class SegmentTree:
    def __init__(self, n, T):
        p = 1
        while  2 ** (p - 1) < n:
            p += 1
        self.tree = [T] * (2 ** p)
        self.M = 2 ** (p - 1)

    # odejmuje z magazynu idx val miejsca
    def update(self, idx, val):
        idx += self.M
        self.tree[idx] -= val
        idx //= 2
        while idx >= 1:
            self.tree[idx] = max(self.tree[idx * 2], self.tree[idx * 2 + 1])
            idx //= 2

    # zwraca indeks pierwszego magazynu gdzie można zająć val miejsca
    def query(self, val):
        cur = 1
        while cur < self.M:
            cur *= 2
            if self.tree[cur] < val:
                cur += 1
        return cur - self.M


def coal1(A, T):
    ST = SegmentTree(len(A), T)
    last_idx = -1
    for x in A:
        idx = ST.query(x)
        if idx == -1:
            break  # Brak dostępnego magazynu
        ST.update(idx, x)
        last_idx = idx
    return last_idx




runtests( coal1, all_tests = True)

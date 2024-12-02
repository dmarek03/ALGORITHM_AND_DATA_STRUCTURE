from egz3btesty import runtests


def can_go_from(level: int, room: int, no_rooms: int, list_of_chambers):
    return 0 <= level < no_rooms and room < no_rooms and list_of_chambers[level][room] != '#'


def print_matrix(tab, L):
    for i, row in enumerate(tab):
        for j, el in enumerate(row):
            if not el:
                if L[i][j] == '#':
                    print("  =", end="\t")
                else:
                    print("  .", end="\t")
            else:
                print("%3d" % el, end="\t")
        print()

    print("------------")


def maze( L ):
    n = len(L)
    if L[n-1][n-1] == '#' or (L[0][1] == '#' and L[1][0] == '#') or (L[n-1][n-2] == '#' and L[n-2][n-1] == '#'):
        return -1

    new_list = [[0]*n for _ in range(n)]
    if not L[0][1] == '#':
        new_list[0][1] = 1

    distance = 0
    for row in range(n):
        if L[row][0] == '#':
            break
        new_list[row][0] = distance
        distance += 1

    for col in range(1, n):
        for row in range(n):
            if L[row][col] == '#':
                continue

            if can_go_from(row - 1, col, n, L) and new_list[row-1][col] > 0:
                new_list[row][col] = new_list[row-1][col] + 1

            if can_go_from(row, col - 1, n, L) and new_list[row][col-1] > 0:
                cnt = new_list[row][col-1] + 1
                for k in range(row, -1, -1):
                    if L[k][col] == '#':
                        break
                    if new_list[k][col] <= cnt:
                        new_list[k][col] = cnt
                    cnt += 1

    return new_list[n-1][n-1] if new_list[n-1][n-1] else -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )

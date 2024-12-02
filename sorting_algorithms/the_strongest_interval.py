

def the_strongest_interval(tab):
    tab.sort(key=lambda x: x[0])
    print(f'{tab=}')
    n = len(tab)
    new_t = sorted([[t[0], t[1], i] for i, t in enumerate(tab)], key=lambda x: x[1])

    for i in range(n):
        new_t[i] = [new_t[i][0], new_t[i][1], new_t[i][2], i]

    max_interval = 0
    max_idx = 0

    for i in range(n):

        if new_t[i][3]-new_t[i][2] > max_interval:
            max_interval = new_t[i][3]-new_t[i][2]
            max_idx = i
    return (new_t[max_idx][0], new_t[max_idx][1]), max_interval



T = [(4, 8), (5, 9), (1, 2), (1, 3), (2, 8), (3, 7), (4, 6), (8, 9), (6, 10), (6, 11), (9, 14), (11, 16), (3, 4)]
max_span, max_interval = the_strongest_interval(T)
print(f'{max_span=}')
print(f'{max_interval=}')


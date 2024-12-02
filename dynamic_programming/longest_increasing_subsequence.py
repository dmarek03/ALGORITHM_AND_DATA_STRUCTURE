
def lis(tab:list[int]) -> int:
    n = len(tab)
    dp = [1]*n

    for i in range(1,n):
        for j in range(i):
            if tab[i] >= tab[j] and dp[j] + 1 > dp[i]:

                dp[i] = dp[j] + 1
    print(f'{dp=}')

    return max(dp)


tab = [1, 1, 1, 1, 2, 2, 3]
lis_length= lis(tab)
print(f'{lis_length=}')
print("------------------")


def binary_search(arr, val):
    left_idx = 0
    right_idx = len(arr) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if val > arr[mid_idx]:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx - 1

    return left_idx  # It will never exceed the left side of an array


def lis_2(arr) -> list[int]:
    n = len(arr)
    if n < 2:
        return arr
    last = []
    ind = []
    parents = [-1] * n

    for i in range(n):
        j = binary_search(last, arr[i])
        if j >= len(last):
            if j > 0:
                parents[i] = ind[j - 1]
            ind.append(i)
            last.append(arr[i])
        else:
            ind[j] = i
            last[j] = arr[i]
            if j > 0:
                parents[i] = ind[j - 1]

    # Get result
    result = [-1] * len(last)
    j = ind[-1]
    for i in range(len(last) - 1, -1, -1):
        result[i] = arr[j]
        j = parents[j]

    return result


def lis3(tab) -> int:
    n = len(tab)
    s = []
    s.append(tab[0])

    for i in range(1, n):
        if tab[i] >= s[len(s)-1]:
            s.append(tab[i])
        else:
            s[binary_search(s, tab[i])] = tab[i]
    return len(s)

#
tab = [1, 1, 1 ,2]
res = lis(tab)
print(f'{res=}')

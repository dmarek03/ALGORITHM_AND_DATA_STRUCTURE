# Korzystjac z problemu plecakowego sprawdzamy czy istnieje w naszej tablicy podciąg o danej sumie.
# Złożoność O(n*value)
def is_sub_sum(tab, value):
    if value < 0:
        return False, []
    if value < 2:
        for t in tab:
            if t == value:
                return True, [t]
        return False, []
    processed_tab = [t for t in tab if 0 < t <= value]
    n = len(processed_tab)
    dp = [[0]*(value+1) for _ in range(n)]

    for i in range(processed_tab[0], value+1):
        dp[0][i] = processed_tab[0]

    for i in range(1, n):
        for w in range(1, value+1):
            dp[i][w] = dp[i-1][w]
            if w >= processed_tab[i]:
                dp[i][w] = max(dp[i][w], dp[i-1][w-processed_tab[i]] + processed_tab[i])

            if dp[i][w] == value:
                return True, dp
    return False, dp


def get_sub(dp, processed_tab, value):
    if not dp or dp[0][-1] == 0:
        return []

    contents = []
    w = len(dp[0]) - 1

    i = len(dp) - 1
    while dp[i][w] == 0:
        i -= 1
    if dp[i][w] != value:
        return []

    for i in range(i, 0, -1):
        # If we have taken an item from the 'i'th row, a sum stored
        # in this row will be different from a sum in a row above
        if dp[i][w] != dp[i - 1][w]:
            # We take this item to the subsequence and reduce the remaining
            # sum, so we have to decrease a value of a column pointer 'w'
            contents.append(processed_tab[i])  # Change to 'i' if you want indices of elements
            w -= processed_tab[i]
    # As we will never check the first row in a loop above, we have
    # to assess whether the item from the first row was taken separately
    # We decide to take the first element only there is still some value
    # remaining
    if w > 0:
        contents.append(processed_tab[0])  # Change to '0' if you want indices of elements

    contents.reverse()
    return contents
A1= [1, 3, 5, 2, 7, 13, 8]
A2 = [1, 1, 1, 3, 5, 2, 1, 1, 1, 7, 1, 1, 1, 1, 13, 8]
T = 10

res, F = is_sub_sum(A1, T)
print(*F, sep='\n')
print(res)
print(get_sub(F, A1, T))
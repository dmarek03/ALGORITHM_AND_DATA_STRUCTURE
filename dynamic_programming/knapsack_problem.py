from random import randint


def get_sum(tab1, tab2):
    elem_sum = 0
    for i in tab1:
        elem_sum += tab2[i]
    return elem_sum


def get_weights_prices(size: int, min_range: int, max_range: int):
    weights = [randint(min_range, max_range) for _ in range(size)]
    prices = [randint(min_range, max_range)for _ in range(size)]
    return weights, prices


def filter_items(weights, prices, max_weight):
    w_filtered = []
    p_filtered = []
    for i in range(len(weights)):
        if weights[i] <= max_weight and prices[i] > 0:
            w_filtered.append(weights[i])
            p_filtered.append(prices[i])
    return w_filtered, p_filtered


def knapsack(weights, prices, max_weight):

    if min(weights) > max_weight:
        return 0
    n = len(weights)

    print(f'{weights=}')
    print(f'{prices=}')

    dp = [[0] * (max_weight + 1) for _ in range(n)]

    for i in range(weights[0], max_weight + 1):
        dp[0][i] = prices[0]

    for i in range(1, n):
        for w in range(1, max_weight + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= weights[i]:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i]] + prices[i])

    return dp[n - 1][max_weight], dp


def get_knapsack(dp, weights):
    contents = []
    w = len(dp[0]) - 1
    for i in range(len(dp) - 1, 0, -1):
        # If we have taken an item from the 'i'th row, a profit stored
        # in this row will be different than a profit in a row above
        if dp[i][w] != dp[i - 1][w]:
            # We take this item to the knapsack and reduce its remaining
            # capacity so we have to decrease a value of a column pointer 'w'
            contents.append(i)
            w -= weights[i]
    # As we will never check the first row in a loop above, we have
    # to asses whether the item from the first row was taken separately
    # We decide to take the first element only if the remaining weight
    # which can be used is no lower than a weight of this element
    if w >= weights[0]:
        contents.append(0)

    # Reverse the result array as we get indices in a reversed order
    contents.reverse()
    return contents




# W = [4, 1, 2, 4, 3, 5, 10, 3]
# P = [7, 3, 2, 10, 4, 1, 7, 2]
# MaxW = 10
#
# W = [5, 3, 4, 2]
# P = [60, 50, 70, 30]
# MaxW = 5
W, P = get_weights_prices(20, 10, 300)
# print(f'{W=}')
# print(f'{P=}')

MaxW= 200
profit, F = knapsack(W, P, MaxW)
print(*F, sep='\n')
print('Profit:', profit)
contents = get_knapsack(F, W)
print('Contents:', contents)

print(get_sum(contents, P))
from egzP3atesty import runtests
from math import inf


# Complexity -> O(nmp)
# Przygotowujemy dane dla każdych wyborów  wydzielając koszty,ilosć głosów do uzyskania i maksymalny budżet.
# Następnie wykonujemy knapsack algorytm i znajdujemy największą ilość głosów jakie można uzyskać w danych wyborach.
# Finalny wynik to suma głosów z wszytskich wyborów.

class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


def knapsack(dp, budget, prices, costs, i):
    if budget < 0:
        return -inf
    if i >= len(prices):
        return 0

    if dp[i][budget]:
        return dp[i][budget]
    d1 = knapsack(dp, budget - costs[i], prices, costs, i + 1) + prices[i]
    d2 = knapsack(dp, budget, prices, costs, i + 1)

    dp[i][budget] = max(d1, d2)
    return dp[i][budget]


def knapsack2(costs, votes, budget):
    if min(costs) > budget:
        return 0
    n = len(costs)

    dp = [[0] * (budget + 1) for _ in range(n)]

    for i in range(costs[0], budget + 1):
        dp[0][i] = votes[0]

    for i in range(1, n):
        for w in range(1, budget + 1):
            dp[i][w] = dp[i - 1][w]
            if w >= costs[i]:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - costs[i]] + votes[i])
    # print(*dp, sep='\n')
    return dp[n - 1][budget]


def wybory(tab):
    max_sum = 0
    for elem in tab:
        budget = elem.fundusze
        votes = []
        costs = []
        pp = elem

        while pp:
            votes.append(pp.wyborcy)
            costs.append(pp.koszt)
            pp = pp.next
        # dp = [[None for _ in range(budget + 1)] for _ in range(len(votes))]
        # max_sum += knapsack(dp, budget, votes, costs, 0)
        max_sum += knapsack2(costs, votes, budget)

    return max_sum


runtests(wybory, all_tests=True)

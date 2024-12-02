from math import inf


# Use a modified Binary Search algorithm to find the next station
def get_station_idx(distances, left, right, max_range):
    while left <= right:
        mid = (left + right) // 2
        if max_range < distances[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return right


def tank(capacity, distances, prices, length):
    if capacity >= length:
        return 0
    if distances[0] > capacity:
        return -1

    last_station_idx = get_station_idx(distances, 0, len(distances) - 1, length)
    n = last_station_idx + 1

    F = [inf] * n
    # Store a cost required to fill up a tank on the first station
    F[0] = prices[0] * distances[0]

    for i in range(1, n):
        j = i - 1
        dist = distances[i] - distances[j]
        while j >= 0 and dist <= capacity:
            F[i] = min(F[i], F[j] + dist * prices[i])
            j -= 1
        if distances[i] <= capacity:
            F[i] = min(F[i], distances[i] * prices[i])

    # Get the last station (the one of the lowest total cost)
    min_idx = last_station_idx
    i = min_idx - 1
    while i >= 0 and length - distances[i] <= capacity:
        if F[i] < F[min_idx]:
            min_idx = i
        i -= 1

    #     print(F)
    return F[min_idx], F, min_idx


def get_solution(S, P, F, i):
    res = []

    for j in range(i - 1, -1, -1):
        if F[j] < F[i]:
            res.append((i, S[i] - S[j], F[i] - F[j], P[i]))
            i = j

    res.append((i, S[i], F[i], P[i]))

    return res[::-1]


# Czołg jedzie z punktu A do punktu B. Spalanie czołgu to dokładnie jeden litr paliwa na jeden kilometr
# trasy. W baku mieści się dokładnie L litrów paliwa. Trasa z A do B to prosta, na której znajdują się
# stacje benzynowe (na pozycjach będących liczbami naturalnymi; A jest na pozycji 0). Proszę podać
# algorytmy dla następujących przypadków:
#     1) Wyznaczamy stacje tak, żeby koszt przejazdu był minimalny (w tym wypadku każda stacja ma
# dodatkowo cenę za litr paliwa). Na każdej stacji możemy tankować dowolną ilość paliwa.
#     2) j.w., ale jeśli na stacji tankujemy, to musimy zatankować do pełna.
from math import inf


# 1)


def tank_fueling(distance, fuel_tank, stops, prices):
    if fuel_tank < stops[0]:
        return False
    T = [-1] * (distance + 1)
    for i in range(len(T)):
        for j in range(len(stops)):
            if stops[j] > i:
                break
            if stops[j] == i:
                T[i] = prices[j]
    total_cost = 0
    for i in range(1, distance + 1 - fuel_tank):
        min_cost = inf
        for j in range(i, i + fuel_tank):
            if T[j] != -1:
                min_cost = min(min_cost, T[j])
        total_cost += min_cost
    return total_cost


# 2)


def tank_fueling2(distance, fuel_tank, stops, prices):
    F = [0] * len(stops)
    F[0] = prices[0] * stops[0]
    for i in range(1, len(stops)):
        j = i - 1
        minimum = F[j] + (stops[i] - stops[j]) * prices[i]
        while j >= 0 and fuel_tank >= stops[i] - stops[j]:
            minimum = min(minimum, F[j] + (stops[i] - stops[j]) * prices[i])
            j -= 1
        if j == -1 and fuel_tank >= stops[i]:
            minimum = min(minimum, prices[i] * stops[i])
        F[i] = minimum
    result = F[len(stops) - 1]
    for i in range(len(stops)):
        if distance - stops[i] <= fuel_tank:
            result = min(F[i], result)
    return result


stops = [1, 9, 15, 16, 17, 27, 28]
prices = [1, 100, 10, 15, 1, 30, 30]
distance = 30
fuel = 14
print(tank_fueling(distance, fuel, stops, prices))
print(tank_fueling2(distance, fuel, stops, prices))
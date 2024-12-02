"""
Mamy tablicę A zawierającą liczby naturalne i chcemy sprawdzić czy da się wybrać liczby, które zsumują się do wartośći T.

"""

def is_sum(tab, number):
    sum_of_element = sum(tab)

    dp = [False]*(sum_of_element+1)
    dp[0] = True

    for a in tab:
        for i in range(sum_of_element, -1, -1):
            if dp[i]:
                dp[i+a] = True
    return dp[number]


t = [2, 3, 8, 16, 35]
number = 5
print(f'{is_sum(t, number)}')

"""
f(s,i) = f(s, i-1) or f(s- A[i], i-1)
if s < 0: return False
f(0,i) = True
f(s, 0) = False
"""


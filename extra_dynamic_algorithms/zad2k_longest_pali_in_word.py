from zad2ktesty import runtests


def f(a, b, s):
    if a == b:
        return True
    if a + 1 == b:
        return s[a] == s[b]
    if s[a] != s[b]:
        return False
    if s[a] == s[b]:
        return f(a+1, b-1, s)


# Complexity - > 0(n^2)
def palindrom( S :str):
    n = len(S)
    longest_pali = ''
    curr_pali = ''
    for i in range(n):
        for j in range(i+1, n):
            if f(i, j, S):
                curr_pali = S[i:j+1]
        if len(curr_pali) > len(longest_pali):
            longest_pali = curr_pali

    return longest_pali


runtests ( palindrom )
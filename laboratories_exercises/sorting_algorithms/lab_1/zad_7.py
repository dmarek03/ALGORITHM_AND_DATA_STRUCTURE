"""
W tablicy szukamy takiego indeksu, że A[i] != ai, gdzie A= [a0, a1, a2, ...] -posortowaną, brakuje jakiegoś elementu,
do k mamy elementy, której nie ma
"""
# binary search
# if A[mid] == mid: search(right) else search(left)
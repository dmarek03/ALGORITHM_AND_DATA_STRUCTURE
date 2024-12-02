# Znalezienie największego zbioru przedziałów, które na siebie nie zachodzą.

def task_management(span):
    span.sort(key=lambda x: x[1])
    res = [span[0]]
    curr_span = span[0]

    for s in span:
        if s[0] > curr_span[1]:
            res.append(s)
            curr_span = s
    return res


A = [[5.22, 11.55], [8.45, 11.05], [5.35, 6.20], [7.00, 8.15]]
D = [[3.15, 8.04], [2.05, 5.42], [9.05, 11.33], [0.25, 2.24], [10.25, 16.42], [12.05, 17.55], [1.12, 3.45]]

print(task_management(A))
print(task_management(D))

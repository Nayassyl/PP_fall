def LessThanNumber(a, n):
    for elem in a:
        if elem < n:
            print(elem, end = " ")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
LessThanNumber(a, 5)
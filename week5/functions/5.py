def first_diff(a, b):
    i = 0
    if a == b: return -1
    while a[i] == b[i]: i += 1
    return i

a, b = [i for i in input().split()]
print(first_diff(a, b))

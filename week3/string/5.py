def changee(st1, st2):
    x = b[0] + a[1:]
    y = a[0] + b[1:]
    return x + ' ' + y
a = input()
b = input()
print(changee(a, b))
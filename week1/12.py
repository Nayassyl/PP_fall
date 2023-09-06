def sol(a, b, c, d, e, f):
    y = (f - (d * c)/a) / ( e - (d * b)/a)
    x = (c - (b * y))/a
    print("{:.{}f}".format(x, 3), "{:.{}f}".format(y, 3))

a, b, c, d, e, f = [float(i) for i in input().split()]
sol(a, b, c, d, e, f)

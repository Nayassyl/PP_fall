def w12(n):
    if abs(n - 1000) <= 100:
        print("within 100 of 1000")
    elif abs(n - 2000) <= 100:
        print("within 100 of 2000")
    else:
        print("not within 100 of 1000 or 2000")


#testing
a = 1025
b = 1935
c = 27
w12(a)
w12(b)
w12(c)
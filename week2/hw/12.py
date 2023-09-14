a = float(input("Input first number: "))
b = float(input("Input second number: "))
c = float(input("Input third number: "))
if a > b:
    if a < c:
        m = a
    elif b > c:
        m = b
    else:
        m = c
else:
    if a > c:
        m = a
    elif b < c:
        m = b
    else:
        m = c

print("The median is", m)

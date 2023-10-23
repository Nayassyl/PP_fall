import random
def ran(n) :
    a = 10 ** (n - 1)
    b = 10 ** (n)
    print( random.randint (a, b))

ran(int(input()))
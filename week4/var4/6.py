import math
def pyth(n):
    while (n != 0):
        l = [int(i) for i in input().split()]
        l = sorted(l)
        hypotenuse = math.sqrt(l[0]**2 + l[1]**2)
        if hypotenuse == l[2]:
            print('R', end=" ")
        elif hypotenuse < l[2]:
            print('O', end=' ')
        else:
            print('A', end=' ')
        n -= 1
pyth(int(input()))

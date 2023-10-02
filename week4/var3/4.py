import math
primes = [2,3]
for i in range(4, 2760000):
    check = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            check = False
    if(check): primes.append(i)

a = [int(i) for i in input().split()]
for elem in a:
    print(primes[elem - 1], end = " ")
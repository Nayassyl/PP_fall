def sum(k):
    while (k != 0):
        a = int(input())
        b = int(input())
        n = int(input())
        print((a*n + b*(n*(n-1))/2))
        k -= 1

sum(int(input()))

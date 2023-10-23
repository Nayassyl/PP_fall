def closest(listt, n):
    sorted(listt)
    for i in range(len(listt)):
        if listt[i] >= n:
            return listt[i - 1]

a = [int(i) for i in input().split()]
n = int(input())
print(closest(a, n))
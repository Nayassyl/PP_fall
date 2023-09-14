n = int(input())
sum = 0
cnt = 0
while(n):
    sum += n
    cnt += 1
    av = sum / cnt
    n = int(input())
print (sum, av)
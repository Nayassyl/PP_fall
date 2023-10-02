def rotate(l):
    l = l[-1:] + l[:-1]
    return l
listt = [i for i in input().split()]
print(rotate(listt))
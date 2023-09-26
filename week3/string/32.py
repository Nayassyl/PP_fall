def firstn_tolower(st, n):
    print(st[:n].lower()+ st[n:])
st = input()
n = int(input())
firstn_tolower(st, n)
import re
# def if_Valid(st):
#     return re.search(([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+, st)
def l(list):
    listt = []
    for elem in list:
        if re.search("@hackerrank.com", elem):
            listt.append(elem)
    print(sorted(listt))
n = int(input())
list = []
while n:
    st = input()
    list.append(st)
    n -= 1
l(list)
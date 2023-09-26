a = [i for i in input().split()]
for elem in a:
    print(elem[0].upper() + elem[1:len(elem) - 1] + elem[len(elem) - 1].upper(), end = " ")
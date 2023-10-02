a = [int(i) for i in input().split()]
b = sorted(a)
c = []
for elem in b:
    for i in range(len(a)):
        if elem == a[i]:
            c.append(i + 1)
            break
for elem in c: print(elem, end = " ")
#just input a list, size is not necessary
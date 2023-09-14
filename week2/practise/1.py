a = [int(i) for i in input().split()]
for elem in a:
    if elem == 0 or elem % 35 != 0: print("no")
    else: print("yes")
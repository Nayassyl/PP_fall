a = [int(i) for i in input().split()]
cntodd, cnteven, cntzero = 0, 0, 0
for elem in a:
    if elem == 0: cntzero += 1
    elif elem % 2 != 0: cntodd += 1
    else: cnteven += 1
print("Number of zero numbers: ", cntzero)
print("Number of even numbers: ", cnteven)
print("Number of odd numbers: ", cntodd)
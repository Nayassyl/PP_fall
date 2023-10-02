def make_pairr(a, b):
    listt = []
    if len(a) == len(b):
        for i in range(len(a)):
            listt.append((a[i], b[i]))
    elif len(a) > len(b):
        b += b[:len(a) - len(b)]
        for i in range(len(a)):
            listt.append((a[i], b[i]))
    else:
        a += a[:len(b) - len(a)]
        for i in range(len(b)):
            listt.append((a[i], b[i]))
    return set(listt)
list1 = [2,3,4,5,6,7,8]
list2 = [4,9,16,25,36,49,64]
print(make_pairr(list1, list2))
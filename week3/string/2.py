def freg(st):
    dict = {}
    for elem in st:
        keys = dict.keys()
        if elem in keys:
            dict[elem] += 1
        else:
            dict[elem] = 1
    return dict
print(freg(input()))


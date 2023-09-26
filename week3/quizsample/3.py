def kreker4(container):
    d = dict()
    for i in container:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    count = 0
    l = []
    for key, value in d.items():
        if value > count:
            l.append(key)
            count = value
    return l[len(l)-1]
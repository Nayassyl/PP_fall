def remove_odd(st):
    st1  = ""
    for i in range(len(st)):
        if i % 2 != 0:
            st1 += st[i]
    return st1
print(remove_odd(input()))

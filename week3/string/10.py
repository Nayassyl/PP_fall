def change_first_last(st):
    return (st[len(st) - 1] + st[1:len(st) - 1] + st[0])
print(change_first_last(input()))
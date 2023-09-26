def to_middle(st1, st2):
    return st1[:len(st1) // 2] + st2 + st1[len(st1) // 2:]

st1 = input()
st2 = input()
print(to_middle(st1, st2))
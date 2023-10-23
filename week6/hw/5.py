import re
n = int(input())


def is_Valid(st):
    if st[0] == '+':
        st = st[1:]
    if re.findall('\D', st):
        return False
    if len(st) != 10 and len(st) != 11:
        return False
    return bool(re.search('^[7-8]', st))


while n:
    st = ""
    list = [i for i in input().split()]
    for elem in list:
        st += elem
    print(is_Valid(st))
    n -= 1

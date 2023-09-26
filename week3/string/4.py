def change(st):
    ch = st[0]
    st = st.replace(ch, '$')
    st = ch + st[1:]
    return st

print(change(input()))

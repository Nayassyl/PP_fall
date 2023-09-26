def to_upper(st):
    cnt = 0
    for i in range(4):
        if st[i] == st[i].upper(): cnt += 1
    if cnt >= 2: return st.upper()
    return st
print(to_upper(input()))

def non_repeat(st):
    for elem in st:
        if st.count(elem) == 1:
            return elem
    return "all characters are repeating"
print(non_repeat(input()))
def repeat(st):
    for elem in st:
        if st.count(elem) > 1:
            return elem
    return "all characters are unique"
print(repeat(input()))
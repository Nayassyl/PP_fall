def repeated_word(st):
    a = set()
    for elem in st.split():
        if elem in a: return elem
        else: a.add(elem)
    return "no repeated words"
print(repeated_word(input()))
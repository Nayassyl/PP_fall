def occurence(st):
    words = {}
    for elem in st.split():
        if elem in words:
            words[elem] += 1
        else:
            words[elem] = 1
    a = sorted(words.values(), reverse = True)
    for (i, j) in words.items():
        if j == a[1]:
            return i
print(occurence(input()))
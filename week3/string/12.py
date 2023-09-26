def word_occurence(st):
    wordss = dict()
    for words in st.split():
        if words in wordss:
            wordss[words] += 1
        else:
            wordss[words] = 1
    return wordss
print(word_occurence(input()))

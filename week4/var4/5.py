def longest():
    with open("file.txt", 'r') as f:
        max_length = 0
        max_word = ""
        for i in f:
            for j in i.split(' '):
                if len(j) > max_length:
                    max_length = len(j)
                    max_word = j
        print(max_word)
longest()
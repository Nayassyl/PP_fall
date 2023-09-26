def occurence(st):
    letters = dict()
    for letter in st:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

a = occurence(input())
for elem in sorted(a, key = a.get, reverse = True):
    if a[elem] > 1: print( elem, a)
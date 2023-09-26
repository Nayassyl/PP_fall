vowel = ['a', 'e', 'o', 'i', 'u']
def translate(st, cnt=0):
    if st[0] in vowel:
        if cnt > 0:
            return st + "ay"
        return st + "yay"
    elif cnt == len(st):
        return "Not vowels in string"
    else:
        st = st[1:] + st[0]
        cnt += 1
        return translate(st, cnt)

print(translate(input()))

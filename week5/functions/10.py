def findalll(string, char):
    a = []
    for i in range(len(string)):
        if string[i] == char:
            a.append(i)
    return a

string = input()
char = input()
print(findalll(string, char))
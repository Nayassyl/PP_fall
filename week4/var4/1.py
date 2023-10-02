aa = input()
a = [i for i in aa]
l = '_' * len(a)
b = [i for i in '_' * len(aa)]
print("Welcome to Hangman!")
print(l)
while(b != a):
    letter = input("Guess you letter:")
    if letter in a:
        for i in range(len(a)):
            if a[i] == letter:
                b[i] = letter
        for i in b:
            print(i, end = "")
        print()
    else: print("Incorrect!")
print("you won!")
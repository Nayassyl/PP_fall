import random
r = random.randint(1, 9)
while True:
    a = int(input("Guess the number (between 1 and 9): "))
    if a == r:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again.")

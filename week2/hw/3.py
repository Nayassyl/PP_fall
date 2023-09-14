y = int(input("Input a dog's age in human years: "))
yh = 0
for i in range(1, y + 1):
    if i <= 2: yh += 10.5
    else: yh += 4
print("The dog's age in dog's years is: ", int(yh))
print("Enter a list of values:")
l = [i for i in input().split()]
print("Enter a specified value:")
a = input()

print(bool(a in l))

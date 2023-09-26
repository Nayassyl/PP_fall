import textwrap
a = input()
b = []
while(a):
    b.append(a)
    a = input()

for elem in b:
    print(textwrap.dedent(elem), end = " ")

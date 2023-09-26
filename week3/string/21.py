import textwrap
st = input()
a = input()
b = []
while(a):
    b.append(a)
    a = input()

for elem in b:
    print(textwrap.indent(elem, st))
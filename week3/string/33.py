a = input() 
b = ''
for elem in a:
    if elem == '.':
        b += ','
        continue
    if elem == ',': 
        b += '.'
        continue
    b += elem
print(b)
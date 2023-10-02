d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
   {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, 
   {'name':'Princess', 'phone':'555-3141', 'email':''}, 
   {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]
l1 = []
l2 = []
for user in d:
    for x,y in user.items():
        if x == 'phone' and y[len(y) - 1] == '8':
            l1.append(user['name'])
        if x == 'email' and y == '':
            l2.append(user['name'])
for i in l1: print(i, end = " ")
print()
for i in l2: print(i, end = " ")

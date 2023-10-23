birthdays = {
    "Assylkhan Nursaya" : '20/04/05',
    'Onggarbay Armanzhan' : '07/10/2005',
    'Assylkhan Inkar' : '15/05/2007'
}
print("Welcome to the birthday dictionary! We know the birthdays of:")
for elem in birthdays:
    print(elem)
print("Who's birthday do you want to look up?")
name = input()
for elem in birthdays:
    if elem == name:
        res = "{}'s birthday is {}"
        print(res.format(elem, birthdays[elem]))
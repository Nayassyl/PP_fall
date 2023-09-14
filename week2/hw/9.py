ms = {
    '1' : 'January',
    '2' : 'February',
    '3' : 'March',
    '4' : 'April',
    '5' : 'May',
    '6' : 'June',
    '7' : 'July',
    '8' : 'August',
    '9' : 'September',
    '10' : 'October',
    '11' : 'November',
    '12' : 'December'
}
a = input("Input the month (e.g. [1-12]):")
m = int(a);
if m > 2 and m < 6: st = 'spring'
elif m > 5 and m < 9: st = "summer"
elif m > 8 and m < 12: st = 'autumn'
else: st = 'winter'
d = int(input("Input the day:"))
for x in ms:
    if a == x: print(ms[x],",", d,".Season is" , st)

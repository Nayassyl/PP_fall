def ily(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
       return True
    return False

def gnd(y, m, d):
   ds = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   if ily(y):
       ds[2] = 29
   if d < ds[m]:
       nd = d + 1
       nm = m
       ny = y
   else:
       nd = 1
       if m < 12:
           nm = m + 1
           ny = y
       else:
           nm = 1
           ny = y + 1
   return ny, nm, nd

y = int(input("Input a year: "))
m = int(input("Input a month [1-12]: "))
d = int(input("Input a day [1-31]: "))

ny, nm, nd = gnd(y, m, d)

# Output

print(f"The next date is [{ny}-{nm}-{nd}]")
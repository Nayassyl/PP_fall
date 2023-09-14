s = input()
bl = True
try: int(s)
except ValueError: bl = False
if bl: print('The string is an integer.')
else: print('The string is not an integer.')
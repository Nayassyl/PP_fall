def ctf(C):
    F = (C * 9/5) + 32
    return F

def ftc(F):
    C = (F - 32) * 5/9
    return C

g = input()
if "°C" in g:
    C = int(g[:2])
    F = int(ctf(C))
    print(g,"is",F, "in Fahrenheit")
elif "°F" in g:
    F = int(g[:2])
    C = int(ftc(F))
    print(g,"is",C,"in Celcius")
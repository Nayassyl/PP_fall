def fibbo(n):
    if n <= 1:
        return n
    else:
        return fibbo(n - 2) + fibbo(n - 1)

for i in range(1, 51):
    if fibbo(i) <= 50:
        print(fibbo(i), end = " ")
    else: break
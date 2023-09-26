def delete_nth(st, n):
    try:
        if len(st) == 0 or n > len(st):
            raise Exception()
    except:
        print("Wrong input!")
    else:
        print(st[:n - 1] + st[n:])

st = input()
n = int(input())
delete_nth(st, n)
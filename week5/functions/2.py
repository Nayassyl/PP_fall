def add_exitement(listt):
    for string in listt:
        string += '!'
        print(string, end = " ")
a = [i for i in input().split()]
add_exitement(a)


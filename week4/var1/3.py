def is_match(list, strr):
    for i in list:
        if (len(strr) == len(i)):
            check = True
            for j in range(len(strr)):
                if strr[j] != '*' and i[j] != strr[j]:
                    check = False
                    break
            if check:
                print(i, end=' ')

listt = [i for i in input().split()]
string = input()
is_match(listt, string)
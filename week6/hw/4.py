import re
def subs():
    for i in range(int(input())):
        s = re.sub("(?<=\s)&&(?=\s)", "and", input())
        print(re.sub("(?<=\s)\|\|(?=\s)", "or", s))
subs()
import re
def is_Valid():
    n = int(input())
    while n:
        st = input()
        name, emaill = [i for i in st.split()]
        email = emaill[1:len(emaill) - 1]
        if re.match('([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email):
            print(name, email)
        n -= 1
is_Valid()

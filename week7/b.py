import re

def rewrite_password(line, username, new_password):
    parts = line.split(':')
    if len(parts) == 2:
        existing_username, existing_password = parts
        if existing_username == username:
            return f'{username}:{new_password}\n'
    return line

def change_password2(users, password, login):
    temp_login = ''
    new_password = ''
    ok = False
    if login in users and users[login] == password:
        check = input('Welcome, would you like to change your password(yes/no): ')
        if check.lower() == 'yes':
            print('Provide your new password')
            while new_password == password:
                new_password = change_password()
            temp_login = login
            ok = True
        elif check.lower() == 'no':
            print(f'Welcome, my friend: {login}')
            # quit()
        
    
    if ok:
        with open('Users.txt', 'r') as file1:
            lines = file1.readlines()
        modified_lines = [rewrite_password(line, temp_login, new_password) for line in lines]
        with open('Users.txt', 'w') as file2:
            file2.writelines(modified_lines)
            print('Password changed')

def change_password():
    flag = True
    while flag:
        new_password = input()
        if check_password(new_password):
            print('Valid password')
            flag = False
            return new_password
        else:
            print('Please provide a valid new password')
            # quit()

def check_password(p):
    a = re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?@#$%^&*])[a-zA-Z0-9!?@$%^&*]+', p)
    return bool(a)

def Checker(p):
    users = {}
    with open('Users.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(':')
            if len(parts) == 2:
                k, v = parts
                users[str(k)] = v 
    if p in users.keys():
        return True
    else:
        return False

def Log_in(login, pasword):
    login = input('Log in: ')
    password = input('Password: ')
    if not Checker(login):
        print("You didn't sign in")

def Sing_in(login, password):
    flag1 = True
    while flag1:
        if check_password(password):
            break
        password = input('Please provide a valid new password: ')
    modified_lines = login + ':' + password
    with open('Users.txt', 'a') as file2:
        file2.write('\n' + modified_lines)
        # a = Label(wind2, text = 'Welcome')


from tkinter import *
from functools import partial



wind1 = Tk()  
wind1.geometry('400x150')  
wind1.title('Main window')


def toRegForm():
    wind2 = Tk()
    wind2.geometry('400x150')
    wind2.title = ('Registration Form')
    usernameLabel = Label(wind2, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(wind2, textvariable=username).grid(row=0, column=1)  
    userr = username.get()
    
    
    passwordLabel = Label(wind2,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(wind2, textvariable=password, show='*').grid(row=1, column=1)  
    passw = password.get()
    
    RegButton = Button(wind2, text="Registration", command=lambda: Sing_in(userr, passw)).grid(row=4, column=0)
    

    


	
def toLogForm():
    wind3 = Tk()
    wind3.geometry('400x150')
    wind3.title = ('Login Form')
    usernameLabel = Label(wind3, text="User Name").grid(row=0, column=0)
    username = StringVar()
    usernameEntry = Entry(wind3, textvariable=username).grid(row=0, column=1)  

    passwordLabel = Label(wind3,text="Password").grid(row=1, column=0)  
    password = StringVar()
    passwordEntry = Entry(wind3, textvariable=password, show='*').grid(row=1, column=1)  

    loginButton = Button(wind3, text="Login", command = Log_in).grid(row=4, column=0)
    print(username.get(), password.get())

# Windows

LogBut = Button(wind1, text = 'Login', command = toLogForm).grid()
RegBut = Button(wind1, text = 'Registration', command = toRegForm).grid()

# # Username label and text entry box
# usernameLabel = Label(wind1, text="User Name").grid(row=0, column=0)
# username = StringVar()
# usernameEntry = Entry(wind1, textvariable=username).grid(row=0, column=1)  

# # Password label and password entry box
# passwordLabel = Label(wind1,text="Password").grid(row=1, column=0)  
# password = StringVar()
# passwordEntry = Entry(wind1, textvariable=password, show='*').grid(row=1, column=1)  

# validateLogin = partial(validateLogin, username, password)

# # Login button
# loginButton = Button(wind1, text="Login", command=validateLogin).grid(row=4, column=0)  

wind1.mainloop()
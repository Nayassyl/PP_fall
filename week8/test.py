import pymysql
from tkinter import *
from functools import partial
import re

# database connection
connection = pymysql.connect(host="localhost", port=3306, user="root", password = "Qazzaq1@", database="test")
cursor = connection.cursor()

def inserting(login, password):
    sql= "INSERT INTO userss (login, password) VALUES (%s, %s)"
    val = (login, password)
    cursor.execute(sql, val)
    connection.commit()

def check_password(p):
    a = re.search(r'^(?=(.*[a-z]){3,})(?=(.*[A-Z]){2,})(?=(.*[0-9]){2,})(?=(.*[!@#$%^&*()\-__+.]){1,}).{8,}$', p)
    return bool(a)

def login_checker(login):
    sql = "SELECT * FROM userss WHERE login = %s"
    cursor.execute(sql, login)
    users = cursor.fetchall()
    return bool(users)

def sign_in(login, password):
    print(login, password)
    flag1 = True
    while flag1:
        if not check_password(password):
            root = Tk()
            a = Label(root, text = "Please provide correct password!\nPassword parameters:\n1)At least 2 uppercase letters\n2)At least 2 umbers\n3)Special characters\n4)At least 8 characters").grid()
            root.mainloop()
            break
        elif login_checker(login):
            root = Tk()
            a = Label(root, text = "This username already exist. Please provide new username").grid()
            root.mainloop()
            break
        else:
            inserting(login, password) 
            root = Tk()
            a = Label(root, text = "Welcome!").grid()
            
        

    


wind1 = Tk()  
wind1.geometry('400x150')  
wind1.title('Main window')


def toRegForm():
    wind2 = Tk()
    wind2.geometry('400x150')
    wind2.title = ('Registration Form')
    usernameLabel = Label(wind2, text="User Name").grid(row=0, column=0)
    usernameEntry = Entry(wind2)
    usernameEntry.grid(row=0, column=1)  
    
    
    passwordLabel = Label(wind2,text="Password").grid(row=1, column=0)  
    passwordEntry = Entry(wind2, show='*')
    passwordEntry.grid(row=1, column=1)  
    
    RegButton = Button(wind2, text="Registration", command=lambda:sign_in(usernameEntry.get(), passwordEntry.get()))
    RegButton.grid()

    

    


	
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

    loginButton = Button(wind3, text="Login", command = Log_in(username, password)).grid(row=4, column=0)

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


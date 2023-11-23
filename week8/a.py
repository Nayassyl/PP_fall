import pymysql
from tkinter import *
from functools import partial
import re
import time

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

class windows(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.geometry = ("500x500")
        #self.resizable(True, True)
        self.configure(bg = '#1C1C1C')
        self.switch_frame(Startpage)
        self.title("  ")
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.grid()
class Startpage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Frame.configure(self, bg = '#1C1C1C')
        Label(self, text = "Main Page", foreground = "white", background="#1C1C1C").grid(row = 1)
        Button(self, text = "Login", foreground = "white", background= "#1C1C1C", width = 20,
            command=lambda: master.switch_frame(LoginPage)).grid(row = 3, pady = 5)
        Button(self, text="Sign in", foreground = "white", background = "#1C1C1C", width = 20,
                command=lambda: master.switch_frame(Signinpage)).grid(row =4, pady = 5)

class Signinpage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Button(self, text="Back", foreground="white",background="#1C1C1C",  width = 20,
                  command=lambda: master.switch_frame(Startpage)).grid(row = 8)
        Label(self, text="Name", foreground = "white", background = "#1C1C1C").grid(row = 1)
        Label(self, text="Password", foreground = "white", background = "#1C1C1C").grid(row = 3, pady=5)
        aa =  Label(self, text = "Password parameters:\n1)At least 2 uppercase letters\n2)At least 2 umbers\n3)Special characters\n4)At least 8 characters", background="#1C1C1C", foreground= "white").grid(row = 5, pady = 5)
        name = Entry(self, background = "black", foreground= "white")
        password = Entry(self, background = "black", foreground= "white")
        name.grid(row = 2,pady = 5)
        password.grid(row = 4, pady = 5)

        def sign_in(login, passwordd):
            if not check_password(passwordd):
                password.delete(0, len(password.get()))
                password.insert(0, "Invalid Password")
                time.sleep(2)
                password.delete(0, len(password.get()))
            elif login_checker(login):
                name.delete(0, len(name.get()))
                name.insert(0,"Existed Login")
                time.sleep(2)
                name.delete(0, len(name.get()))
            else:
                inserting(login, passwordd)
                a = Label(self, text = "You are registered successfully! Please Log In", foreground="white", background= "#1C1C1C").grid(row = 4, column = 0)
                tolog = Button(self, text = "Log In Page", foreground = "white", background="#1C1C1C", command = lambda:master.switch_frame(LoginPage))
                tolog.grid(row = 6, pady = 5)

            
        
        b = Button(self, text = "Sign in", foreground = "white", background="#1C1C1C", width = 20, command = lambda: sign_in(name.get(), password.get()))
        b.grid(row = 7, pady = 5)
        
        
class LoginPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Button(self, text="Back", foreground = "white", background = "#1C1C1C", width=20,
                  command=lambda: master.switch_frame(Startpage)).grid(row = 7)
        Label(self, text="UserName", foreground = "white", background = "#1C1C1C").grid(row = 1)
        Label(self, text="Password", foreground = "white", background = "#1C1C1C").grid(row = 3,pady=5)

        username = Entry(self, background = "black", foreground= "white")
        passwordd = Entry(self, background = "black", foreground= "white", show = "*")
        username.grid(row = 2,pady = 5)
        passwordd.grid(row = 4, pady = 5)

        def log(login, passw):
            sql = "select * from userss where login = %s"
            cursor.execute(sql, login)
            users = cursor.fetchall()
            if not users:
                username.delete(0, len(username.get()))
                username.insert(0,"Invalid Login")
                time.sleep(2)
                username.delete(0, len(username.get()))
            else:
                if users[0][2] != passw:
                    passwordd.delete(0, len(passwordd.get()))
                    passwordd.insert(0,"Invalid password")
                    time.sleep(2)
                    passwordd.delete(0, len(passwordd.get()))
                else:
                    master.switch_frame(UserPage)
        
        Button(self, text = "Login", foreground = "white", background="#1C1C1C", width = 20, command = lambda: log(username.get(), passwordd.get())).grid(row = 6, pady = 5)

class UserPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Button(self, text="Back", foreground = "white", background = "#1C1C1C", width=20,
                  command=lambda: master.switch_frame(Startpage)).grid(row = 4, pady = 10)
        Label(self, text="Welcome!", foreground = "white", background = "#1C1C1C").grid(row = 1)
        Button(self, text="Change password", foreground = "white", background = "#1C1C1C", width=15, height=3,
                  command=lambda: master.switch_frame(Changepass)).grid(pady = 5, row = 2)
        Button(self, text="Change login", foreground = "white", background = "#1C1C1C", width = 15, height=3,
                  command=lambda: master.switch_frame(Changelog)).grid(pady = 5,row =3)

class Changepass(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Button(self, text="Back", foreground = "white", background = "#1C1C1C", width=20,
                  command=lambda: master.switch_frame(UserPage)).grid(row = 8, pady = 5)
        Label(self, text="Login", foreground = "white", background = "#1C1C1C").grid(row = 1)
        Label(self, text="Old password", foreground = "white", background = "#1C1C1C").grid(row = 3,pady=5)
        Label(self, text="New password", foreground = "white", background = "#1C1C1C").grid(row = 5,pady=5)

        log = Entry(self, background = "black", foreground= "white")
        oldpass = Entry(self, background = "black", foreground= "white")
        newpass = Entry(self, background = "black", foreground= "white")
        log.grid(row = 2, pady = 5)
        oldpass.grid(row = 4, pady = 5)
        newpass.grid(row = 6,pady = 5)
        def change_pass(login, password, new_password):
            sql = "select * from userss where login = %s"
            users = cursor.execute(sql, login)
            if not users:
                log.delete(0, len(log.get()))
                log.insert(0,"Invalid Login")
                time.sleep(2)
                log.delete(0, len(log.get()))

            if users[0][2] != password:
                oldpass.delete(0, len(oldpass.get()))
                oldpass.insert(0,"Wrong password")
                time.sleep(2)
                oldpass.delete(0, len(oldpass.get()))
            else:
                if not check_password:
                    newpass.delete(0, len(newpass.get()))
                    newpass.insert(0,"Invalid password")
                    time.sleep(2)
                    newpass.delete(0, len(newpass.get()))
                else:
                    sql = "update userss set password = %s where id = %d"
                    cursor.execute("update userss set password = %s where id = %d"%(new_password, users[0][0]))
                    cursor.commit()
        Butt = Button(self, text = "Change Password", background = "#1C1C1C", foreground= "white",width = 20,  command = lambda:change_pass(log.get(),oldpass.get(), newpass.get()))
        Butt.grid(row = 7)

class Changelog(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Button(self, text="Back", foreground = "white", background = "#1C1C1C", width=20,
                  command=lambda: master.switch_frame(UserPage)).grid(row = 6)
        Label(self, text="Login", foreground = "white", background = "#1C1C1C").grid(row = 1)
        Label(self, text="New Login", foreground = "white", background = "#1C1C1C").grid(row = 3,pady= 5)
        oldname = Entry(self, background = "black", foreground= "white")
        newname = Entry(self, background = "black", foreground= "white")
        oldname.grid(row = 2)
        newname.grid(row = 4)
        def change_login(o, n):
            if login_checker(n):
                newname.delete(0, len(newname.get()))
                newname.insert(0,"Existed login!")
                time.sleep(2)
                newname.delete(0, len(newname.get()))
            if not login_checker(o):
                oldname.delete(0, len(oldname.get()))
                oldname.insert(0,"Invalid Login")
                time.sleep(2)
                oldname.delete(0, len(oldname.get()))
            else:
                cursor.execute("select * from userss where login = %s", o)
                user = cursor.fetchall()
                cursor.execute("update userss set login = %s where id = %d "%(n, user[0][0]))
                cursor.commit()
        Butt = Button(self, text = "Change Login", foreground= "white", background= "#1C1C1C", command = lambda:change_login(oldname.get(), newname.get()))
        Butt.grid(row = 5)


            

wind = windows()
wind.mainloop()
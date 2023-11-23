import tkinter as tk
import psycopg2
from config import configuration
import re
import time
def execute_login(name,password):
    connection = None
    try:
        parameters = configuration()
        connection = psycopg2.connect(**parameters)
        cursor = connection.cursor()
        query = """INSERT INTO users(user_name,user_password) VALUES(%s,%s))"""
        cursor.execute(query,[name,password,])
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


def execute_signin():
    connection = None
    try:
        parameters = configuration()
        connection = psycopg2.connect(**parameters)
        cursor = connection.cursor()
        query = """SELECT * FROM users"""
        cursor.execute(query)
        rows = cursor.fetchall()
        connection.commit()
        cursor.close()
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
def check_password(password):
    return bool(re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?@#$%^&*])[a-zA-Z0-9!?@$%^&*]+', password))
    


class app(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.geometry("300x300+600+250")
        self.resizable(True, True)
        self.configure(bg="#65A8E2")
        self.switch_frame(Startpage)
        self.title("ДАУНЫ")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid(row = 0,column = 0)


class Startpage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Main Page", foreground="#65A8E2").grid(column=2,row = 1,padx= 40)
        tk.Button(self, text="Login", foreground="#65A8E2", width=10, height=3,
                  command=lambda: master.switch_frame(Loginpage)).grid(column= 1,row = 3)
        tk.Button(self, text="Sign in", foreground="#65A8E2", width = 10, height=3,
                  command=lambda: master.switch_frame(Signinpage)).grid(column = 3,row =3)


class Loginpage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master) 
        tk.Button(self, text="<--", foreground="#65A8E2", width=3, height=1,
                  command=lambda: master.switch_frame(Startpage)).grid(row = 0, column= 0)
        tk.Label(self, text="Name", foreground="#65A8E2").grid(row = 1 , column= 0,)
        tk.Label(self, text="Password", foreground="#65A8E2").grid(row = 2, column= 0,pady=10)
        name = tk.Entry(self)
        password = tk.Entry(self)
        name.grid(row = 1,column = 2)
        password.grid(row = 2, column = 2)
        def exlogin(n,p):
                if check_password(p):
                    execute_login(n,p)
                else:
                    password.delete(0,len(password.get()))
                    password.insert(0,"Invalid password")
        tk.Button(self, text="Login", foreground="#65A8E2", command=lambda: exlogin(name.get(),password.get()),
                  width=8, height=3).grid(row = 6 , column = 8)


class Signinpage(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        tk.Button(self, text="<--", foreground="#65A8E2", width=3, height=1,
                  command=lambda: master.switch_frame(Startpage)).grid(row = 0, column= 0)
        tk.Label(self, text="Name", foreground="#65A8E2").grid(row = 1 , column= 0,)
        tk.Label(self, text="Password", foreground="#65A8E2").grid(row = 2, column= 0,pady=10)
        name = tk.Entry(self)
        password = tk.Entry(self)
        name.grid(row = 1,column = 2)
        password.grid(row = 2, column = 2)
        def exsignin(n,p):
            rows = execute_signin()
            for i in rows:
                if i[0] == n and i[1] == p:
                    name.delete(0,len(name.get()))
                    password.delete(0,len(password.get()))
                    name.insert("Success")
                    password.insert("Success")
                    time.sleep(2)
                    name.delete(0,len(name.get()))
                    password.delete(0,len(password.get()))
                    return True
            return False
        tk.Button(self, text="Sign in", foreground="#65A8E2", command=lambda: execute_signin(name.get(), password.get()),
                  width=8, height=3).grid(row = 6 , column = 8)
        
programma = app()
programma.mainloop()

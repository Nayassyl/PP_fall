from tkinter import *


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
        Frame.configure(self, bg = '#1C1C1C')
        Label(self, text = "Dimensions of first matrix:", foreground = "white", background="#1C1C1C").grid(row = 1, column = 1)
        Label(self, text = "x", foreground= "white", background="#1C1C1C").grid(row = 1, column = 3)
        n1 = Entry(self, foreground="white", background = "black", width = 5)
        n1.grid(row = 1, column = 2)
        m1 = Entry(self, foreground="white", background = "black", width = 5)
        m1.grid(row = 1, column = 4)

        global arr1
        arr1 = matrix()
        arr1.set_row(n1.get())
        arr1.set_column(m1.get())

        Label(self, text = "Dimensions of second matrix:", foreground = "white", background="#1C1C1C").grid(row = 2, column = 1)
        Label(self, text = "x", foreground= "white", background="#1C1C1C").grid(row = 2, column = 3)
        n2 = Entry(self, foreground="white", background = "black", width = 5)
        n2.grid(row = 2, column = 2)
        m2 = Entry(self, foreground="white", background = "black", width = 5)
        m2.grid(row = 2, column = 4)
        
        global arr2
        arr2 = matrix()
        arr2.set_row(n2)
        arr2.set_column(m2)

        Button(self, text = "OK", background= "black", foreground="white", width = 5, command = lambda:master.switch_frame(EnterPage)).grid(row = 3, column = 4)

class EnterPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self, bg = "#1C1C1C")
        Label(self, text="Enter matrix :", font=('arial', 10, 'bold'), 
        bg="bisque2").place(x=20, y=20)

        x2 = 0
        y2 = 0
        rows, cols = (arr1.get_rows(), arr1.get_column())
        for i in range(rows):
            for j in range(cols):

                entry = Entry(self ,width=3)
                entry.place(x=60 + x2, y=50 + y2)
                x2 += 30

        y2 += 30
        x2 = 0
        button= Button(self,text="Submit", bg='bisque3', width=15)
        button.place(x=160,y=140)

class matrix:
    def set_row(self, newrow):
        self.rows = int(newrow)
    def set_column(self, newcol):
        self.columns = int(newcol)
    def set_arr(self, newarr):
        self.arr = newarr
    def get_row(self):
        return self.rows
    def get_column(self):
        return self.columns
    def get_arr(self):
        return self.arr
wind = windows()
wind.mainloop()



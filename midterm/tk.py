from tkinter import *

root = Tk()
root.geometry("500x300")
l1 = Label(root, text = "REGISTRATION FORM").grid(row = 0, column = 2)
l2 = Label(root, text = "Name:").grid(row = 1, column = 1)
e1 = Entry(root).grid(row = 1, column = 2)
l3 = Label(root, text = "address:").grid(row = 1, column =  3)
e2 = Entry(root).grid(column = 4, row = 1)
l4 = Label(root, text = "Age:").grid(row = 2, column = 1)
e3 = Entry(root).grid(row = 2, column = 2)

l5 = Label(root, text = "Designation:").grid(row = 3, column = 1)
e4 = Spinbox(root).grid(row = 3, column = 2) 
l6 = Label(root, text = "Gender:").grid(row = 3, column = 3)
s1 = Radiobutton(root, text = "Male").grid(row = 3, column = 4)
s2 = Checkbutton(root, text = "Female").grid(row = 3, column = 5)
S

b1 = Button(root, text = "SUBMIT").grid(row = 7, column = 2)
root.mainloop()
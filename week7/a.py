import tkinter as tk


def F():
    print("Hello!")


root = tk.Tk()
l1 = tk.Label(root, text='Username')
e1 = tk.Entry(root)
e1.pack()
b1 = tk.Button(root, text='OK', command=lambda: F(e1.get()))
b1.pack()
root.mainloop()


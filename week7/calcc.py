from tkinter import *

class body(Frame):
    def __init__(self, root):
        super(body, self).__init__(root)
        self.build()
    def build(self):
        self.formula = "0"
        self.label = Label(text = self.formula, font = ("Times New Roman", 20, "bold" ), background = "black", foreground = "white")
        self.label.place(x = 10, y = 50)

        buttons = [
            "C", "DEL", "%", "/",
            "7", "8", "9", "*",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "(", "0", ")", "="
        ]

        x = 10
        y = 140
        for bt in buttons:
            com = lambda x = bt:self.commands(x)
            Button(text = bt, background = "orange", font = ("Times New Roman", 15), command = com).place(x = x, y = y, width = 110, height = 78)
            x += 115
            if x > 400:
                x = 10
                y += 80    
    def commands(self, op):
        if op == "C":
            self.formula = ""
        elif op == "DEL":
            self.formula = self.formula[0: -1]
        elif op == "%":
            self.formula = str((eval(self.formula)) / 100)
        elif op == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += op
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.label.configure(text = self.formula)

if __name__ == '__main__':
    root = Tk()
    root["background"] = "black"
    root.geometry("485x550+200+200")
    root.title("Calculator")
    root.resizable(False, False)
    app = body(root)
    app.pack()
    root.mainloop()

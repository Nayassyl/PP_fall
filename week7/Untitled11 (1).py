#!/usr/bin/env python
# coding: utf-8

# In[2]:


from tkinter import *
root = Tk()
root.mainloop()


# In[9]:


from tkinter import Label
widget=Label(None,text='HelloWorld')
widget.pack()
widget.mainloop()


# In[8]:


from tkinter import *
def quit():
    print ('Hello, getting out of here')
root = Tk()
window2 = Tk()
widget = Button(window2, text='Press me to quit' , command=quit)
widget.pack()
window2.mainloop()
root.mainloop()


# In[16]:


from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
def take():
    print (E1.get())
    window2 = Tk()
    L2 = Label(window2, text="Welcome")
    L2.pack()
    window2.mainloop()
button = Button(top, text='Ok' , command=take)
button.pack()
top.mainloop()


# In[17]:


from tkinter import *
def cb():
    print ("variable is", var.get())
win = Tk()
var = IntVar()
c = Checkbutton(
win, text="Enable Tab",
variable=var,
command= (lambda: cb()))
c.pack()
win.mainloop()


# In[19]:



class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.formula = "0"
        self.lbl = Label(text=self.formula, font=("Times New Roman", 21, "bold"), bg="#000", foreground="#FFF")
        self.lbl.place(x=11, y=50)

        btns = [
            "C", "DEL", "*", "=",
            "1", "2", "3", "/",
            "4", "5", "6", "+",
            "7", "8", "9", "-",
            "(", "0", ")", "X^2"
        ]

        x = 10
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 15),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117
            if x > 400:
                x = 10
                y += 81

    def logicalc(self, operation):
        if operation == "C":
            self.formula = ""
        elif operation == "DEL":
            self.formula = self.formula[0:-1]
        elif operation == "X^2":
            self.formula = str((eval(self.formula))**2)
        elif operation == "=":
            self.formula = str(eval(self.formula))
        else:
            if self.formula == "0":
                self.formula = ""
            self.formula += operation
        self.update()

    def update(self):
        if self.formula == "":
            self.formula = "0"
        self.lbl.configure(text=self.formula)


if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#000"
    root.geometry("485x550+200+200")
    root.title("Калькулятор")
    root.resizable(False, False)
    app = Main(root)
    app.pack()
    root.mainloop()


# In[21]:
from tkinter import *


root=Tk()
root.title("Ayana's keyboard")
root.geometry('800x800')

buttonA=Button(height=2, width=5, text='a', bg='white')
buttonA.place(x=155, y=344)
buttonB=Button(height=2, width=5, text='b', bg='white')
buttonB.place(x=360,y=386)
buttonC=Button(height=2, width=5, text='c', bg='white')
buttonC.place(x=270, y=386)
buttonCaps=Button(height=2, width=10, text='CapsLk', bg='white')
buttonD=Button(height=2, width=5, text='d', bg='white')
buttonD.place(x=245,y=344)
buttonE=Button(height=2, width=5, text='e', bg='white')
buttonE.place(x=230,y=302)
buttonF=Button(height=2, width=5, text='f', bg='white')
buttonF.place(x=290,y=344)
buttonG=Button(height=2, width=5, text='g', bg='white')
buttonG.place(x=335,y=344)
buttonH=Button(height=2, width=5, text='h', bg='white')
buttonH.place(x=380,y=344)
buttonI=Button(height=2, width=5, text='i', bg='white')
buttonI.place(x=455,y=302)
buttonJ=Button(height=2, width=5, text='j', bg='white')
buttonJ.place(x=425,y=344)
buttonK=Button(height=2, width=5, text='k', bg='white')
buttonK.place(x=470,y=344)
buttonL=Button(height=2, width=5, text='l', bg='white')
buttonL.place(x=515,y=344)
buttonM=Button(height=2, width=5, text='m', bg='white')
buttonM.place(x=450, y=386)
buttonN=Button(height=2, width=5, text='n', bg='white')
buttonN.place(x=405, y=386)
buttonO=Button(height=2, width=5, text='o', bg='white')
buttonO.place(x=500,y=302)
buttonP=Button(height=2, width=5, text='p', bg='white')
buttonP.place(x=545,y=302)
buttonQ=Button(height=2, width=5, text='q', bg='white')
buttonQ.place(x=140,y=302)
buttonR=Button(height=2, width=5, text='r', bg='white')
buttonR.place(x=275,y=302)
buttonS=Button(height=2, width=5, text='s', bg='white')
buttonS.place(x=200,y=344)
buttonT=Button(height=2, width=5, text='t', bg='white')
buttonT.place(x=320,y=302)
buttonU=Button(height=2, width=5, text='u', bg='white')
buttonU.place(x=410,y=302)
buttonV=Button(height=2, width=5, text='v', bg='white')
buttonV.place(x=315, y=386)
buttonW=Button(height=2, width=5, text='w', bg='white')
buttonW.place(x=185,y=302)
buttonX=Button(height=2, width=5, text='x', bg='white')
buttonX.place(x=225,y=386)
buttonY=Button(height=2, width=5, text='y', bg='white')
buttonY.place(x=365,y=302)
buttonZ=Button(height=2, width=5, text='z', bg='white')
buttonZ.place(x=180,y=386)

button0=Button(height=2, width=5, text='0      )', bg='white')
button0.place(x=525,y=260)
button1=Button(height=2, width=5, text='1      !', bg='white')
button1.place(x=120,y=260)
button2=Button(height=2, width=5, text='2      @', bg='white')
button2.place(x=165,y=260)
button3=Button(height=2, width=5, text='3      #', bg='white')
button3.place(x=210,y=260)
button4=Button(height=2, width=5, text='4      $', bg='white')
button4.place(x=255,y=260)
button5=Button(height=2, width=5, text='5      %', bg='white')
button5.place(x=300,y=260)
button6=Button(height=2, width=5, text='6      ^', bg='white')
button6.place(x=345,y=260)
button7=Button(height=2, width=5, text='7      &', bg='white')
button7.place(x=390,y=260)
button8=Button(height=2, width=5, text='8      *', bg='white')
button8.place(x=435,y=260)
button9=Button(height=2, width=5, text='9      (', bg='white')
button9.place(x=480,y=260)

buttonSign=Button(height=2, width=5, text='`', bg='white')
buttonSign.place(x=75, y=260)
buttonMinus=Button(height=2, width=5, text='-      _', bg='white')
buttonMinus.place(x=570,y=260)
buttonEqual=Button(height=2, width=5, text='=      +', bg='white')
buttonEqual.place(x=615, y=260)
buttonSlash=Button(height=2, width=5, text='\\      |', bg='white')
buttonSlash.place(x=680,y=302)
buttonSlash2=Button(height=2, width=5, text='/      ?', bg='white')
buttonSlash2.place(x=585, y=386)
buttonBraces1=Button(height=2, width=5, text='[      {', bg='white')
buttonBraces1.place(x=590, y=302)
buttonBraces2=Button(height=2, width=5, text=']      }', bg='white')
buttonBraces2.place(x=635, y=302)
buttonSign2=Button(height=2, width=5, text=';      :', bg='white')
buttonSign2.place(x=560, y=344)
buttonSign3=Button(height=2, width=5, text="'      \"", bg='white')
buttonSign3.place(x=605, y=344)
buttonDot=Button(height=2, width=5, text='.      >', bg='white')
buttonDot.place(x=540, y=386)
buttonComa=Button(height=2, width=5, text=',      <', bg='white')
buttonComa.place(x=495, y=386)
buttonGmail=Button(height=2, width=7, text='@gmail', bg='white')
buttonGmail.place(x=210, y=428)
buttonCom=Button(height=2, width=7, text='.com', bg='white')
buttonCom.place(x=490,y=428)
buttonSpace=Button(height=2, width=30, bg='white')
buttonSpace.place(x=270,y=428)
buttonBackspace=Button(height=2, width=10, text='Backspace', bg='white')
buttonBackspace.place(x=660,y=260)

buttonReset=Button(text='RESET', width=7, bg='white')
buttonReset.place(x=430, y=0)
buttonDELETE=Button(text='DELETE', width=7, bg='white')
buttonDELETE.place(x=310,y=0)
buttonSave=Button(text='SAVE', width=7, bg='white')
buttonSave.place(x=370,y=0)
buttonCopy=Button(text='COPY', width=7, bg='white')
buttonCopy.place(x=490, y=0)
buttonCaps=Button(width=10, height=2, text='CapsLk', bg='white')
buttonCaps.place(x=75,y=344)
buttonShift=Button(height=2, width=10, text='Shift', bg='white')
buttonShift.place(x=100, y=386)
buttonEnter=Button(width=10, height=2, text='Enter', bg='white')
buttonEnter.place(x=650,y=344)

label=Label(width=113, bg='white')
label2=Label(width=113, height=10, bg='white')
label2.place(x=0,y=70)
label.place(x=0,y=40)

CAPS=0
Shift=0

def pressShift(event):
    global Shift
    if Shift==0:
        buttonShift['bg']='gray'
        Shift=1
def pressCaps(event):
    global CAPS
    if CAPS==1:
        CAPS=0
        buttonCaps['bg']='white'
    else:
        CAPS=1
        buttonCaps['bg']='gray'
def pressA(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='a'
    else:
        label['text']+='A'
        Shift=0
        buttonShift['bg']='white'
def pressB(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='b'
    else:
        label['text']+='B'
        Shift=0
        buttonShift['bg']='white'
def pressC(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='c'
    else:
        label['text']+='C'
        Shift=0
        buttonShift['bg']='white'
def pressD(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='d'
    else:
        label['text']+='D'
        Shift=0
        buttonShift['bg']='white'
def pressE(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='e'
    else:
        label['text']+='E'
        Shift=0
        buttonShift['bg']='white'
def pressF(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='f'
    else:
        label['text']+='F'
        Shift=0
        buttonShift['bg']='white'
def pressG(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='g'
    else:
        label['text']+='G'
        Shift=0
        buttonShift['bg']='white'
def pressH(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='h'
    else:
        label['text']+='H'
        Shift=0
        buttonShift['bg']='white'
def pressI(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='i'
    else:
        label['text']+='I'
        Shift=0
        buttonShift['bg']='white'
def pressJ(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='j'
    else:
        label['text']+='J'
        Shift=0
        buttonShift['bg']='white'
def pressK(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='k'
    else:
        label['text']+='K'
        Shift=0
        buttonShift['bg']='white'
def pressL(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='l'
    else:
        label['text']+='L'
        Shift=0
        buttonShift['bg']='white'
def pressM(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='m'
    else:
        label['text']+='M'
        Shift=0
        buttonShift['bg']='white'
def pressN(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='n'
    else:
        label['text']+='N'
        Shift=0
        buttonShift['bg']='white'
def pressO(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='o'
    else:
        label['text']+='O'
        Shift=0
        buttonShift['bg']='white'
def pressP(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='p'
    else:
        label['text']+='P'
        Shift=0
        buttonShift['bg']='white'
def pressQ(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='q'
    else:
        label['text']+='Q'
        Shift=0
        buttonShift['bg']='white'
def pressR(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='r'
    else:
        label['text']+='R'
        Shift=0
        buttonShift['bg']='white'
def pressS(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='s'
    else:
        label['text']+='S'
        Shift=0
        buttonShift['bg']='white'
def pressT(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='t'
    else:
        label['text']+='T'
        Shift=0
        buttonShift['bg']='white'
def pressU(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='u'
    else:
        label['text']+='U'
        Shift=0
        buttonShift['bg']='white'
def pressV(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='v'
    else:
        label['text']+='V'
        Shift=0
        buttonShift['bg']='white'
def pressW(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='w'
    else:
        label['text']+='W'
        Shift=0
        buttonShift['bg']='white'
def pressX(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='x'
    else:
        label['text']+='X'
        Shift=0
        buttonShift['bg']='white'
def pressY(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='y'
    else:
        label['text']+='Y'
        Shift=0
        buttonShift['bg']='white'
def pressZ(event):
    global Shift
    if CAPS==0 and Shift==0:
        label['text']+='z'
    else:
        label['text']+='Z'
        Shift=0
        buttonShift['bg']='white'

def press0(event):
    global Shift
    if Shift==0:
        label['text']+='0'
    else:
        label['text']+=')'
        Shift=0
        buttonShift['bg']='white'
def press1(event):
    global Shift
    if Shift==0:
        label['text']+='1'
    else:
        label['text']+='!'
        Shift=0
        buttonShift['bg']='white'
def press2(event):
    global Shift
    if Shift==0:
        label['text']+='2'
    else:
        label['text']+='@'
        Shift=0
        buttonShift['bg']='white'
def press3(event):
    global Shift
    if Shift==0:
        label['text']+='3'
    else:
        label['text']+='#'
        Shift=0
        buttonShift['bg']='white'
def press4(event):
    global Shift
    if Shift==0:
        label['text']+='4'
    else:
        label['text']+='$'
        Shift=0
        buttonShift['bg']='white'
def press5(event):
    global Shift
    if Shift==0:
        label['text']+='5'
    else:
        label['text']+='%'
        Shift=0
        buttonShift['bg']='white'
def press6(event):
    global Shift
    if Shift==0:
        label['text']+='6'
    else:
        label['text']+='^'
        Shift=0
        buttonShift['bg']='white'
def press7(event):
    global Shift
    if Shift==0:
        label['text']+='7'
    else:
        label['text']+='&'
        Shift=0
        buttonShift['bg']='white'
def press8(event):
    global Shift
    if Shift==0:
        label['text']+='8'
    else:
        label['text']+='*'
        Shift=0
        buttonShift['bg']='white'
def press9(event):
    global Shift
    if Shift==0:
        label['text']+='9'
    else:
        label['text']+='('
        Shift=0
        buttonShift['bg']='white'

def pressSign(event):
    label['text']+='`'
def pressMinus(event):
    global Shift
    if Shift==0:
        label['text']+='-'
    else:
        label['text']+='_'
        Shift=0
        buttonShift['bg']='white'
def pressDot(event):
    global Shift
    if Shift==0:
        label['text']+='.'
    else:
        label['text']+='>'
        Shift=0
        buttonShift['bg']='white'
def pressComa(event):
    global Shift
    if Shift==0:
        label['text']+=','
    else:
        label['text']+='<'
        Shift=0
        buttonShift['bg']='white'
def pressEqual(event):
    global Shift
    if Shift==0:
        label['text']+='='
    else:
        label['text']+='+'
        Shift=0
        buttonShift['bg']='white'
def pressSlash(event):
    global Shift
    if Shift==0:
        label['text']+='\\'
    else:
        label['text']+='|'
        Shift=0
        buttonShift['bg']='white'
def pressSlash2(event):
    global Shift
    if Shift==0:
        label['text']+='/'
    else:
        label['text']+='?'
        Shift=0
        buttonShift['bg']='white'
def pressBraces1(event):
    global Shift
    if Shift==0:
        label['text']+='['
    else:
        label['text']+='{'
        Shift=0
        buttonShift['bg']='white'
def pressBraces2(event):
    global Shift
    if Shift==0:
        label['text']+=']'
    else:
        label['text']+='}'
        Shift=0
        buttonShift['bg']='white'
def pressSign2(event):
    global Shift
    if Shift==0:
        label['text']+=';'
    else:
        label['text']+=':'
        Shift=0
        buttonShift['bg']='white'
def pressSign3(event):
    global Shift
    if Shift==0:
        label['text']+="'"
    else:
        label['text']+='"'
        Shift=0
        buttonShift['bg']='white'
def pressGmail(event):
    label['text']+='@gmail'
def pressCom(event):
    label['text']+='.com'

def pressReset(event):
    label2['text']=''
    label['text']=''
def pressDelete(event):
    label['text']=''
def pressSpace(event):
    label['text']+=' '
def pressBackspace(event):
    new=''
    for i in range(len(label['text'])-1):
        new+=label['text'][i]
    label['text']=new
def pressSave(event):
    label2['text']+=f"\n{label['text']}"
def pressEnter(event):
    label['text']+='\n'
def pressCopy(event):
    with open('keyboard.txt', 'w+') as file_holder:
        file=file_holder.write(label2['text'])
    label2['text']=''

buttonA.bind('<Button-1>', pressA)
buttonB.bind('<Button-1>', pressB)
buttonC.bind('<Button-1>', pressC)
buttonD.bind('<Button-1>', pressD)
buttonE.bind('<Button-1>', pressE)
buttonF.bind('<Button-1>', pressF)
buttonG.bind('<Button-1>', pressG)
buttonH.bind('<Button-1>', pressH)
buttonI.bind('<Button-1>', pressI)
buttonJ.bind('<Button-1>', pressG)
buttonK.bind('<Button-1>', pressK)
buttonL.bind('<Button-1>', pressL)
buttonM.bind('<Button-1>', pressM)
buttonN.bind('<Button-1>', pressN)
buttonO.bind('<Button-1>', pressO)
buttonP.bind('<Button-1>', pressP)
buttonQ.bind('<Button-1>', pressQ)
buttonR.bind('<Button-1>', pressR)
buttonS.bind('<Button-1>', pressS)
buttonT.bind('<Button-1>', pressT)
buttonU.bind('<Button-1>', pressU)
buttonV.bind('<Button-1>', pressV)
buttonW.bind('<Button-1>', pressW)
buttonX.bind('<Button-1>', pressX)
buttonY.bind('<Button-1>', pressY)
buttonZ.bind('<Button-1>', pressZ)

button0.bind('<Button-1>', press0)
button1.bind('<Button-1>', press1)
button2.bind('<Button-1>', press2)
button3.bind('<Button-1>', press3)
button4.bind('<Button-1>', press4)
button5.bind('<Button-1>', press5)
button6.bind('<Button-1>', press6)
button7.bind('<Button-1>', press7)
button8.bind('<Button-1>', press8)
button9.bind('<Button-1>', press9)

buttonSign.bind('<Button-1>', pressSign)
buttonMinus.bind('<Button-1>', pressMinus)
buttonEqual.bind('<Button-1>', pressEqual)
buttonDot.bind('<Button-1>', pressDot)
buttonComa.bind('<Button-1>', pressComa)
buttonSlash.bind('<Button-1>', pressSlash)
buttonSlash2.bind('<Button-1>', pressSlash2)
buttonBraces1.bind('<Button-1>', pressBraces1)
buttonBraces2.bind('<Button-1>', pressBraces2)
buttonSign2.bind('<Button-1>', pressSign2)
buttonSign3.bind('<Button-1>', pressSign3)
buttonSpace.bind('<Button-1>', pressSpace)
buttonGmail.bind('<Button-1>', pressGmail)
buttonCom.bind('<Button-1>', pressCom)
buttonBackspace.bind('<Button-1>', pressBackspace)

buttonDELETE.bind('<Button-1>',pressDelete)
buttonSave.bind('<Button-1>', pressSave)
buttonReset.bind('<Button-1>', pressReset)
buttonEnter.bind('<Button-1>',pressEnter)
buttonCaps.bind('<Button-1>', pressCaps)
buttonShift.bind('<Button-1>', pressShift)
buttonCopy.bind('<Button-1>', pressCopy)

root.mainloop()


# In[27]:


import tkinter as tk

top = tk.Tk()
top.title("On Screen Keyboard")

def click(key):
    if key == "<-":
        s = entry.get()
        entry.delete(len(s) - 1, tk.END)
    elif key == " Space ":
        entry.insert(tk.END, ' ')
    else:
        entry.insert(tk.END,key)

button_list = [
'q','w','e','r','t','y','u','i','o','p','<-',
'a','s','d','f','g','h','j','k','l',
'z','x','c','v','b','n','m'
,' Space '
]

entry = tk.Entry(top, width = 84)
entry.grid(row = 1, columnspan = 15)

r = 2
c = 0
for b in button_list:
    rel = 'groove'
    command = lambda x=b: click(x)
    if b != " Space ":
        tk.Button(top, text = b, width = 5, relief = rel, command = command).grid(row = r, column = c)
    if b == " Space ":
        tk.Button(top, text = b, width = 30, relief = rel, command = command).grid(row = 5, columnspan = 10)
    c+=1
    if c > 10 and r == 2:
        c = 0
        r+=1
    if c > 8 and r == 3:
        c = 0
        r+=1
    
top.mainloop()


# In[ ]:





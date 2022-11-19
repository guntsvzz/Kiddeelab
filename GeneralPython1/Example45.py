from tkinter import *

window = Tk()
window.title('Example44')
window.geometry('500x500')
window.resizable(False,False) #width,height

f1 = Frame(window,width=100,height=100,bg='white')
f1.grid(row=0,column=0)
f2 = Frame(window,width=100,height=100,bg='black')
f2.grid(row=0,column=1)
f3 = Frame(window,width=100,height=100,bg='white')
f3.grid(row=0,column=2)
f4 = Frame(window,width=100,height=100,bg='black')
f4.grid(row=0,column=3)
f5 = Frame(window,width=100,height=100,bg='white')
f5.grid(row=0,column=4)

A = Label(f1,text = 'A',bg='white',fg = 'red',font = (None,40))
A.place(x=50,y=50,anchor='n')
B = Label(f2,text = 'B',bg='black',fg = 'red',font = (None,40))
B.place(x=50,y=50,anchor='e')
C = Label(f3,text = 'C',bg='white',fg = 'red',font = (None,40))
C.place(x=50,y=50,anchor='w')
D = Label(f4,text = 'D',bg='black',fg = 'red',font = (None,40))
D.place(x=50,y=50,anchor='s')
E = Label(f5,text = 'E',bg='white',fg = 'red',font = (None,40))
E.place(x=50,y=50,anchor='c')

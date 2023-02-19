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

f6 = Frame(window,width=100,height=100,bg='black')
f6.grid(row=1,column=0)
f7 = Frame(window,width=100,height=100,bg='white')
f7.grid(row=1,column=1)
f8 = Frame(window,width=100,height=100,bg='black')
f8.grid(row=1,column=2)
f9 = Frame(window,width=100,height=100,bg='white')
f9.grid(row=1,column=3)
f10 = Frame(window,width=100,height=100,bg='black')
f10.grid(row=1,column=4)

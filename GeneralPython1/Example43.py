from tkinter import *

window = Tk()
window.title('Example43')
window.geometry('500x300')
window.resizable(False,False) #width,height

f1 = Frame(window,width=500,height=100,bg='red')
f1.pack(side = RIGHT)
f2 = Frame(window,width=50,height=100,bg='yellow')
f2.pack(side = RIGHT)
f3 = Frame(window,width=500,height=100,bg='blue')
f3.pack(side = RIGHT)
#pack place grid


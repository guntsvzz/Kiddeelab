from tkinter import *
window = Tk()
window.title('Test21')
window.geometry('800x400')
window.resizable(False,False) #width,height
#Frame
f1 = Frame(window,width=400,height=200,bg='orange')
f1.grid(row=0,colaumn=0)
f2 = Frame(window,width=400,height=200,bg='purple')
f2.grid(row=0,column=1)
f3 = Frame(window,width=400,height=200,bg='blue')
f3.grid(row=1,column=0)
f4 = Frame(window,width=400,height=200,bg='green')
f4.grid(row=1,column=1)
#Label
lb1 = Label(f1,text='Python',bg='orange',font=(None,40))
lb1.place(x=200,y=100,anchor='c')
lb2 = Label(f2,text='Tkinter',bg='purple',font=(None,40))
lb2.place(x=200,y=100,anchor='c')
lb3 = Label(f3,text='By',bg='blue',font=(None,40))
lb3.place(x=200,y=100,anchor='c')
lb4 = Label(f4,text='KiddeeLab',bg='green',font=(None,40))
lb4.place(x=200,y=100,anchor='c')

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('Example46')
window.geometry('500x300')
window.resizable(False,False) #width,height
def Box():
   messagebox.showinfo('Notification','You select '+str(var1.get())+str(var2.get()))
   messagebox.showwarning('Notification','Warning')
   messagebox.showerror('Notification','Error')
   
def Yes():
    window.destroy()
    print('Quit')
    
#Frame
f1 = Frame(window,width=500,height=100,bg='red')
f1.pack()
f2 = Frame(window,width=500,height=100,bg='yellow')
f2.pack()
f3 = Frame(window,width=500,height=100,bg='blue')
f3.pack()
#IntVar
var1 = IntVar()
var2 = IntVar()
#CheckButton
c1 = Checkbutton(f1,text='Apple',variable=var1,bg='red')
c1.place(x=200,y=50,anchor='c')
c2 = Checkbutton(f1,text='Orange',variable=var2,bg='red')
c2.place(x=300,y=50,anchor='c')
#Button
btn1 = Button(f2,text='Message',width=20,height=2,command=Box)
btn1.place(x=250,y=50,anchor='c')
btn2 = Button(f3,text='Confirm',width=20,height=2,command=Yes)
btn2.place(x=250,y=50,anchor='c')

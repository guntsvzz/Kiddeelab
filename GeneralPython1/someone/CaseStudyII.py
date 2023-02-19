from tkinter import *
from tkinter import messagebox
window = Tk()
window.title('CaseStudyII')
window.geometry('400x250')
window.resizable(False,False) #width,height
def result():
    total = [] #pay
    foodlist = [] #food name
    check = [var1.get(),var2.get(),var3.get(),var4.get()]
    price = [50,40,20,10]
    foodname = ['Chicken Rice','Pork Rice','Coke','Water']#var1 50 var2 40 var3 20 var4 10
    for i in range(len(check)):
        if check[i] == 1:
            total.append(price[i])
            foodlist.append(foodname[i])
    result_food = 5
    messagebox.showinfo('Summary','Total is {} Baht.\nThere are {}'.format(sum(total),foodlist))
        
#Frame
f1 = Frame(window,width=400,height=30,bg='tomato2')
f1.pack()
f2 = Frame(window,width=400,height=70,bg='snow2')
f2.pack()
f3 = Frame(window,width=400,height=30,bg='orange')
f3.pack()
f4 = Frame(window,width=400,height=120,bg='snow2')
f4.pack()
#Label
lb1 = Label(f1,text='Please select your food',fg='white',bg='tomato2',font=(None,20))
lb1.place(x=200,y=15,anchor='c')
lb3 = Label(f3,text='Please select your drink',fg='white',bg='orange',font=(None,20))
lb3.place(x=200,y=15,anchor='c')
#IntVar
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
#CheckButton
c1 = Checkbutton(f2,text='Chicken Rice 50',variable=var1,bg='snow2')
c1.place(x=200,y=20,anchor='c')
c2 = Checkbutton(f2,text='Pork Rice 40',variable=var2,bg='snow2')
c2.place(x=200,y=50,anchor='c')
c3 = Checkbutton(f4,text='Coke 20',variable=var3,bg='snow2')
c3.place(x=200,y=20,anchor='c')
c4 = Checkbutton(f4,text='Water 10',variable=var4,bg='snow2')
c4.place(x=200,y=50,anchor='c')
#Button
btn = Button(f4,text='Confirm',width=20,height=2,command = result)
btn.place(x=200,y=90,anchor='c')

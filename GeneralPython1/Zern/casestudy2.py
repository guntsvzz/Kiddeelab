from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Case Study2')
window.geometry('400x250')
window.resizable(False,False)
def confirm():
    food = ''
    price = 0
    menus = {
        'foods' : [' Pork Steak', ' Spaghetti', ' Soda', ' Mineral Water'], 
        'prices' : [250, 200, 30, 15]
    } 

    if v1.get() == 1:
        food  += menus['foods'][0]
        price += menus['prices'][0]
    if v2.get() == 1:
        food  += menus['foods'][1]
        price += menus['prices'][1]
    if v3.get() == 1:
        food  += menus['foods'][2]
        price += menus['prices'][2]
    if v4.get() == 1:
        food  += menus['foods'][3]
        price += menus['prices'][3]

    messagebox.showinfo('Receipt',f'There are : {food}\nTotal Price : {price}')

v1, v2, v3, v4 = IntVar(), IntVar(), IntVar(), IntVar()
####Frame
f1 = Frame(window, width= 400, height=30, bg='#eb6734')
f1.pack()
f2 = Frame(window, width= 400, height=70, bg='snow2')
f2.pack()
f3 = Frame(window, width= 400, height=30, bg='#eba834')
f3.pack()
f4 = Frame(window, width= 400, height=70, bg='snow2')
f4.pack()
f5 = Frame(window, width= 400, height=50, bg='snow2')
f5.pack()
####Label
l1 = Label(f1,text='Please select your food', bg='#eb6734',fg='white',font=(None,20))
l1.place(x=200,y=15,anchor = 'center')
l3 = Label(f3,text='Please select your drink', bg='#eba834',fg='white',font=(None,20))
l3.place(x=200,y=15,anchor = 'center')
####CheckButton
c2_1 = Checkbutton(f2, text='Pork Steak : 250 B', variable=v1)
c2_1.place(x=120,y=15,anchor='w')
c2_2 = Checkbutton(f2, text='Spaghetti : 200 B', variable=v2)
c2_2.place(x=120,y=45,anchor='w')
c4_1 = Checkbutton(f4, text='Soda : 30 B', variable=v3)
c4_1.place(x=120,y=15,anchor='w')
c4_2 = Checkbutton(f4, text='Mineral Water : 15 B', variable=v4)
c4_2.place(x=120,y=45,anchor='w')
####Button
bt = Button(f5, text='Confirm',bg='red2',fg='white',font=(None,15),command=confirm)
bt.pack()
window.mainloop()
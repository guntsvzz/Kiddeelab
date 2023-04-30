from tkinter import * 
from tkinter import messagebox

window = Tk()
window.geometry('400x200') #width x height
window.title('example 46')
window.resizable(False, False) #width, height

def remove():
    print('hello')
    window.destroy()
    
def remind(): 
    #Messagebox Widget
    messagebox.showinfo('Notification', f'I was clicked remind button {m.get()} and {f.get()}') #Title, Content
    #showinfo/showwarning/showerror
    # print(m.get())
    # print(f.get())

m = IntVar() #track variable state value of Checkbutton
f = IntVar() 
#CheckButton Widget
male = Checkbutton(window,text='male',variable=m)
male.place(x= 200, y=50,anchor = 'center')
female = Checkbutton(window,text='female',variable=f)
female.place(x= 200, y=70,anchor = 'center')
#Button Widget
bt1 = Button(window, text='remove', bg='red', fg='white', font= (None, 20), command= remove)
bt1.place(x=125, y=150, anchor='center')
bt2 = Button(window, text='remind', bg='red', fg='white', font= (None, 20), command= remind)
bt2.place(x=275, y=150, anchor='center')

window.mainloop()
from tkinter import * #classes, function, variable

window = Tk()
window.geometry('300x300') #width x height
window.title('example 44')
window.resizable(False, False) #width,height

####Frame
f1 = Frame(window, width = 100, height=100, bg='green2')
f1.grid(row = 0, column=0)
f2 = Frame(window, width = 100, height=100, bg='black')
f2.grid(row = 0, column=1)
f3 = Frame(window, width = 100, height=100, bg='green2')
f3.grid(row = 0, column=2)
f4 = Frame(window, width = 100, height=100, bg='black')
f4.grid(row = 1, column=0)
f5 = Frame(window, width = 100, height=100, bg='green2')
f5.grid(row = 1, column=1)
f6 = Frame(window, width = 100, height=100, bg='black')
f6.grid(row = 1, column=2)
f7 = Frame(window, width = 100, height=100, bg='green2')
f7.grid(row = 2, column=0)
f8 = Frame(window, width = 100, height=100, bg='black')
f8.grid(row = 2, column=1)
f9 = Frame(window, width = 100, height=100, bg='green2')
f9.grid(row = 2, column=2)
####LABEL
l1 = Label(f1, text = 'A', bg='green2', fg = 'red', font= (None, 30))
l1.place(x=50, y=50, anchor = CENTER)
l2 = Label(f2, text = 'B', bg='black', fg = 'white', font= (None, 30))
l2.place(x=50, y=50, anchor = CENTER)

window.mainloop()
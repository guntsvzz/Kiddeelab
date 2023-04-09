from tkinter import * #classes, function, variable

window = Tk()
window.geometry('400x200') #width x height
window.title('example 43')
window.resizable(False, False) #width,height

f1 = Frame(window, width = 400, height=100, bg='red')
f1.pack()
f1 = Frame(window, width = 400, height=100, bg='orange')
f1.pack()

window.mainloop()
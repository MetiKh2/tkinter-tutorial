from tkinter import *
master=Tk() #where m is the name of the main window object
master.title('Form')
top=Toplevel()
top.title('Python')
t=Text(master,height=2,width=30)
t.pack()
t.insert(END,'Hello Guys')

master.mainloop()
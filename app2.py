from tkinter import *
master=Tk() #where m is the name of the main window object
var1=IntVar()
Checkbutton(master,text='male',variable=var1).grid(row=0,sticky=W)
var2=IntVar()
Checkbutton(master,text='female',variable=var2).grid(row=1,sticky=W)
Label(master,text='FirstName').grid(row=2)
Label(master,text='LastName').grid(row=3)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=2,column=1)
e2.grid(row=3,column=1)
master.mainloop()
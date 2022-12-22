from tkinter import *
master=Tk() #where m is the name of the main window object

# w=Label(master,text='Hey Guys').pack()
# lb=Listbox(master)
# lb.insert(1,'python')
# lb.insert(2,'Java')
# lb.insert(3,'C++')
# lb.insert(4,'AnyOther')
# lb.pack()

mb=Menubutton(master,text='World')
mb.grid()
mb.menu=Menu(mb,tearoff=0)
mb['menu']=mb.menu
cVar=IntVar()
aVar=IntVar()
mb.menu.add_checkbutton(label='Contact',variable=cVar)
mb.menu.add_checkbutton(label='About',variable=aVar)
mb.pack()

master.mainloop()
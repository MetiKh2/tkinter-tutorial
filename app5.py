from tkinter import *
master=Tk() #where m is the name of the main window object

menu=Menu(master)
master.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open ...')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=master.destroy)
helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About')

our_message='This is our message'
message_var=Message(master,text=our_message)
message_var.config(bg='lightgreen')
message_var.pack()

v=IntVar()
Radiobutton(master,text='Boy',variable=v,value=1).pack(anchor=W)
Radiobutton(master,text='Girl',variable=v,value=2).pack(anchor=W)

w=Scale(master,from_=0,to=42)
w.pack()
w=Scale(master,from_=0,to=200,orient=HORIZONTAL)
w.pack()
master.mainloop()
from tkinter import *
master=Tk() #where m is the name of the main window object

scrollbar=Scrollbar(master)
scrollbar.pack(side=RIGHT,fill=Y)
mylist=Listbox(master,yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END,'This is line number'+str(line))
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)
master.mainloop()
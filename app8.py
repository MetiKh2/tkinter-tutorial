from tkinter import *
master=Tk() #where m is the name of the main window object
w=Spinbox(master,from_=0,to=10)
w.pack()
m1=PanedWindow()
m1.pack(fill=BOTH,expand=1)
left=Entry(m1,bd=5)
m1.add(left)
m2=PanedWindow(m1,orient=VERTICAL)
m1.add(m2)
top=Scale(m2,orient=HORIZONTAL)
m2.add(top)
master.mainloop()
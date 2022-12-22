from tkinter import *
master=Tk() #where m is the name of the main window object
frame=Frame(master)
frame.pack()
bottomfarme=Frame(master)
bottomfarme.pack(side=BOTTOM)
redbutton=Button(frame,text='Red',fg='red')
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text='Brown',fg='brown')
greenbutton.pack(side=LEFT)
bluebutton=Button(frame,text='Blue',fg='blue')
bluebutton.pack(side=LEFT)
blackbutton=Button(bottomfarme,text='Black',fg='black')
blackbutton.pack(side=BOTTOM)


master.mainloop()
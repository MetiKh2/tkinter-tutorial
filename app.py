import tkinter as tk
master=tk.Tk() #where m is the name of the main window object
master.title('Counting Seconds')
#widgets are added here
button=tk.Button(master,text='Stop',width=25,command=master.destroy)
button.pack()
w=tk.Canvas(master,width=40,height=60)
w.pack()
canvas_height=20
canvas_width=200
y=int(canvas_height/2)
w.create_line(0,y,canvas_width,y)
master.mainloop()
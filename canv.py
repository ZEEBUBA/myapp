import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import messagebox
from PIL import Image,ImageTk
app=tk.Tk()
app.geometry('400x400')

#can = tk.Canvas(app,bd=8,bg='blue',height=50,cursor='circle')
#can.pack()

#can = tk.Canvas(app,bd=8,bg='blue',cursor='dot',height=50)
#can.pack()

#can = tk.Canvas(app,bd=3,bg='blue',cursor='dot',height=50,relief='raised',)
#can.pack()

#can = tk.Canvas(app,bd=8,bg='blue',cursor='dot',height=50,scrollregion='s')
#can.pack()

can = tk.Canvas(app,bd=8,bg='white',cursor='circle')
coord = 10, 50, 240, 210
arc = can.create_arc(coord, start=0, extent=150, fill="blue")
line = can.create_line(10,10,200,200,fill='white')
can.pack()


can = tk.Canvas(app,bd=8,bg='blue',cursor='circle')
filename = ImageTk.PhotoImage(file = "weather icon.jpg")
image = can.create_image(50, 50, anchor='ne', image=filename)
can.pack()
app.mainloop()


import tkinter as tk
from PIL import Image,ImageTk

app = tk.Tk()
app.geometry('400x400')

imagefile = 'gui bg.jpg'
img = Image.open(imagefile)
img2 = ImageTk.PhotoImage(img)
label = tk.Label(app,image=img2)
label.place(width=400,height=400)

frame = tk.Frame(app,highlightbackground='blue',highlightthickness=2,highlightcolor='blue')
frame.place(x=40,y=40,width=200,height=40)
entry = tk.Entry(frame,font=('calibri',13),fg='black')
entry.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.7)

frame2 = tk.Frame(app,highlightbackground='blue',highlightthickness=2,highlightcolor='blue')
frame2.place(x=250,y=40,width=100,height=40)
button = tk.Button(frame2,text='Search',font=('calibri,12'))
button.place(relx=0.1,rely=0.1,relheight=0.7,relwidth=0.8)

frame3 = tk.Frame(app,highlightbackground='blue',highlightthickness=2,highlightcolor='blue')
frame3.place(x=40,y=100,width=310,height=200)
app.mainloop()
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
app=tk.Tk()
app.geometry('400x400')

imagefile = 'weather icon.jpg'
img = Image.open(imagefile)
img2 = ImageTk.PhotoImage(img)


but1 = tk.Checkbutton(app,activebackground='red')
but1.pack()

but2 = tk.Checkbutton(app,activeforeground='green')
but2.pack()

but3 = tk.Checkbutton(app,bg='blue')
but3.pack()

def check():
    messagebox.showinfo('check','next')

but4 = tk.Checkbutton(app,bd=6,command=check)
but4.pack()

but5 = tk.Checkbutton(app,cursor='circle',disabledforeground='pink',text='zainab',font='calibri',fg='black')
but5.pack()

but6 = tk.Checkbutton(app,highlightcolor='blue',text='fatima',font='calibri',underline=3)
but6.pack()

but7 = tk.Checkbutton(app,highlightbackground='red')
but7.pack()

#but8 = tk.Checkbutton(app,image=img2)
#but8.pack()

but9 = tk.Checkbutton(app,offvalue=2)
but9.pack()

but10 = tk.Checkbutton(app,onvalue=2)
but10.pack()

#but11 = tk.Checkbutton(app)
#but11.pack(side='left',padx=24,pady=12)

#but12 = tk.Checkbutton(app,relief='raised',selectcolor='red',width=5,height=5)
#but12.pack()

#but13 = tk.Checkbutton(app,text=('zainab\n','fatima\n','amina\n'),width=5,height=5)
#but13.pack()

but14 = tk.Checkbutton(app,state='disabled')
but14.pack()

but15 = tk.Checkbutton(app,text='zainab',wraplength=3)
but15.pack()



app.mainloop()


#height,Bitmap,Highlightcolor,justify,offvalue,onvalue,setimage,text,variable,width

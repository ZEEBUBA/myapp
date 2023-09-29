import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
app=tk.Tk()
app.geometry('400x400')

imagefile = 'weather icon.jpg'
img = Image.open(imagefile)
img2 = ImageTk.PhotoImage(img)


def button():
    print('you will make it')
    
def mine():
    print('wealthy lady')
    
    
but = tk.Button(app,activebackground='black',text='money')
but.pack(pady=20)

but2 = tk.Button(app,activeforeground='red',text='money')
but2.pack()
but3 = tk.Button(app,bd=5,text='money')
but3.pack()

but4 = tk.Button(app,bg='blue',text='money')
but4.pack()

but5 = tk.Button(app,fg='red',text='money',width=6,height=4,command=mine)
but5.pack()
  
but6 = tk.Button(app,fg='red',text='money',width=6,height=4,command=button)
but6.pack()
  
but7 = tk.Button(app,bg='white',text='money',font=('arial',12,'italic'))
but7.pack()  
  
but8 = tk.Button(app,text='money',highlightcolor='green')
but8.pack()

but9 = tk.Button(app,image=img2,width=6,height=8)
but9.pack()

but10 = tk.Button(app,bg='white',text='micheal', font=('arial',12,'italic'))
but10.pack(side='left', padx=25)

but11 = tk.Button(app,bg='white',text='money', font=('arial',12,'italic'),relief='sunken')
but11.pack()

but12 = tk.Button(app,bg='white',text='money', font=('arial',12,'italic'),relief='groove',state='disabled')
but12.pack()

but13 = tk.Button(app,bg='white', text='money', font=('arial', 12, 'underline'),relief='raised')
but13.pack()


def buttoniclick():

    messagebox.showinfo('buttonclick','my name is')


but14 = tk.Button(app,bg='white', text='money', font=('arial', 12, 'italic'),relief='raised',wraplength=1,command=buttoniclick)

but14.pack()


def buttonclick():
    messagebox.showinfo('buttonclick','click me')
    
def buttontoclick():
    but15.flash()  
       

but15 = tk.Button(app, bg='blue', text='money', font=('arial', 12, 'underline'), activebackground='black', command=buttonclick)
but15.pack(pady=10)

but16 = tk.Button(app,bg='blue', text='money', font=('arial', 12, 'underline'), activebackground='black', command=buttontoclick)
but16.pack(pady=25)

#def depart():
#    messagebox.showinfo('depart','cyber security')

#but17 = tk.Button(app,bg='red',text='department',command=depart)
#but17.pack()



app.mainloop()

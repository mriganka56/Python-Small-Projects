from tkinter import *
from tkinter.ttk import *
from time import strftime

w=Tk()
w.title("Digital-Clock")

def time():
    str=strftime('%H:%M:%S %p')
    label.config(text=str)
    label.after(1000, time)

label=Label(w,font=("ds-digital",80),background='black',foreground="cyan")
label.pack(anchor='center')
time()

mainloop()
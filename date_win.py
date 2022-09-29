#pip install tk-tools
from tkinter import *
import datetime

window = Tk()
window.title("main") 
window.minsize(width=400,height=400) 
lbl = Label(window, text="Сегодняшняя дата: ", font=("Arial Bold", 15))
lbl.grid(column=0, row=0)  
lbl = Label(window, text=datetime.date.today(), font=("Arial Bold", 15))
lbl.grid(column=3, row=0) 
window.mainloop()
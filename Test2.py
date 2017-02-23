import tkinter
from tkinter import ttk
tkwindow = tkinter.Tk()
chk = ttk.Checkbutton(tkwindow, text="foo")
chk.grid(column=0, row=0)
print(chk.state())
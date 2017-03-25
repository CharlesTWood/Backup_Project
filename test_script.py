from tkinter import *
from tkinter import ttk

main_window = Tk()
main_window.geometry('1000x700+300+100')
main_window.title('Test GUI')
canvas = Canvas(main_window, bg='gray58', width=1000, height=700)
text = Text(main_window, width=40, height=15, wrap='word')
text.grid(row=0, column=0)
scroll = ttk.Scrollbar(main_window, orient=VERTICAL, command=text.yview)
scroll.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand=scroll.set)
mainloop()

'''
canvas1 = Canvas(root, bg='white', width=300, height=300)

canvas1.create_line(0,0,300,300, dash=(4, 4,), width=50, fill='red')
canvas1.create_rectangle(0,0,200,200)
canvas1.create_oval(0,0,100,150)

#canvas.pack(side='top')


canvas = Canvas(root, bg='gray58', width=1000, height=700)

#canvas.create_rectangle(0,0,202,202, outline='black', width=8)
canvas.create_rectangle(20,400 ,600,680, fill='snow3', activefill='snow2', outline='SkyBlue')

#canvascoords = 12,50,240,240
#arc = canvas1.create_arc(canvascoords, start=30, extent=150, fill='blue')

canvas.pack()

mainloop()
'''
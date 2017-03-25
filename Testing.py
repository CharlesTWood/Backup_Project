from tkinter import *


class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='black'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)
        canv.config(scrollregion=(0, 0, 300, 1000))
        canv.config(highlightthickness=0)

        sbar = Scrollbar(self)
        sbar.config(command=canv.yview)
        canv.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        canv.pack(side=LEFT, expand=YES, fill=BOTH)

        for i in range(20):
            canv.create_text(200, (i * 100), text='AAA' + str(i), fill='white')
        self.canvas = canv


ScrolledCanvas().mainloop()









from tkinter import *
import time
root = Tk()
from functools import partial


def check_account(username, password):
    print("sdasdasd")
    if username == "admin":
        print('user works')
        if password == "password":
            print('Welcome')
            time.sleep(5)


label1 = Label(root, text="Name")
label2 = Label(root, text="Password")
entry1 = Entry(root)
entry2 = Entry(root)

#Holy Crap This is silly
function_for_check_for_account = partial(check_account, entry1, entry2)
button1 = Button(root, text="Login", command= function_for_check_for_account)
button1.grid(row=1, column=2)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

checkbox = Checkbutton(root, text="Keep me Logged in")
checkbox.grid(columnspan=2)
root.mainloop()
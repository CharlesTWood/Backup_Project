from tkinter import *
import tkinter
from tkinter import ttk
from datetime import datetime


def main():

    # Utilities
    red = StringVar()
    red.set('red')
    text = StringVar()
    user_accounts = ['']
    user_passwords = ['']
    admin_accounts = ['admin']
    admin_passwords = ['password']

    class backupManager:
        permissions = [0, 1]

        def __init__(self, username, permissions):
            self.username = username
            self.permissions = permissions

        def welcome(self):
            print('Welcome')
            root.destroy()

    def login():

        def check_account(logontime):

            if entrybox1.get() in user_accounts and entrybox2.get() in user_passwords:
                    for each_line in user_accounts:
                        print(each_line, 'logged in at:', logontime)
                    user = backupManager(entrybox1.get(), 0)
                    user.welcome()

            elif entrybox1.get() in admin_accounts and entrybox2.get() in admin_passwords:
                for each_line in admin_accounts:
                    print(each_line, 'logged in at:', logontime)
                user = backupManager(entrybox1.get(), 0)
                user.welcome()

            else:

                text.set('Login Failed')
                invalid_login = Label(root, textvariable=text, fg= red.get())
                invalid_login.grid(row=3, column=2)

        def create_user():

            def add_user():

                print('checkbox2 - UserButton', checkbox2.state())
                print('checkbox3 - AdminButton', checkbox3.state())

                if checkbox2.instate(['selected']):
                    if len(entrybox3.get()) >= 1 and len(entrybox4.get()) >= 6:
                        user_accounts.append(entrybox3.get())
                        # Prints latest added user in the admin accounts list
                        print('added user account', user_accounts[-1])

                elif checkbox3.instate(['selected']):
                    if len(entrybox3.get()) >= 1 and len(entrybox4.get()) >= 6:
                        admin_accounts.append(entrybox3.get())
                        # Prints latest added user in the admin accounts list
                        print('added admin user', admin_accounts[-1])
                '''
                elif not checkvar2 and not checkvar3:
                    print('ERROR: User did not select a checkbox for user type')
                    text.set('You must specify user Type')
                    user_type_error_message = Label(create_account_root, textvariable=text, fg=red.get())
                    user_type_error_message.grid(row=3, column=2)
                '''

            create_account_root = tkinter.Tk()

            label3 = Label(create_account_root, text="Username")
            label4 = Label(create_account_root, text="Password")

            button3 = Button(create_account_root, text="Create Account ", command=lambda: add_user())

            entry3 = StringVar()
            entrybox3 = Entry(create_account_root, textvariable=entry3)
            entry4 = StringVar()
            entrybox4 = Entry(create_account_root, textvariable=entry4)

            checkbox2 = ttk.Checkbutton(create_account_root, text="User")
            checkbox3 = ttk.Checkbutton(create_account_root, text="Admin")


            # Grid
            checkbox2.grid(row=3, column=0)
            checkbox3.grid(row=3, column=1)

            label3.grid(row=0, sticky=E)
            label4.grid(row=1, sticky=E)

            entrybox3.grid(row=0, column=1)
            entrybox4.grid(row=1, column=1)

            button3.grid(row=1, column=2)



        # Main GUI for login screen
        label1 = Label(root, text="Username")
        label2 = Label(root, text="Password")

        entry1 = StringVar()
        entrybox1 = Entry(root, textvariable=entry1)
        entry2 = StringVar()
        entrybox2 = Entry(root, textvariable=entry2)

        time = datetime.now()

        label1.grid(row=0, sticky=E)
        label2.grid(row=1, sticky=E)

        entrybox1.grid(row=0, column=1)
        entrybox2.grid(row=1, column=1)

        checkbox = Checkbutton(root, text="Keep me Logged in")
        checkbox.grid(columnspan=2)

        button1 = Button(root, text="Login", command=lambda: check_account(time))
        button1.grid(row=1, column=2)

        button2 = Button(root, text="Create Account", command=create_user)
        button2.grid(row=0, column=2)

        root.mainloop()
    login()

root = Tk()
main()
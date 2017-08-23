from tkinter import *
import tkinter
from tkinter import ttk, Canvas, Frame, BOTH
from datetime import datetime


def main():

    # Utilities
    red = StringVar()
    text = StringVar()
    user_accounts = ['user']
    user_passwords = ['password']
    admin_accounts = ['']
    admin_passwords = ['']

    class backupManager:
        permissions = [0, 1]

        def __init__(self, username, permissions):
            self.username = username
            self.permissions = permissions

        def welcome(self):
            print('Welcome')
            root.destroy()
            main_window = tkinter.Tk()
            canvas = Canvas(main_window, width=200, height=100)
            canvas.pack()


    def login():

        def check_account(logontime):

            if entrybox_username.get() in user_accounts and entrybox_password.get() in user_passwords:
                    for each_line in user_accounts:
                        print(each_line, 'logged in at:', logontime)
                    user = backupManager(entrybox_username.get(), 0)
                    user.welcome()

            elif entrybox_username.get() in admin_accounts and entrybox_password.get() in admin_passwords:
                for each_line in admin_accounts:
                    print(each_line, 'logged in at:', logontime)
                user = backupManager(entrybox_username.get(), 0)
                user.welcome()

            else:
                text.set('Login Failed')
                red.set('red')
                invalid_login = Label(root, textvariable=text, fg=red.get())
                invalid_login.grid(row=3, column=2)

        def create_user():

            def add_user():

                print('checkbox2 - UserButton', checkbox2.state())
                print('checkbox3 - AdminButton', checkbox3.state())

                if checkbox2.instate(['selected']):
                    if len(entrybox_Create_account_root.get()) >= 1 and len(entrybox_Create_account_root_password.get()) >= 6:
                        user_accounts.append(entrybox_Create_account_root.get())
                        print('added user account:', user_accounts[-1])
                        create_account_root.destroy()

                elif checkbox3.instate(['selected']):
                    if len(entrybox_Create_account_root.get()) >= 1 and len(entrybox_Create_account_root_password.get()) >= 6:
                        admin_accounts.append(entrybox_Create_account_root.get())
                        print('added admin user:', admin_accounts[-1])
                        create_account_root.destroy()

                else:
                    print('ERROR: User did not select a checkbox for user type')
                    user_type_error_message = Label(create_account_root, text="You must specify user Type", fg="red")
                    user_type_error_message.grid(row=2, column=4)


            create_account_root = tkinter.Tk()

            label_Username = Label(create_account_root, text="Username")
            label_Password = Label(create_account_root, text="Password")

            entryvar_Create_account_root = StringVar()
            entrybox_Create_account_root = Entry(create_account_root, textvariable=entryvar_Create_account_root)
            entryvar_Create_account_root_password = StringVar()
            entrybox_Create_account_root_password = Entry(create_account_root, textvariable=entryvar_Create_account_root_password)
            checkbox2 = ttk.Checkbutton(create_account_root, text="User")
            checkbox3 = ttk.Checkbutton(create_account_root, text="Admin")

            button_create_account = Button(create_account_root, text="Create Account ", command=lambda: add_user())

            # Grid
            checkbox2.grid(row=3, column=0)
            checkbox3.grid(row=3, column=1)

            label_Username.grid(row=0, sticky=E)
            label_Password.grid(row=1, sticky=E)

            entrybox_Create_account_root.grid(row=0, column=1)
            entrybox_Create_account_root_password.grid(row=1, column=1)

            button_create_account.grid(row=1, column=2)



        # Main GUI for login screen
        label_Username = Label(root, text="Username")
        label_Password = Label(root, text="Password")

        entryvar_username = StringVar()
        entrybox_username = Entry(root, textvariable=entryvar_username)
        entryvar_password = StringVar()
        entrybox_password = Entry(root, textvariable=entryvar_password)

        time = datetime.now()

        label_Username.grid(row=0, sticky=E)
        label_Password.grid(row=1, sticky=E)

        entrybox_username.grid(row=0, column=1)
        entrybox_password.grid(row=1, column=1)

        checkbox_keepmelogged = Checkbutton(root, text="Keep me Logged in")
        checkbox_keepmelogged.grid(columnspan=2)

        button_Login = Button(root, text="Login", command=lambda: check_account(time))
        button_Login.grid(row=1, column=2)

        button2 = Button(root, text="Create Account", command=create_user)
        button2.grid(row=0, column=2)

        root.mainloop()
    login()

root = Tk()
main()
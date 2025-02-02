from tkinter import *
import tkinter.messagebox


class PassUserWin:
    def __init__(self, master):
        master.title("My Program")
        self.label_pass = Label(master, text="Password:")
        self.entry_pass = Entry(master, show="*")
        self.button_enter = Button(master, text="Login", command=self.new_window)
        self.button_change = Button(master, text="Change Password", command=self.change_pass)
        self.label_pass.grid(row=1, sticky=E)
        self.entry_pass.grid(row=1, column=1)
        self.button_enter.grid(row=2, columnspan=2, pady=5)
        self.button_change.grid(row=3, columnspan=2, pady=5, padx=5)

    def change_pass(self):
        change = Toplevel(master=root)
        u = ChangePassUser(change)
        change.mainloop()

    def new_window(self):
        global master_pass
        self.password = self.entry_pass.get()
        if self.password == master_pass:
            new = Toplevel(master=root)
            w = Window(new)
            new.mainloop()
        else:
                tkinter.messagebox.showinfo(title="Error", message="Incorrect Password")


class ChangePassUser:
    def __init__(self, master):
        master.title("Change Password")
        self.org_pass = Label(master, text="Enter Original Password:").grid(row=1, column=0, sticky=E)
        self.org_pass_enter = Entry(master).grid(row=1, column=1)
        self.new_pass = Label(master, text="Enter New Password:").grid(row=2, column=0, sticky=E)
        self.new_pass_confirm = Label(master, text="Confirm New Password:").grid(sticky=E, row=3, column=0)
        self.new_pass_enter = Entry(master, show="*").grid(row=2, column=1)
        self.new_passConfirm_enter = Entry(master, show="*").grid(row=3, column=1, sticky=E)
        self.chg_button = Button(master, text="Apply", command=self.change).grid(row=4, columnspan=4)

    def change(self):
        global master_pass
        self.org_pass = self.org_pass_enter.get()
        if self.org_pass == master_pass:
            self.pass_new = self.new_pass_enter.get()
            self.confirm = self.new_pass_confirm.get()
            if self.pass_new == self.confirm:
                master_pass = self.pass_new
                tkinter.messagebox.showinfo(title="Success", message="Password and Username Changed!")
            else:
                tkinter.messagebox.showinfo(title="Error", message="Passwords do not match")
        else:
            tkinter.messagebox.showinfo(title="Error", message="Wrong original password")



class Window:
    def __init__(self, master):
        master.title("My Program")
        self.m = StringVar()
        self.label_1 = Label(master, text="My Program")
        self.button = Button(master, text="Print Message", command=self.message)
        self.label_2 = Label(master, textvariable=self.m)
        self.label_1.pack()
        self.button.pack()
        self.label_2.pack()

    def message(self):
        self.m.set("Hello World!")


master_pass = "Temp4Now"
root = Tk()
p = PassUserWin(root)
root.mainloop()

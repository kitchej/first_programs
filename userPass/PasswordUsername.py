from tkinter import *
import tkinter.messagebox


class ExampleProgram:
    def __init__(self, master):
        self.frame_main = Frame(master)
        self.frame_login = Frame(master)
        for frame in (self.frame_main, self.frame_login):
            frame.grid(row=0, column=0, sticky='news')
        master.title("My Program")
        self.message = StringVar()
        self.label_1 = Label(self.frame_main, text="My Program")
        self.button = Button(self.frame_main, text="Print Message", command=self.message_display)
        self.label_2 = Label(self.frame_main, textvariable=self.message)
        self.sec_q_button = Button(self.frame_main, text="Set security questions", command=self.set_security_qs)
        self.logout = Button(self.frame_main, text="Logout", command=self.logout)
        self.label_1.pack()
        self.button.pack()
        self.label_2.pack()
        self.sec_q_button.pack()
        self.logout.pack()
        # Login page
        self.label_username = Label(self.frame_login, text="Username:")
        self.entry_username = Entry(self.frame_login)
        self.label_pass = Label(self.frame_login, text="Password:")
        self.entry_pass = Entry(self.frame_login, show="*")
        self.button_login = Button(self.frame_login, text="Login", command=self.login)
        self.button_change_userpass = Button(self.frame_login, text="Change Username and Password",
                                                 command=self.change_userpass)
        self.reset_userpass_button = Button(self.frame_login, text="Reset Password", command=self.reset_win)
        self.label_username.grid(sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.label_pass.grid(row=1, sticky=E)
        self.entry_pass.grid(row=1, column=1)
        self.button_login.grid(row=2, columnspan=2, pady=1)
        self.reset_userpass_button.grid(row=3, columnspan=4)
        self.button_change_userpass.grid(row=4, columnspan=2, pady=1, padx=1)

    def change_userpass(self):
        self.sec_q_win = Toplevel(master=root)
        u = SecurityQuestions(self.sec_q_win)
        self.sec_q_win.mainloop()

    def login(self):
        global master_pass
        global master_username
        self.user_name = self.entry_username.get()
        self.password = self.entry_pass.get()
        if self.user_name == master_username:
            if self.password == master_pass:
                self.frame_main.tkraise()
            else:
                tkinter.messagebox.showerror(title="Error", message="Incorrect Password")
        else:
            tkinter.messagebox.showerror(title="Error", message="Incorrect Username")

    def message_display(self):
        self.message.set("Hello World!")

    def set_security_qs(self):
        self.sec_q_win = Toplevel(master=root)
        q = SecurityQuestionsReset(self.sec_q_win)
        self.sec_q_win.mainloop()

    def logout(self):
        self.answer = tkinter.messagebox.askquestion(title="Confirm Logout", message="Are you sure you want to logout?")
        if self.answer == "yes":
            self.frame_login.tkraise()

    def reset_win(self):
        self.reset_win = Toplevel(master=root)
        u = ResetWindow(self.reset_win)
        self.reset_win.mainloop()


class ChangePassUser:
    def __init__(self, master):
        master.title("Change Username and Password")
        self.new_user = Label(master, text="Enter New Username:")
        self.new_pass = Label(master, text="Enter New Password:")
        self.new_pass_enter = Entry(master, show="*")
        self.new_user_enter = Entry(master)
        self.chg_button = Button(master, text="Apply", command=self.change)
        self.new_user.grid(row=3, column=0, sticky=E)
        self.new_user_enter.grid(row=3, column=1)
        self.new_pass.grid(row=4, column=0, sticky=E)
        self.new_pass_enter.grid(row=4, column=1)
        self.chg_button.grid(row=5, columnspan=4)

    def change(self):
        global master_username
        global master_pass
        master_username = self.new_user_enter.get()
        master_pass = self.new_pass_enter.get()
        tkinter.messagebox.showinfo(title="Success", message="Password and Username Changed!")


class SecurityQuestions:
    def __init__(self, master):
        global sec_q1_master
        global sec_q2_master
        global sec_q1_ans_master
        global sec_q2_ans_master
        master.title("Security Questions")
        self.sec_q1 = Label(master, text=sec_q1_master)
        self.sec_q2 = Label(master, text=sec_q2_master)
        self.sec_q1_ans = Label(master, text="Answer: ")
        self.sec_q2_ans = Label(master, text="Answer: ")
        self.sec_q1_ans_entry = Entry(master)
        self.sec_q2_ans_entry = Entry(master)
        self.verify_sec_qs = Button(master, text="Verify", command=self.verify)
        self.sec_q1.grid(row=0, columnspan=4, pady=4)
        self.sec_q1_ans.grid(row=1, column=0, sticky=E)
        self.sec_q1_ans_entry.grid(row=1, column=1)
        self.sec_q2.grid(row=2, columnspan=4, pady=4)
        self.sec_q2_ans.grid(row=3, column=0, sticky=E)
        self.sec_q2_ans_entry.grid(row=3, column=1)
        self.verify_sec_qs.grid(row=4, columnspan=4, pady=4)

    def verify(self):
        global sec_q1_ans_master
        global sec_q2_ans_master
        self.sec_q1_ans_verify = self.sec_q1_ans_entry.get()
        self.sec_q2_ans_verify = self.sec_q2_ans_entry.get()
        if self.sec_q1_ans_verify == sec_q1_ans_master:
            if self.sec_q2_ans_verify == sec_q2_ans_master:
                self.change = Toplevel(master=root)
                c = ChangePassUser(self.change)
                self.change.mainloop()

            else:
                tkinter.messagebox.showerror(title="Error", message="Wrong answer for security question 2")
        else:
            tkinter.messagebox.showerror(title="Error", message="Wrong answer for security question 1")


class SecurityQuestionsReset:
    def __init__(self, master):
        master.title("Reset Security Questions")
        self.frame_sec_q = Frame(master)
        self.frame_login = Frame(master)
        for frame in (self.frame_login, self.frame_sec_q):
            frame.grid(row=0, column=0, sticky='news')
        # Login page
        self.label_username = Label(self.frame_login, text="Username:")
        self.entry_username = Entry(self.frame_login)
        self.label_pass = Label(self.frame_login, text="Password:")
        self.entry_pass = Entry(self.frame_login, show="*")
        self.button_login = Button(self.frame_login, text="Login", command=self.login)
        self.label_username.grid(sticky=E)
        self.entry_username.grid(row=0, column=1)
        self.label_pass.grid(row=1, sticky=E)
        self.entry_pass.grid(row=1, column=1)
        self.button_login.grid(row=2, columnspan=2, pady=1)
        #Securty Questions Reset Window
        self.sec_q1 = Label(self.frame_sec_q, text="Security question 1: ")
        self.sec_q2 = Label(self.frame_sec_q, text="Security question 2: ")
        self.sec_q1_entry = Entry(self.frame_sec_q)
        self.sec_q2_entry = Entry(self.frame_sec_q)
        self.sec_q1_ans = Label(self.frame_sec_q, text="Answer to question 1: ")
        self.sec_q2_ans = Label(self.frame_sec_q, text="Answer to question 2: ")
        self.sec_q1_ans_entry = Entry(self.frame_sec_q)
        self.sec_q2_ans_entry = Entry(self.frame_sec_q)
        self.set_sec_qs = Button(self.frame_sec_q, text="Set", command=self.reset_questions)
        self.sec_q1.grid(row=0, column=0, sticky=E)
        self.sec_q1_entry.grid(row=0, column=1)
        self.sec_q1_ans.grid(row=1, column=0)
        self.sec_q1_ans_entry.grid(row=1, column=1)
        self.sec_q2.grid(row=2, column=0,  sticky=E)
        self.sec_q2_entry.grid(row=2, column=1)
        self.sec_q2_ans.grid(row=3, column=0)
        self.sec_q2_ans_entry.grid(row=3, column=1)
        self.set_sec_qs.grid(row=4, columnspan=4)

    def login(self):
        global master_pass
        global master_username
        self.user_name = self.entry_username.get()
        self.password = self.entry_pass.get()
        if self.user_name == master_username:
            if self.password == master_pass:
                self.frame_sec_q.tkraise()
            else:
                tkinter.messagebox.showerror(title="Error", message="Incorrect Password")
        else:
            tkinter.messagebox.showerror(title="Error", message="Incorrect Username")

    def reset_questions(self):
        global sec_q1_master
        global sec_q2_master
        global sec_q1_ans_master
        global sec_q2_ans_master
        sec_q1_master = self.sec_q1_entry.get()
        sec_q1_ans_master = self.sec_q1_ans_entry.get()
        sec_q2_master = self.sec_q2_entry.get()
        sec_q2_ans_master = self.sec_q2_ans_entry.get()
        tkinter.messagebox.showinfo(title="Success", message="Security questions set!")


class ResetWindow:
    def __init__(self, master):
        master.title("Security Questions")
        self.sec_q1 = Label(master, text=sec_q1_master)
        self.sec_q2 = Label(master, text=sec_q2_master)
        self.sec_q1_ans = Label(master, text="Answer: ")
        self.sec_q2_ans = Label(master, text="Answer: ")
        self.sec_q1_ans_entry = Entry(master)
        self.sec_q2_ans_entry = Entry(master)
        self.verify_sec_qs = Button(master, text="Reset", command=self.reset)
        self.sec_q1.grid(row=0, columnspan=4, pady=4)
        self.sec_q1_ans.grid(row=1, column=0, sticky=E)
        self.sec_q1_ans_entry.grid(row=1, column=1)
        self.sec_q2.grid(row=2, columnspan=4, pady=4)
        self.sec_q2_ans.grid(row=3, column=0, sticky=E)
        self.sec_q2_ans_entry.grid(row=3, column=1)
        self.verify_sec_qs.grid(row=4, columnspan=4, pady=4)

    def reset(self):
        global master_username
        global master_pass
        self.answer = tkinter.messagebox.askquestion(title="Confirm",
                                                     message="Are you sure you want to reset your username and password to their default values")
        if self.answer == "yes":
            master_username = "User1"
            master_pass = "Password"


master_username = "User1"
master_pass = "Password"
sec_q1_master = ""
sec_q2_master = ""
sec_q1_ans_master = ""
sec_q2_ans_master = ""
root = Tk()
e = ExampleProgram(root)
root.mainloop()

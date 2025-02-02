from tkinter import *
from tkinter.ttk import *
import smtplib
import secrets


username = "User1"
password = "password"


class UserPassWin:
    global username
    global password

    def __init__(self, master):
        self.master = master
        self.paddingx = 5
        self.paddingy = 5
        self.login_err = StringVar()
        self.login_err.set("")
        self.user_label = Label(self.master, text="Username: ")
        self.pass_label = Label(self.master, text="Password: ")
        self.user_entry = Entry(self.master)
        self.pass_entry = Entry(self.master, show="*")
        self.login_error_label = Label(self.master, textvariable=self.login_err)
        self.login_button = Button(self.master, text="Login", command=self.login)
        self.forgot_button = Button(self.master, text="Forgot Password", command=self.forgot_pass)

        self.user_label.grid(row=0, column=0, padx=self.paddingx, pady=self.paddingy)
        self.pass_label.grid(row=1, column=0, padx=self.paddingx, pady=self.paddingy)
        self.user_entry.grid(row=0, column=1, padx=self.paddingx, pady=self.paddingy)
        self.pass_entry.grid(row=1, column=1, padx=self.paddingx, pady=self.paddingy)
        self.login_error_label.grid(row=2, column=1)
        self.forgot_button.grid(row=3, column=0, padx=self.paddingx, pady=self.paddingy)
        self.login_button.grid(row=3, column=1, padx=self.paddingx, pady=self.paddingy)

    def login(self):
        username_entry = self.user_entry.get()
        password_entry = self.pass_entry.get()
        if username_entry == username:
            if password_entry == password:
                main_win_frame.tkraise()
                self.login_err.set("")
            else:
                self.login_err.set("Wrong Password")
        else:
            self.login_err.set("Wrong Username")

    @staticmethod
    def forgot_pass():
        forgot_pass_frame.tkraise()


class ForgotPassWin:
    def __init__(self, master):
        self.master = master
        self.paddingx = 5
        self.paddingy = 5
        self.reg_emails = [['smtp.gmail.com', 'bnkitchen34@gmail.com']]
        self.confirm_code = None

        self.forgotPassErr = StringVar()
        self.forgotPassErr.set("")
        self.enter_email_label = Label(self.master, text="Enter Email: ")
        self.email_entry = Entry(self.master)
        self.error_display = Label(self.master, textvariable=self.forgotPassErr)
        self.send_email_button = Button(self.master, text="Send", command=self.send_confirm_code)

        self.code_enter_label = Label(self.master, text="Enter Code: ")
        self.code_enter = Entry(self.master)
        self.verify_button = Button(self.master, text="Verify", command=self.verify)

        self.enter_email_label.grid(row=0, column=0, padx=self.paddingx, pady=self.paddingy)
        self.email_entry.grid(row=0, column=1, padx=self.paddingx, pady=self.paddingy)
        self.error_display.grid(row=1, column=1, padx=self.paddingx, pady=self.paddingy)
        self.send_email_button.grid(row=2, column=1, padx=self.paddingx, pady=self.paddingy)

    @staticmethod
    def generate_code():
        return secrets.choice(range(10000, 100000))

    def send_confirm_code(self):
        recipient = self.email_entry.get()
        self.confirm_code = self.generate_code()
        for email in self.reg_emails:
            if recipient in email:
                service = email[0]
                self.code_enter_label.grid(row=3, column=0, padx=self.paddingx, pady=self.paddingy)
                self.code_enter.grid(row=3, column=1, padx=self.paddingx, pady=self.paddingy)
                self.verify_button.grid(row=4, column=1, padx=self.paddingx, pady=self.paddingy)
            else:
                self.forgotPassErr.set("That email is not registered")
                return
        with smtplib.SMTP(service, 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login('itsyaboiekitch85@gmail.com', '')

            subject = 'Verify'
            body = f"Your security code is: {self.confirm_code}"
            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail('itsyaboiekitch85@gmail.com', recipient, msg)

    def verify(self):
        entered_code = self.code_enter.get()
        if int(entered_code) == self.confirm_code:
            print("Worked")
        else:
            print("did not work")


class MainWin:
    def __init__(self, master):
        self.master = master
        self.label = Label(self.master, text="This is the main program")
        self.logout = Button(self.master, text="Logout", command=self.logout)

        self.label.pack()
        self.logout.pack()

    @staticmethod
    def logout():
        user_pass_frame.tkraise()
        user_pass_win.user_entry.delete(0, END)
        user_pass_win.pass_entry.delete(0, END)


root = Tk()

main_win_frame = Frame(root)
user_pass_frame = Frame(root)
forgot_pass_frame = Frame(root)

for frame in (main_win_frame, user_pass_frame, forgot_pass_frame):
    frame.grid(row=0, column=0, sticky='nesw')

user_pass_win = UserPassWin(user_pass_frame)
main_win_win = MainWin(main_win_frame)
forgot_pass_win = ForgotPassWin(forgot_pass_frame)

user_pass_frame.tkraise()

root.mainloop()

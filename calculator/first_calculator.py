from tkinter import *
import tkinter.messagebox


def multiply():
    try:
        answer = float(entry_1.get()) * float(entry_2.get())
        tkinter.messagebox.showinfo("Answer", answer)
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Invalid input")


def divide():
    try:
        answer = float(entry_1.get()) / float(entry_2.get())
        tkinter.messagebox.showinfo("Answer", answer)
    except ZeroDivisionError:
        tkinter.messagebox.showinfo("Error", "Cannot divide by zero!")
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Invalid input")


def add():
    try:
        answer = float(entry_1.get()) + float(entry_2.get())
        tkinter.messagebox.showinfo("Answer", answer)
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Invalid input")


def subtract():
    try:
        answer = float(entry_1.get()) - float(entry_2.get())
        tkinter.messagebox.showinfo("Answer", answer)
    except ValueError:
        tkinter.messagebox.showinfo("Error", "Invalid input")


root = Tk()
root.title("Calculator")

# WIDGETS


label_1 = Label(root, text="Calculator")
multi = Button(root, text="*", command=multiply)
div = Button(root, text="/", command=divide)
adding = Button(root, text="+", command=add)
sub = Button(root, text=" - ", command=subtract)
entry_1 = Entry(root)
entry_2 = Entry(root)
label_2 = Label(text="Num 1:")
label_3 = Label(text="Num 2: ")


# GUI layout

label_2.grid(row=1)
label_3.grid(row=2)
entry_1.grid(row=1, column=1, padx=25)
entry_2.grid(row=2, column=1,padx=25)
adding.grid(row=3, column=0, sticky=W, padx=2)
sub.grid(row=4, column=0, sticky=W)
multi.grid(row=3, column=1, sticky=W, padx=2)
div.grid(row=4, column=1, sticky=W, padx=2)

root.mainloop()

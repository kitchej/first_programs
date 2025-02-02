"""
------------------------------------
Calculator Version 3.0
Created by Joshua Kitchen
Spring 2019, modified February 2020
------------------------------------
"""
from tkinter import *
import tkinter.messagebox
from tkinter import colorchooser
from tkinter.ttk import *
import math


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal_press(event=None):
    global expression
    try:
        total = eval(entry_box.get())
        equation.set(total)
        expression = ""
    except ZeroDivisionError:
        equation.set("Error")
        expression = ""
    except ValueError:
        equation.set("Error")
        expression = ""
    except SyntaxError:
        equation.set("Error")
        expression = ""
    except NameError:
        equation.set("Error")
        expression = ""


def square_root():
    global expression
    try:
        total = math.sqrt(float(entry_box.get()))
        equation.set(round(total, 4))
        expression = ""
    except ValueError:
        equation.set("Error")
        expression = ""


def square():
    global expression
    try:
        total = (float(entry_box.get()) ** 2)
        equation.set(total)
        expression = ""
    except ValueError:
        equation.set("Error")
        expression = ""


def clear(event=None):
    global expression
    expression = ""
    equation.set("")


def change_color(color):
    root.configure(background=color)

def custom_color():
    color = colorchooser.askcolor()
    root.configure(background=color[1])

def open_help():
    tkinter.messagebox.showinfo("Help", "\"Enter\" --> evaluate entered function\n\"Delete\" --> clear entry box")


def open_about():
    tkinter.messagebox.showinfo("About", "Created by Joshua Kitchen. \nOriginal: Spring 2019. Updated February 2020 ")


root = Tk()
root.title("Calculator 3.0")
icon = PhotoImage(file=r"calculator_icon.png")
root.iconphoto(False, icon)
expression = ""
equation = StringVar()
menu = Menu(root)
root.config(menu=menu)
color_menu = Menu(menu, tearoff=0)
help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="Color", menu=color_menu)
color_menu.add_command(label="Blue", command=lambda: change_color("#000072"))
color_menu.add_command(label="Red", command=lambda: change_color("#CC0000"))
color_menu.add_command(label="Green", command=lambda: change_color("#008000"))
color_menu.add_command(label="Purple", command=lambda: change_color("#3D195D"))
color_menu.add_command(label="Yellow", command=lambda: change_color("#EBEF00"))
color_menu.add_command(label="Black", command=lambda: change_color("black"))
color_menu.add_command(label="White", command=lambda: change_color("white"))
color_menu.add_command(label="Custom", command=custom_color)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Keyboard short-cuts", command=open_help)
help_menu.add_command(label="About", command=open_about)
entry_box = Entry(root, textvariable=equation)
root.bind("<Return>", equal_press)
root.bind("<Delete>", clear)
multiply = Button(root, text=" * ", command=lambda: press("*"))
div = Button(root, text=" / ", command=lambda: press("/"))
add = Button(root, text=" + ", command=lambda: press("+"))
sub = Button(root, text=" - ", command=lambda: press("-"))
zero = Button(root, text=" 0 ", command=lambda: press(0))
one = Button(root, text=" 1 ", command=lambda: press(1))
two = Button(root, text=" 2 ", command=lambda: press(2))
three = Button(root, text=" 3 ", command=lambda: press(3))
four = Button(root, text=" 4 ", command=lambda: press(4))
five = Button(root, text=" 5 ", command=lambda: press(5))
six = Button(root, text=" 6 ", command=lambda: press(6))
seven = Button(root, text=" 7 ", command=lambda: press(7))
eight = Button(root, text=" 8 ", command=lambda: press(8))
nine = Button(root, text=" 9 ", command=lambda: press(9))
equal = Button(root, text=" = ", command=equal_press)
clear = Button(root, text=" C ", command=clear)
sqrt = Button(root, text="√x", command=square_root)
r_par = Button(root, text=" ( ", command=lambda: press("("))
l_par = Button(root, text=" ) ", command=lambda: press(")"))
sq = Button(root, text=" ˣ² ", command=lambda: square())
dec = Button(root, text=" . ", command=lambda: press("."))
entry_box.grid(row=0, columnspan=6, pady=2)
add.grid(row=2, padx=2, pady=2)
sub.grid(row=2, column=1, padx=2, pady=2)
multiply.grid(row=2, column=2, padx=2, pady=2)
div.grid(row=2, column=3, padx=2, pady=2)
equal.grid(row=7, column=1, padx=2)
zero.grid(row=6, column=1, padx=2, pady=2)
one.grid(row=5, padx=2, pady=2)
two.grid(row=5, column=1, padx=2, pady=2)
three.grid(row=5, column=2, padx=2, pady=2)
four.grid(row=4, padx=2, pady=2)
five.grid(row=4, column=1, padx=2, pady=2)
six.grid(row=4, column=2, padx=2, pady=2)
seven.grid(row=3, padx=2, pady=2)
eight.grid(row=3, column=1, padx=2, pady=2)
nine.grid(row=3, column=2, padx=2, pady=2)
clear.grid(row=6, column=2, padx=2, pady=2)
sqrt.grid(row=5, column=3, padx=2, pady=2)
r_par.grid(row=3, column=3, padx=2, pady=2)
l_par.grid(row=4, column=3, padx=2, pady=2)
sq.grid(row=6, column=3, padx=2, pady=2)
dec.grid(row=6, column=0, padx=2, pady=2)

root.mainloop()

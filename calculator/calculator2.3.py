"""
------------------------------------
Calculator Version 2.3
Created by Joshua Kitchen
Spring 2019, modified September 2019
------------------------------------
"""
import tkinter as tk
import tkinter.messagebox
import math


class Calculator:
    def __init__(self, master):
        master.title("Calculator 2.3")
        self.expression = ""
        self.equation = tk.StringVar()
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        self.color_menu = tk.Menu(self.menu)
        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Color", menu=self.color_menu)
        self.color_menu.add_command(label="Blue", command=lambda: self.change_color("blue"))
        self.color_menu.add_command(label="Red", command=lambda: self.change_color("red"))
        self.color_menu.add_command(label="Green", command=lambda: self.change_color("green"))
        self.color_menu.add_command(label="Purple", command=lambda: self.change_color("purple"))
        self.color_menu.add_command(label="Orange", command=lambda: self.change_color("orange"))
        self.color_menu.add_command(label="Pink", command=lambda: self.change_color("pink"))
        self.color_menu.add_command(label="Black", command=lambda: self.change_color("black"))
        self.color_menu.add_command(label="White", command=lambda: self.change_color("white"))
        self.menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="Keyboard short-cuts", command=lambda: self.open_help())
        self.help_menu.add_command(label="About", command=lambda: self.open_about())
        self.entry_box = tk.Entry(master, textvariable=self.equation)
        master.bind("<Return>", self.equal_press)
        master.bind("<Delete>", self.clear)
        self.multiply = tk.Button(master, text=" * ", command=lambda: self.press("*"), height=1, width=5)
        self.div = tk.Button(master, text=" / ", command=lambda: self.press("/"), height=1, width=5)
        self.add = tk.Button(master, text=" + ", command=lambda: self.press("+"), height=1, width=5)
        self.sub = tk.Button(master, text=" - ", command=lambda: self.press("-"), height=1, width=5)
        self.zero = tk.Button(master, text=" 0 ", command=lambda: self.press(0), height=1, width=5)
        self.one = tk.Button(master, text=" 1 ", command=lambda: self.press(1), height=1, width=5)
        self.two = tk.Button(master, text=" 2 ", command=lambda: self.press(2), height=1, width=5)
        self.three = tk.Button(master, text=" 3 ", command=lambda: self.press(3), height=1, width=5)
        self.four = tk.Button(master, text=" 4 ", command=lambda: self.press(4), height=1, width=5)
        self.five = tk.Button(master, text=" 5 ", command=lambda: self.press(5), height=1, width=5)
        self.six = tk.Button(master, text=" 6 ", command=lambda: self.press(6), height=1, width=5)
        self.seven = tk.Button(master, text=" 7 ", command=lambda: self.press(7), height=1, width=5)
        self.eight = tk.Button(master, text=" 8 ", command=lambda: self.press(8), height=1, width=5)
        self.nine = tk.Button(master, text=" 9 ", command=lambda: self.press(9), height=1, width=5)
        self.equal = tk.Button(master, text=" = ", command=lambda: self.equal_press(), height=9, width=5)
        self.clear = tk.Button(master, text=" C ", command=self.clear, height=1, width=5)
        self.sqrt = tk.Button(master, text="√x", command=self.square_root, height=1, width=5)
        self.r_par = tk.Button(master, text=" ( ", command=lambda: self.press("("), height=1, width=5)
        self.l_par = tk.Button(master, text=" ) ", command=lambda: self.press(")"), height=1, width=5)
        self.sq = tk.Button(master, text=" ˣ² ", command=lambda: self.square(), height=1, width=5)
        self.dec = tk.Button(master, text=" . ", command=lambda: self.press("."), height=1, width=5)
        self.entry_box.grid(row=0, columnspan=6, pady=2)
        self.add.grid(row=2, padx=2, pady=2)
        self.sub.grid(row=2, column=1, padx=2, pady=2)
        self.multiply.grid(row=2, column=2, padx=2, pady=2)
        self.div.grid(row=2, column=3, padx=2, pady=2)
        self.equal.grid(row=1, rowspan=7, column=4, padx=2)
        self.zero.grid(row=6, column=1, padx=2, pady=2)
        self.one.grid(row=5, padx=2, pady=2)
        self.two.grid(row=5, column=1, padx=2, pady=2)
        self.three.grid(row=5, column=2, padx=2, pady=2)
        self.four.grid(row=4, padx=2, pady=2)
        self.five .grid(row=4, column=1, padx=2, pady=2)
        self.six.grid(row=4, column=2, padx=2, pady=2)
        self.seven.grid(row=3, padx=2, pady=2)
        self.eight.grid(row=3, column=1, padx=2, pady=2)
        self.nine.grid(row=3, column=2, padx=2, pady=2)
        self.clear.grid(row=6, column=2, padx=2, pady=2)
        self.sqrt.grid(row=5, column=3, padx=2, pady=2)
        self.r_par.grid(row=3, column=3, padx=2, pady=2)
        self.l_par.grid(row=4, column=3, padx=2, pady=2)
        self.sq.grid(row=6, column=3, padx=2, pady=2)
        self.dec.grid(row=6, column=0, padx=2, pady=2)

    def press(self, num):
        self.expression = self.expression + str(num)
        self.equation.set(self.expression)

    def equal_press(self, event=None):
        try:
            total = eval(self.entry_box.get())
            self.equation.set(total)
            self.expression = ""
        except ZeroDivisionError:
            self.equation.set("Error")
            self.expression = ""
        except ValueError:
            self.equation.set("Error")
            self.expression = ""
        except SyntaxError:
            self.equation.set("Error")
            self.expression = ""
        except NameError:
            self.equation.set("Error")
            self.expression = ""

    def square_root(self):
        try:
            total = math.sqrt(float(self.entry_box.get()))
            self.equation.set(round(total, 4))
            self.expression = ""
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def square(self):
        try:
            total = (float(self.entry_box.get()) ** 2)
            self.equation.set(total)
            self.expression = ""
        except ValueError:
            self.equation.set("Error")
            self.expression = ""

    def clear(self, event=None):
        self.expression = ""
        self.equation.set("")

    @staticmethod
    def change_color(color):
        root.configure(background=color)

    @staticmethod
    def open_help():
        tkinter.messagebox.showinfo("Help", "\"Enter\" --> evaluate entered function\n\"Delete\" --> clear entry box")

    @staticmethod
    def open_about():
        tkinter.messagebox.showinfo("About", "Created by Joshua Kitchen, Spring 2019. Modified September 2019 "
                                             "\n\nA basic calculator created for practice (and for fun).")


root = tk.Tk()
c = Calculator(root)
root.mainloop()

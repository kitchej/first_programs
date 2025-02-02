import os
import subprocess as sp
import random
import tkinter as tk
from tkinter import filedialog


def open_dir():
    global path
    root.directory = filedialog.askdirectory(initialdir='')
    path.set(root.directory)


def get_random_pic(_dir):
    global path
    pics = os.listdir(_dir)
    random_pic = pics[random.randint(0, len(pics))]
    random_pic = os.path.join(path.get(), f"\"{random_pic}\"")
    sp.run([f"eog --new-instance {random_pic} "], shell=True, check=True)


root = tk.Tk()

path = tk.StringVar()

dir_entry = tk.Entry(root, textvariable=path)
choose_dir = tk.Button(root, text='Choose Dir', command=open_dir)
random_button = tk.Button(root, text="Random Picture", command=lambda: get_random_pic(dir_entry.get()))

dir_entry.pack()
choose_dir.pack()
random_button.pack()

root.mainloop()


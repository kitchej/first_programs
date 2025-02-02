from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import ImageTk, Image
import os


def open_dir():
    global path
    root.directory = filedialog.askdirectory()
    path.set(root.directory)


def view():
    global images
    global img
    global viewer_frame
    global image_counter
    global img_display
    global path_entry
    viewer_frame.tkraise()
    manual_path = path_entry.get()
    if manual_path:
        try:
            os.chdir(manual_path)
            images = os.listdir(os.getcwd())
        except AttributeError:
            pass
        except FileNotFoundError:
            pass
        except PermissionError:
            pass
        except OSError:
            pass
    else:
        try:
            os.chdir(root.directory)
            images = os.listdir(os.getcwd())
        except AttributeError:
            pass
    try:
        img = ImageTk.PhotoImage(Image.open(images[image_num]).resize((820, 540)))
    except OSError:
        pass
    except IndexError:
        pass
    img_display = Label(viewer_frame, image=img)
    img_display.grid(row=0, column=0, columnspan=3)
    image_counter.set(f'{image_num + 1}/{len(images)}')


def forward_img():
    global images
    global img
    global image_num
    global img_display
    global image_counter
    if image_num < len(images) - 1:
        image_num += 1
        img_display.grid_forget()
        try:
            img = ImageTk.PhotoImage(Image.open(images[image_num]).resize((820, 540)))
        except OSError:
            pass
        img_display = Label(viewer_frame, image=img)
        img_display.grid(row=0, column=0, columnspan=3)
        image_counter.set(f'{image_num + 1}/{len(images)}')
    else:
        pass


def back_img():
    global images
    global img
    global image_num
    global img_display
    global image_counter
    if image_num > 0:
        image_num -= 1
        img_display.grid_forget()
        try:
            img = ImageTk.PhotoImage(Image.open(images[image_num]).resize((820, 540)))
        except OSError:
            pass
        img_display = Label(viewer_frame, image=img)
        img_display.grid(row=0, column=0, columnspan=3)
        image_counter.set(f'{image_num + 1}/{len(images)}')
    else:
        pass


def path_screen():
    global path_frame
    global images
    global img
    global image_num
    images = []
    img = None
    image_num = 0
    path_frame.tkraise()


images = []
img = None
image_num = 0

root = Tk()
root.title('Image Viewer')
root.minsize(height=600, width=820)
path_frame = Frame(root)
viewer_frame = Frame(root)

for frame in (path_frame, viewer_frame):
    frame.grid(row=0, column=0, sticky='news')

# enter path screen
path_frame.tkraise()
path = StringVar()
white_space = Label(path_frame)
white_space2 = Label(path_frame)
white_space3 = Label(path_frame)
intro = Label(path_frame, text='Enter Path:')
path_entry = Entry(path_frame, textvariable=path)
file_manager = Button(path_frame, text='Open File Manager', command=open_dir)
view_button = Button(path_frame, text='View', command=view)
white_space.grid(row=0, column=0, padx=150)
white_space2.grid(row=1, column=0, padx=150)
white_space3.grid(row=2, column=0, padx=150)
intro.grid(row=0, column=3)
path_entry.grid(row=1, column=3, padx=50)
file_manager.grid(row=2, column=3)
view_button.grid(row=3, column=3)

# viewer screen
image_counter = StringVar()
img_display = Label(viewer_frame)
img_display.grid(row=0, column=0, columnspan=3)
image_counter_dis = Label(viewer_frame, textvariable=image_counter)
image_counter_dis.grid(row=1, column=1)
back = Button(viewer_frame, text='<<', command=back_img)
_exit = Button(viewer_frame, text='back', command=path_screen)
forward = Button(viewer_frame, text='>>', command=forward_img)
back.grid(row=2, column=0)
_exit.grid(row=2, column=1)
forward.grid(row=2, column=2)

root.mainloop()

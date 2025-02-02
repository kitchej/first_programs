from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import os
from PIL import ImageTk, Image


def open_dir():
    global path
    root.directory = filedialog.askdirectory()
    path.set(root.directory)


def view():
    global images, img, viewer_frame, image_counter, img_display, path_entry, prev1, prev2, prev3, prev4, prev5, prev6,\
        prev7, image_paths, middle, prev1_name_counter, prev2_name_counter, prev3_name_counter, prev5_name_counter, \
        prev6_name_counter, prev7_name_counter
    # print(f"Head: {head}\n"
    #       f"Middle: {middle}\n"
    #       f"Tail: {tail}\n")
    prev1.pack_forget()
    prev2.pack_forget()
    prev3.pack_forget()
    prev4.pack_forget()
    prev5.pack_forget()
    prev6.pack_forget()
    prev7.pack_forget()
    img_display.pack_forget()
    viewer_frame.tkraise()
    try:
        img = ImageTk.PhotoImage(Image.open(image_paths[middle]).resize((720, 480)))
    except FileNotFoundError:
        img = ImageTk.PhotoImage(error_img)
    except PermissionError:
        img = ImageTk.PhotoImage(error_img)
    except OSError:
        img = ImageTk.PhotoImage(error_img)
    img_display = Label(pic_frame, image=img)
    img_display.pack()
    prev1 = Button(preview, image=images[0], command=lambda: jump_backward(3), textvariable=prev1_name,
                   compound=TOP)
    prev2 = Button(preview, image=images[1], command=lambda: jump_backward(2), textvariable=prev2_name,
                   compound=TOP)
    prev3 = Button(preview, image=images[2], command=lambda: jump_backward(1), textvariable=prev3_name,
                   compound=TOP)
    prev4 = Button(preview, image=images[3], textvariable=prev4_name, compound=TOP)
    prev5 = Button(preview, image=images[4], command=lambda: jump_forward(1), textvariable=prev5_name,
                   compound=TOP)
    prev6 = Button(preview, image=images[5], command=lambda: jump_forward(2), textvariable=prev6_name,
                   compound=TOP)
    prev7 = Button(preview, image=images[6], command=lambda: jump_forward(3), textvariable=prev7_name,
                   compound=TOP)
    prev1.pack(side=LEFT)
    prev2.pack(side=LEFT)
    prev3.pack(side=LEFT)
    prev4.pack(side=LEFT)
    prev5.pack(side=LEFT)
    prev6.pack(side=LEFT)
    prev7.pack(side=LEFT)
    image_counter.set(f'{image_counter_num}/{len(image_paths)}')
    prev1_name.set(image_paths[prev1_name_counter])
    prev2_name.set(image_paths[prev2_name_counter])
    prev3_name.set(image_paths[prev3_name_counter])
    prev4_name.set(image_paths[middle])
    prev5_name.set(image_paths[prev5_name_counter])
    prev6_name.set(image_paths[prev6_name_counter])
    prev7_name.set(image_paths[prev7_name_counter])


def get_pics():
    global path_entry, images, error, image_paths, images
    manual_path = path_entry.get()
    if manual_path == "":
        error.set("Please enter a directory to access")
        return
    if manual_path:
        try:
            os.chdir(manual_path)
            image_paths = os.listdir(os.getcwd())
        except AttributeError:
            error.set("Cannot open directory")
            path_frame.tkraise()
            return
        except FileNotFoundError:
            error.set("Cannot open directory")
            path_frame.tkraise()
            return
        except PermissionError:
            error.set("Cannot open directory")
            path_frame.tkraise()
            return
        except OSError:
            error.set("Cannot open directory")
            path_frame.tkraise()
            return
    else:
        try:
            os.chdir(root.directory)
            image_paths = os.listdir(os.getcwd())
        except AttributeError:
            error.set("Cannot open directory")
            path_frame.tkraise()
            return
    try:
        images[0] = ImageTk.PhotoImage(Image.open(image_paths[-3]).resize((100, 75)))
    except FileNotFoundError:
        images[0] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[0] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[0] = ImageTk.PhotoImage(error_img_preview)
    try:
        images[1] = ImageTk.PhotoImage(Image.open(image_paths[-2]).resize((100, 75)))
    except FileNotFoundError:
        images[1] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[1] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[1] = ImageTk.PhotoImage(error_img_preview)
    try:
        images[2] = ImageTk.PhotoImage(Image.open(image_paths[-1]).resize((100, 75)))
    except FileNotFoundError:
        images[2] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[2] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[2] = ImageTk.PhotoImage(error_img_preview)
    try:
        images[3] = ImageTk.PhotoImage(Image.open(image_paths[0]).resize((100, 75)))
    except FileNotFoundError:
        images[3] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[3] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[3] = ImageTk.PhotoImage(error_img_preview)
    try:
        images[4] = ImageTk.PhotoImage(Image.open(image_paths[1]).resize((100, 75)))
    except FileNotFoundError:
        images[4] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[4] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[4] = ImageTk.PhotoImage(error_img_preview)
    try:
        images[5] = ImageTk.PhotoImage(Image.open(image_paths[2]).resize((100, 75)))
    except FileNotFoundError:
        images[5] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[5] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[5] = ImageTk.PhotoImage(error_img_preview)
    try:
        images[6] = ImageTk.PhotoImage(Image.open(image_paths[3]).resize((100, 75)))
    except FileNotFoundError:
        images[6] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[6] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[6] = ImageTk.PhotoImage(error_img_preview)
    view()


def forward_img(jump=False):
    global image_num, image_counter_num, head, tail, images, middle, image_paths, prev1_name_counter, \
        prev2_name_counter, prev3_name_counter, prev5_name_counter, prev6_name_counter, prev7_name_counter
    images[0] = None
    for i in range(len(images)):
        try:
            images[i] = images[i + 1]
        except IndexError:
            images[i] = None
    try:
        images[-1] = ImageTk.PhotoImage(Image.open(image_paths[head]).resize((100, 75)))
    except FileNotFoundError:
        images[-1] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[-1] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[-1] = ImageTk.PhotoImage(error_img_preview)
    if head == len(image_paths) - 1:
        head = 0
    else:
        head += 1

    if tail == len(image_paths) - 1:
        tail = 0
    else:
        tail += 1

    if middle == len(image_paths) - 1:
        middle = 0
    else:
        middle += 1

    if image_counter_num == len(image_paths):
        image_counter_num = 1
    else:
        image_counter_num += 1

    if prev1_name_counter == len(image_paths) - 1:
        prev1_name_counter = 0
    else:
        prev1_name_counter += 1

    if prev2_name_counter == len(image_paths) - 1:
        prev2_name_counter = 0
    else:
        prev2_name_counter += 1

    if prev3_name_counter == len(image_paths) - 1:
        prev3_name_counter = 0
    else:
        prev3_name_counter += 1

    if prev5_name_counter == len(image_paths) - 1:
        prev5_name_counter = 0
    else:
        prev5_name_counter += 1

    if prev6_name_counter == len(image_paths) - 1:
        prev6_name_counter = 0
    else:
        prev6_name_counter += 1

    if prev7_name_counter == len(image_paths) - 1:
        prev7_name_counter = 0
    else:
        prev7_name_counter += 1
    if jump:
        pass
    else:
        view()


def back_img(jump=False):
    global image_num, image_counter_num, head, tail, images, middle, image_paths, prev1_name_counter, \
        prev2_name_counter, prev3_name_counter, prev5_name_counter, prev6_name_counter, prev7_name_counter
    images[-1] = None
    i = -1
    for _ in range(len(images)):
        try:
            images[i] = images[i - 1]
            i -= 1
        except IndexError:
            i -= 1
            pass
    try:
        images[0] = ImageTk.PhotoImage(Image.open(image_paths[tail]).resize((100, 75)))
    except FileNotFoundError:
        images[0] = ImageTk.PhotoImage(error_img_preview)
    except PermissionError:
        images[0] = ImageTk.PhotoImage(error_img_preview)
    except OSError:
        images[0] = ImageTk.PhotoImage(error_img_preview)
    if head == -len(image_paths):
        head = len(image_paths) - 1
    else:
        head -= 1

    if tail == -len(image_paths):
        tail = len(image_paths) - 1
    else:
        tail -= 1

    if middle == -len(image_paths):
        middle = len(image_paths) - 1
    else:
        middle -= 1

    if image_counter_num == 1:
        image_counter_num = len(image_paths)
    else:
        image_counter_num -= 1

    if prev1_name_counter == -len(image_paths):
        prev1_name_counter = len(image_paths) - 1
    else:
        prev1_name_counter -= 1

    if prev2_name_counter == -len(image_paths):
        prev2_name_counter = len(image_paths) - 1
    else:
        prev2_name_counter -= 1

    if prev3_name_counter == -len(image_paths):
        prev3_name_counter = len(image_paths) - 1
    else:
        prev3_name_counter -= 1

    if prev5_name_counter == -len(image_paths):
        prev5_name_counter = len(image_paths) - 1
    else:
        prev5_name_counter -= 1

    if prev6_name_counter == -len(image_paths):
        prev6_name_counter = len(image_paths) - 1
    else:
        prev6_name_counter -= 1

    if prev7_name_counter == -len(image_paths):
        prev7_name_counter = len(image_paths) - 1
    else:
        prev7_name_counter -= 1

    if jump:
        pass
    else:
        view()


def jump_forward(places):
    for _ in range(places):
        forward_img(True)
    view()


def jump_backward(places):
    for _ in range(places):
        back_img(True)
    view()


def path_screen():
    global image_paths, img, pic1, pic2, pic3, pic4, pic5, pic6, pic7, head, tail, middle, images, image_num, \
        image_counter_num, path, prev1_name_counter, prev2_name_counter, prev3_name_counter, prev5_name_counter,\
        prev6_name_counter, prev7_name_counter
    path_frame.tkraise()
    path.set("")
    image_paths = []
    img = None
    pic1 = None
    pic2 = None
    pic3 = None
    pic4 = None
    pic5 = None
    pic6 = None
    pic7 = None
    head = 4
    middle = 0
    tail = -4
    prev1_name_counter = -3
    prev2_name_counter = -2
    prev3_name_counter = -1
    prev5_name_counter = 1
    prev6_name_counter = 2
    prev7_name_counter = 3
    images = [pic1, pic2, pic3, pic4, pic5, pic6, pic7]
    image_num = 0
    image_counter_num = 1


error_img_preview = Image.open(r'error_image.png').resize((100, 75))
error_img = Image.open(r'error_image.png')
image_paths = []
img = None
pic1 = None
pic2 = None
pic3 = None
pic4 = None
pic5 = None
pic6 = None
pic7 = None
head = 4
middle = 0
tail = -4
prev1_name_counter = -3
prev2_name_counter = -2
prev3_name_counter = -1
prev5_name_counter = 1
prev6_name_counter = 2
prev7_name_counter = 3
images = [pic1, pic2, pic3, pic4, pic5, pic6, pic7]
image_num = 0
image_counter_num = 1

root = Tk()
root.title('Image Viewer')
root.minsize(height=475, width=700)
path_frame = Frame(root)
viewer_frame = Frame(root)

for frame in (path_frame, viewer_frame):
    frame.grid(row=0, column=0, sticky='news')

# enter path screen
path_frame.tkraise()
path = StringVar()
error = StringVar()
white_space = Label(path_frame)
white_space2 = Label(path_frame)
white_space3 = Label(path_frame)
intro = Label(path_frame, text='Enter Path:')
path_entry = Entry(path_frame, textvariable=path)
file_manager = Button(path_frame, text='Open File Manager', command=open_dir)
view_button = Button(path_frame, text='View', command=get_pics)
error_message = Label(path_frame, textvariable=error, foreground='red')
white_space.grid(row=0, column=0, padx=120)
white_space2.grid(row=1, column=0, padx=120)
white_space3.grid(row=2, column=0, padx=120)
intro.grid(row=0, column=3)
path_entry.grid(row=1, column=3, padx=50)
file_manager.grid(row=2, column=3)
view_button.grid(row=3, column=3)
error_message.grid(row=4, column=3)

# viewer screen
image_counter = StringVar()
prev1_name = StringVar()
prev2_name = StringVar()
prev3_name = StringVar()
prev4_name = StringVar()
prev5_name = StringVar()
prev6_name = StringVar()
prev7_name = StringVar()
pic_frame = Frame(viewer_frame)
control_panel = Frame(viewer_frame)
preview = Frame(viewer_frame)
img_display = Label(pic_frame)
back = Button(control_panel, text='<<', command=back_img)
_exit = Button(control_panel, text='back', command=path_screen)
forward = Button(control_panel, text='>>', command=forward_img)
image_counter_dis = Label(control_panel, textvariable=image_counter)
prev1 = Button(preview)
prev2 = Button(preview)
prev3 = Button(preview)
prev4 = Button(preview)
prev5 = Button(preview)
prev6 = Button(preview)
prev7 = Button(preview)

pic_frame.pack(side=TOP)
control_panel.pack(side=BOTTOM)
preview.pack(sid=BOTTOM)
img_display.pack()
image_counter_dis.pack()
prev1.pack()
prev2.pack()
prev3.pack()
prev4.pack()
prev5.pack()
prev6.pack()
prev7.pack()
back.pack(side=LEFT)
_exit.pack(side=LEFT)
forward.pack(side=LEFT)

root.mainloop()

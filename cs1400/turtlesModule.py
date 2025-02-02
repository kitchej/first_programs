'''
Project Name: Doodling with Turtles
Author: Joshua Kitchen
Due Date: MM/DD/YYYY
Course: CS1400-005

Put your description here, lessons learned here, and any other information someone using your
program would need to know to make it run.
'''
import turtle as t
import math

grey_scale = [
        '#ffffff',
        '#f2f2f2',
        '#e6e6e6',
        '#d9d9d9',
        '#cccccc',
        '#bfbfbf',
        '#b3b3b3',
        '#a6a6a6',
        '#999999',
        '#8c8c8c',
        '#808080',
        '#737373',
        '#666666',
        '#595959',
        '#4d4d4d',
        '#404040',
        '#333333',
        '#262626',
        '#1a1a1a',
        '#0d0d0d',
        '#000000',
    ]

blue_scale = [
    '#ffffff',
    '#e6eeff',
    '#ccddff',
    '#b3ccff',
    '#99bbff',
    '#80aaff',
    '#6699ff',
    '#4d88ff',
    '#3377ff',
    '#1a66ff',
    '#0055ff',
    '#004de6',
    '#0044cc',
    '#003cb3',
    '#003399',
    '#002b80',
    '#002266',
    '#001a4d',
    '#001133',
    '#00091a',
    '#000000',
]
red_scale = [
    '#ffffff',
    '#ffebe6',
    '#ffd6cc',
    '#ffc2b3',
    '#ffad99',
    '#ff9980',
    '#ff8566',
    '#ff704d',
    '#ff5c33',
    '#ff471a',
    '#ff3300',
    '#e62e00',
    '#cc2900',
    '#b32400',
    '#991f00',
    '#801a00',
    '#661400',
    '#4d0f00',
    '#330a00',
    '#1a0500',
    '#000000',
]
green_scale = [
    '#ffffff',
    '#e6ffe6',
    '#ccffcc',
    '#b3ffb3',
    '#99ff99',
    '#80ff80',
    '#66ff66',
    '#4dff4d',
    '#33ff33',
    '#1aff1a',
    '#00ff00',
    '#00e600',
    '#00cc00',
    '#00b300',
    '#009900',
    '#008000',
    '#006600',
    '#004d00',
    '#003300',
    '#001a00',
    '#000000',
]
yellow_scale = [
    '#ffffff',
    '#ffffe6',
    '#ffffcc',
    '#ffffb3',
    '#ffff99',
    '#ffff80',
    '#ffff66',
    '#ffff4d',
    '#ffff33',
    '#ffff1a',
    '#ffff00',
    '#e6e600',
    '#cccc00',
    '#b3b300',
    '#999900',
    '#808000',
    '#666600',
    '#4d4d00',
    '#333300',
    '#1a1a00',
    '#000000',
]
purple_scale = [
    '#ffffff',
    '#f9ecf9',
    '#f2d9f2',
    '#ecc6ec',
    '#e6b3e6',
    '#df9fdf',
    '#d98cd9',
    '#d279d2',
    '#cc66cc',
    '#c653c6',
    '#bf40bf',
    '#ac39ac',
    '#993399',
    '#862d86',
    '#732673',
    '#602060',
    '#4d194d',
    '#391339',
    '#260d26',
    '#130613',
    '#000000',
]
orange_scale = [
    '#ffffff',
    '#fff5e6',
    '#ffebcc',
    '#ffe0b3',
    '#ffd699',
    '#ffcc80',
    '#ffc266',
    '#ffb84d',
    '#ffad33',
    '#ffa31a',
    '#ff9900',
    '#e68a00',
    '#cc7a00',
    '#b36b00',
    '#995c00',
    '#804d00',
    '#663d00',
    '#4d2e00',
    '#331f00',
    '#1a0f00',
    '#000000',
    ]


def circle(size, fill_color, border_color, rotation=None):
    if rotation:
        t.left(rotation)
    t.color(border_color, fill_color)
    t.begin_fill()
    for _ in range(360):
        t.forward(size)
        t.left(1)
    t.end_fill()


# initial_angle_size must between 60 and 179 degrees for stable performance
def triangle(size, fill_color, border_color, initial_angle_size=None, rotation=None, border_same_as_fill=False):
    if rotation:
        t.left(rotation)
    if not initial_angle_size:
        initial_angle_size = 60  # defaults to an equilateral triangle

    # calculate the size of the other two angles
    opposite_angle_size = (180 - initial_angle_size) / 2
    angles = [initial_angle_size, opposite_angle_size, opposite_angle_size]

    # calculate the other two sides
    side_a = size
    side_b = (side_a / math.sin(math.radians(angles[2]))) * (math.sin(math.radians(angles[0])))
    side_c = (side_a / math.sin(math.radians(angles[2]))) * (math.sin(math.radians(angles[1])))
    sides = [side_a, side_b, side_c]

    if border_same_as_fill:
        t.color(fill_color, fill_color)
    else:
        t.color(border_color, fill_color)
    t.begin_fill()
    for angle, side in zip(angles, sides):
        t.forward(size)
        t.left(180 - angle)
    t.end_fill()


# initial_angle_size must be between 1 and 179 degrees for stable performance
def rhombus(size, fill_color, border_color, initial_angle_size, rotation=None):
    if rotation:
        t.left(rotation)
    opposite_angle_size = (360 - (initial_angle_size * 2)) / 2
    angles = [initial_angle_size, opposite_angle_size, initial_angle_size, opposite_angle_size]

    t.color(border_color, fill_color)
    t.begin_fill()
    for angle in angles:
        t.forward(size)
        t.left(angle)
    t.end_fill()


def square(size, fill_color, border_color, rotation=None):
    if rotation:
        t.left(rotation)
    t.color(border_color, fill_color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()


# size arg should be a tuple: (width, height)
def rectangle(size, fill_color, border_color, rotation=None, border_same_as_fill=False):
    if rotation:
        t.left(rotation)
    if border_same_as_fill:
        t.color(fill_color, fill_color)
    else:
        t.color(border_color, fill_color)
    width = size[0]
    height = size[1]

    sides = [width, height, width, height]

    t.begin_fill()
    for side in sides:
        t.forward(side)
        t.left(90)
    t.end_fill()


def penup_forward(distance):
    t.penup()
    t.forward(distance)
    t.pendown()


def penup_backward(distance):
    t.penup()
    t.backward(distance)
    t.pendown()


def penup_right(rotation):
    t.penup()
    t.right(rotation)
    t.pendown()


def penup_left(rotation):
    t.penup()
    t.left(rotation)
    t.pendown()


def penup_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def pinwheel(size, color):
    initial_pos = t.pos()
    rotate = 0
    for _ in range(8):
        triangle(size, color, 'black', 90, rotation=45)
        t.goto(initial_pos)
        rotate += 1


# 8 colors max
def rainbow_pinwheel(size, colors=None):
    initial_pos = t.pos()
    if colors is None:
        colors = ['purple', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'black']
    color_index = 0
    for _ in range(8):
        triangle(size, colors[color_index], 'black', 90, rotation=45)
        t.goto(initial_pos)
        color_index += 1
        if color_index > len(colors) - 1:
            color_index = 0


def color_shade_pinwheel(colors, size):
    init_pos = t.pos()
    for color in colors:
        triangle(size, color, 'black', 90, 16.6, border_same_as_fill=True)
        t.goto(init_pos)


def create_color_bar():
    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % rgb

    start_rgb = [204, 0, 0]
    start_x = -820
    start_y = -250
    penup_goto(start_x, start_y)

    rectangle_width = 8
    increment = 6
    loops = 204/increment
    loops = int(loops)

    for i in range(loops):
        try:
            rectangle((rectangle_width, 50), rgb_to_hex(tuple(start_rgb)), 'black', border_same_as_fill=True)
        except t.TurtleGraphicsError:
            start_rgb[2] += increment
            continue
        penup_forward(rectangle_width)
        start_rgb[2] += increment

    for i in range(loops):
        try:
            rectangle((rectangle_width, 50), rgb_to_hex(tuple(start_rgb)), 'black', border_same_as_fill=True)
        except t.TurtleGraphicsError:
            start_rgb[0] -= increment
            continue
        penup_forward(rectangle_width)
        start_rgb[0] -= increment

    for i in range(loops):
        try:
            rectangle((rectangle_width, 50), rgb_to_hex(tuple(start_rgb)), 'black', border_same_as_fill=True)
        except t.TurtleGraphicsError:
            start_rgb[1] += increment
            continue
        penup_forward(rectangle_width)
        start_rgb[1] += increment

    for i in range(loops):
        try:
            rectangle((rectangle_width, 50), rgb_to_hex(tuple(start_rgb)), 'black', border_same_as_fill=True)
        except t.TurtleGraphicsError:
            start_rgb[2] -= increment
            continue
        penup_forward(rectangle_width)
        start_rgb[2] -= increment

    for i in range(loops):
        try:
            rectangle((rectangle_width, 50), rgb_to_hex(tuple(start_rgb)), 'black', border_same_as_fill=True)
        except t.TurtleGraphicsError:
            start_rgb[0] += increment
            continue
        penup_forward(rectangle_width)
        start_rgb[0] += increment

    for i in range(loops):
        try:
            rectangle((rectangle_width, 50), rgb_to_hex(tuple(start_rgb)), 'black', border_same_as_fill=True)
        except t.TurtleGraphicsError:
            start_rgb[1] -= increment
            continue
        penup_forward(rectangle_width)
        start_rgb[1] -= increment


def half_circle(size, rotation, fill_color=None, border_color=None, closed=True):
    start = t.pos()
    t.left(rotation)
    if fill_color is not None and border_color is not None:
        t.color(border_color, fill_color)
        t.begin_fill()
    for _ in range(180):
        t.forward(size)
        t.left(1)
    if closed:
        t.left(t.towards(start))
        t.goto(start)
    if fill_color is not None and border_color is not None:
        t.end_fill()


def draw_cloud(fill_color, border_color):
    turns = [0, 250, 190, 225, 290, 180, 225]
    t.color(border_color, fill_color)
    t.begin_fill()
    for turn in turns:
        t.left(turn)
        half_circle(1, 0, closed=False)
    t.end_fill()


def create_color_waves(start_x=-820, start_y=-400):
    def rgb_to_hex(rgb):
        return "#%02x%02x%02x" % rgb

    def increment_rgb(increment_level, rectangle_width, rectangle_height, color, operator):
        colors = {'r': 0, 'g': 1, 'b': 2}
        wave_counter = 0
        loops = 204 / increment_level
        loops = int(loops)
        for i in range(loops):
            try:
                rectangle((rectangle_width, rectangle_height), rgb_to_hex(tuple(start_rgb)), 'black',
                          border_same_as_fill=True)
            except t.TurtleGraphicsError:
                if operator == '+':
                    start_rgb[colors[color]] += increment_level
                else:
                    start_rgb[colors[color]] -= increment_level
                continue

            penup_forward(rectangle_width)

            if operator == '+':
                start_rgb[colors[color]] += increment_level
            else:
                start_rgb[colors[color]] -= increment_level
            wave_counter += 1

            if wave_counter < 51:
                rectangle_height += 1
            else:
                rectangle_height -= 1

    start_rgb = [204, 0, 0]
    penup_goto(start_x, start_y)

    increment_rgb(2, 2.7, 200, 'b', '+')
    increment_rgb(2, 2.7, 200, 'r', '-')
    increment_rgb(2, 2.7, 200, 'g', '+')
    increment_rgb(2, 2.7, 200, 'b', '-')
    increment_rgb(2, 2.7, 200, 'r', '+')
    increment_rgb(2, 2.7, 200, 'g', '-')

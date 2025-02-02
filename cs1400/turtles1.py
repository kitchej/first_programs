'''
Project Name: Doodling with Turtles
Author: Joshua Kitchen
Due Date: MM/DD/YYYY
Course: CS1400-005

optimal screen size is 1640X800

Color waves at the bottom appear to be several triangles but are actually hundreds of individual rectangles that
gradually change their color and fluctuate in height.
'''
import turtle as t
import math


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


def penup_forward(distance):
    t.penup()
    t.forward(distance)
    t.pendown()


def penup_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def penup_home():
    t.penup()
    t.home()
    t.pendown()


def draw_cloud(fill_color, border_color):
    turns = [0, 250, 190, 225, 290, 180, 225]
    t.color(border_color, fill_color)
    t.begin_fill()
    for turn in turns:
        t.left(turn)
        half_circle(1, 0, closed=False)
    t.end_fill()


def draw_rectangle_pinwheel(colors):
    for color in colors:
        rectangle((20, 45), color, 'black', rotation=45, border_same_as_fill=True)


def color_shade_pinwheel(colors, size):
    init_pos = t.pos()
    for color in colors:
        triangle(size, color, 'black', 90, 16.6, border_same_as_fill=True)
        t.goto(init_pos)


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


def main():
    try:
        width = input("Enter the width of the window: ")
        height = input("Enter the height of the window: ")
        width = int(width)
        height = int(height)

    except ValueError:
        print("Enter postive integers for width and height.")
        return

    if width < 1 or height < 1:
        print("Enter postive integers for width and height.")
        return

    t.screensize(width, height)
    t.bgcolor('#808080')
    t.hideturtle()
    t.speed('fastest')

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
        '#ffffff',
        '#e6ffe6',
        '#ccffcc',
        '#b3ffb3',
        '#99ff99',
        '#80ff80',
        '#66ff66',
        '#4dff4d',
        '#33ff33'
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
    ]

    yellow_scale = [
        '#ffffcc',
        '#ffffb3',
        '#ffff99',
        '#ffff80',
        '#ffff66',
        '#ffff4d',
        '#ffff33',
        '#ffff1a',
        '#ffff00',
    ]

    purple_scale = [
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
    ]

    penup_goto(-425, 150)
    draw_cloud('#b436c7', 'black')

    penup_goto(700, 250)
    color_shade_pinwheel(green_scale, 75)

    penup_goto(700, 250)
    color_shade_pinwheel(blue_scale, 50)

    penup_goto(450, 200)
    color_shade_pinwheel(red_scale, 50)

    penup_goto(450, 200)
    color_shade_pinwheel(orange_scale, 35)

    penup_home()

    penup_goto(100, 350)

    draw_rectangle_pinwheel(yellow_scale)

    penup_home()

    penup_goto(50, 250)

    draw_rectangle_pinwheel(purple_scale)

    penup_home()

    penup_goto(0, -150)
    half_circle(1, 290, '#269900', '#269900', True)
    t.left(70)
    t.forward(60)
    t.left(90)
    t.color('brown', 'brown')
    t.forward(100)
    triangle(50, '#000066', '#000066', initial_angle_size=90, rotation=180)

    penup_home()

    create_color_waves()

    t.mainloop()


if __name__ == "__main__":
    main()

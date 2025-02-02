"""
Project Name: Turtles II
Author: Joshua Kitchen
Due Date: 11/14/2020
Course: CS1400-005

options from command line - green, blue, red, purple, orange, grey, yellow, or all
changes the color of the main scene
Example: 
$ python3 turtles2.py green

"""
import turtle
import math
import sys


# initial_angle_size must between 60 and 179 degrees for stable performance
def triangle(turtle_obj, size, fill_color, border_color, initial_angle_size=None, rotation=None,
             border_same_as_fill=False):
    if rotation:
        turtle_obj.left(rotation)
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
        turtle_obj.color(fill_color, fill_color)
    else:
        turtle_obj.color(border_color, fill_color)
    turtle_obj.begin_fill()
    for angle, side in zip(angles, sides):
        turtle_obj.forward(size)
        turtle_obj.left(180 - angle)
    turtle_obj.end_fill()


# size arg should be a tuple: (width, height)
def rectangle(turtle_obj, size, fill_color, border_color, rotation=None, border_same_as_fill=False):
    if rotation:
        turtle_obj.left(rotation)
    if border_same_as_fill:
        turtle_obj.color(fill_color, fill_color)
    else:
        turtle_obj.color(border_color, fill_color)
    width = size[0]
    height = size[1]

    sides = [width, height, width, height]

    turtle_obj.begin_fill()
    for side in sides:
        turtle_obj.forward(side)
        turtle_obj.left(90)
    turtle_obj.end_fill()


def half_circle(turtle_obj, size, rotation, fill_color=None, border_color=None, closed=True):
    start = turtle_obj.pos()
    turtle_obj.left(rotation)
    if fill_color is not None and border_color is not None:
        turtle_obj.color(border_color, fill_color)
        turtle_obj.begin_fill()
    for _ in range(180):
        turtle_obj.forward(size)
        turtle_obj.left(1)
    if closed:
        turtle_obj.left(turtle_obj.towards(start))
        turtle_obj.goto(start)
    if fill_color is not None and border_color is not None:
        turtle_obj.end_fill()


def penup_forward(turtle_obj, distance):
    turtle_obj.penup()
    turtle_obj.forward(distance)
    turtle_obj.pendown()


def penup_goto(turtle_obj, x=0, y=0, turtle_pos=None):
    turtle_obj.penup()
    if turtle_pos:
        turtle_obj.goto(turtle_pos)
    else:
        turtle_obj.goto(x, y)
    turtle_obj.pendown()


def penup_home(turtle_obj):
    turtle_obj.penup()
    turtle_obj.home()
    turtle_obj.pendown()


def draw_cloud(turtle_obj, fill_color, border_color):
    turns = [0, 250, 190, 225, 290, 180, 225]
    turtle_obj.color(border_color, fill_color)
    turtle_obj.begin_fill()
    for turn in turns:
        turtle_obj.left(turn)
        half_circle(turtle_obj, 1, 0, closed=False)
    turtle_obj.end_fill()


# size arg must be a tuple (width, height) - determines the size of each rectangle
def draw_rectangle_pinwheel(turtle_obj, colors, size):
    for color in colors:
        rectangle(turtle_obj, size, color, 'black', rotation=45, border_same_as_fill=True)


def color_shade_pinwheel(turtle_obj, colors, size):
    init_pos = turtle_obj.pos()
    for color in colors:
        triangle(turtle_obj, size, color, 'black', 90, 16.6, border_same_as_fill=True)
        turtle_obj.goto(init_pos)


def colorshade_shell(turtle_obj, colors, radius, rotation=None):
    if rotation:
        turtle_obj.left(rotation)
    original_pos = turtle_obj.pos()
    for color in colors:
        turtle_obj.color(color, color)
        turtle_obj.begin_fill()
        turtle_obj.circle(radius, (360 / len(colors)))
        position = turtle_obj.pos()
        turtle_obj.goto(original_pos)
        turtle_obj.end_fill()
        turtle_obj.goto(position)


def make_balloons(turtle_obj, color_scales, size, scale):
    rotation = 0
    switch = False
    count = 0
    x = turtle_obj.pos()[0]
    y = turtle_obj.pos()[1]
    string_size = 400 / scale
    balloon_pos = []
    for color in color_scales:
        end_pos = turtle_obj.pos()
        colorshade_shell(turtle_obj, color, size, rotation=rotation)
        balloon_pos.append(end_pos)

        if count == 3:
            switch = True

        if switch:
            x = x + (50 / scale)
            y = y - (10 / scale)
        else:
            x = x + (50 / scale)
            y = y + (10 / scale)

        penup_goto(turtle_obj, x, y)
        count += 1

    # Draw balloon strings
    penup_goto(turtle_obj, 0, 0, turtle_pos=balloon_pos.pop(3))
    turtle_obj.right(90)
    turtle_obj.forward(string_size)
    center = turtle_obj.pos()
    for pos in balloon_pos:
        penup_goto(turtle_obj, 0, 0, turtle_pos=pos)
        turtle_obj.goto(center)

    turtle_obj.left(90)
    penup_goto(turtle_obj, 0, 0, turtle_pos=center)


def create_colorshade_box(turtle_obj, color_scale, size):
    width = size[0] / len(color_scale)
    height = size[1]
    increment = width
    for color in color_scale:
        rectangle(turtle_obj, (width, height), color, color, border_same_as_fill=True)
        penup_forward(turtle_obj, increment)


# All dimensions are divided by the 'scale' argrument. So if scale = 2, then the picture will be half the size
def main_picture(turtle_obj, scale, start_x, start_y, mode='all'):
    yellow_scale_partial = [
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

    red_scale_partial = [
        '#ffffff',
        '#ffebe6',
        '#ffd6cc',
        '#ffc2b3',
        '#ffad99',
        '#ff9980',
        '#ff8566',
        '#ff704d',
        '#ff5c33',
    ]

    orange_scale_partial = [
        '#ffffff',
        '#fff5e6',
        '#ffebcc',
        '#ffe0b3',
        '#ffd699',
        '#ffcc80',
        '#ffc266',
        '#ffb84d',
        '#ffad33',
    ]

    blue_scale_partial = [
        '#ffffff',
        '#e6eeff',
        '#ccddff',
        '#b3ccff',
        '#99bbff',
        '#80aaff',
        '#6699ff',
        '#4d88ff',
        '#3377ff',
    ]

    grey_scale_partial = [
        '#ffffff',
        '#f2f2f2',
        '#e6e6e6',
        '#d9d9d9',
        '#cccccc',
        '#bfbfbf',
        '#b3b3b3',
        '#a6a6a6',
        '#999999',
    ]

    green_scale_partial = [
        '#ffffff',
        '#e6ffe6',
        '#ccffcc',
        '#b3ffb3',
        '#99ff99',
        '#80ff80',
        '#66ff66',
        '#4dff4d',
        '#33ff33',
    ]

    purple_scale_partial = [
        '#ffffff',
        '#f9ecf9',
        '#f2d9f2',
        '#ecc6ec',
        '#e6b3e6',
        '#df9fdf',
        '#d98cd9',
        '#d279d2',
        '#cc66cc',
    ]

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
    if mode == 'all':
        main_color_scale = None
        color_scales = [grey_scale, blue_scale, green_scale, orange_scale, red_scale, yellow_scale, purple_scale]
        pinwheel_colors = [purple_scale, blue_scale, green_scale, grey_scale]
        rectangle_pinwheel_colors = [red_scale_partial, yellow_scale_partial, orange_scale_partial]
    elif mode == 'red':
        main_color_scale = red_scale
        color_scales = [red_scale, red_scale, red_scale, red_scale, red_scale, red_scale, red_scale]
        pinwheel_colors = [red_scale, red_scale, red_scale, red_scale]
        rectangle_pinwheel_colors = [red_scale_partial, red_scale_partial, red_scale_partial]
    elif mode == 'blue':
        main_color_scale = blue_scale
        color_scales = [blue_scale, blue_scale, blue_scale, blue_scale, blue_scale, blue_scale, blue_scale]
        pinwheel_colors = [blue_scale, blue_scale, blue_scale, blue_scale]
        rectangle_pinwheel_colors = [blue_scale_partial, blue_scale_partial, blue_scale_partial]
    elif mode == 'green':
        main_color_scale = green_scale
        color_scales = [green_scale, green_scale, green_scale, green_scale, green_scale, green_scale, green_scale]
        pinwheel_colors = [green_scale, green_scale, green_scale, green_scale]
        rectangle_pinwheel_colors = [green_scale_partial, green_scale_partial, green_scale_partial]
    elif mode == 'purple':
        main_color_scale = purple_scale
        color_scales = [purple_scale, purple_scale, purple_scale, purple_scale, purple_scale, purple_scale,
                        purple_scale]
        pinwheel_colors = [purple_scale, purple_scale, purple_scale, purple_scale]
        rectangle_pinwheel_colors = [purple_scale_partial, purple_scale_partial, purple_scale_partial]
    elif mode == 'orange':
        main_color_scale = orange_scale
        color_scales = [orange_scale, orange_scale, orange_scale, orange_scale, orange_scale, orange_scale,
                        orange_scale]
        pinwheel_colors = [orange_scale, orange_scale, orange_scale, orange_scale]
        rectangle_pinwheel_colors = [orange_scale_partial, orange_scale_partial, orange_scale_partial]
    elif mode == 'grey':
        main_color_scale = grey_scale
        color_scales = [grey_scale, grey_scale, grey_scale, grey_scale, grey_scale, grey_scale, grey_scale]
        pinwheel_colors = [grey_scale, grey_scale, grey_scale, grey_scale]
        rectangle_pinwheel_colors = [grey_scale_partial, grey_scale_partial, grey_scale_partial]
    elif mode == 'yellow':
        main_color_scale = yellow_scale
        color_scales = [yellow_scale, yellow_scale, yellow_scale, yellow_scale, yellow_scale, yellow_scale,
                        yellow_scale]
        pinwheel_colors = [yellow_scale, yellow_scale, yellow_scale, yellow_scale]
        rectangle_pinwheel_colors = [yellow_scale_partial, yellow_scale_partial, yellow_scale_partial]
    else:
        print(f'Bad value \"{mode}\" for arg mode')
        return

    """Size values"""
    box_width, box_height = 300 / scale, 200 / scale
    balloons_size = 100 / scale
    box_pos = 150 / scale

    # for pinwheels
    pinwheel_size = 20 / scale
    rec_pinwheel_size = (10 / scale, 20 / scale)
    stand_height = 65 / scale
    spacing = 23 / scale

    """Main Code"""
    penup_goto(turtle_obj, start_x, start_y)
    make_balloons(turtle_obj, color_scales, balloons_size, scale)
    turtle_obj.left(180)
    penup_forward(turtle_obj, box_pos)

    turtle_obj.left(180)

    if mode == 'all':
        create_colorshade_box(turtle_obj, size=(box_width, box_height), color_scale=red_scale)
    else:
        create_colorshade_box(turtle_obj, size=(box_width, box_height), color_scale=main_color_scale)

    sides = [box_height, box_width, box_height, box_width]
    turtle_obj.pencolor('black')
    for side in sides:
        turtle_obj.left(90)
        turtle_obj.forward(side)

    turtle_obj.left(90)

    turtle_obj.forward(box_height)

    heading = turtle_obj.heading()

    for color in pinwheel_colors:
        turtle_obj.forward(stand_height)
        color_shade_pinwheel(turtle_obj, color, pinwheel_size)
        turtle_obj.setheading(heading)

        turtle_obj.left(180)
        turtle_obj.forward(stand_height)

        turtle_obj.right(90)

        turtle_obj.forward(pinwheel_size + spacing)
        turtle_obj.right(90)

    for color in rectangle_pinwheel_colors:
        turtle_obj.forward(stand_height)
        draw_rectangle_pinwheel(turtle_obj, color, rec_pinwheel_size)
        turtle_obj.pencolor('black')
        turtle_obj.setheading(heading)

        turtle_obj.left(180)
        turtle_obj.forward(stand_height)

        turtle_obj.right(90)

        turtle_obj.forward(rec_pinwheel_size[1] + spacing)
        turtle_obj.right(90)


def main():
    args = sys.argv
    args.remove('turtles2.py')

    modes = ['all', 'green', 'blue', 'red', 'purple', 'orange', 'grey', 'yellow']

    if len(args) > 1:
        print("Too many arguments")
        return

    if args[0] not in modes:
        print(f'Bad argument \"{args[0]}\"')
        return

    mode = args[0]

    turtle.screensize(1000, 600)

    turtle1 = turtle.Turtle()

    turtle1.hideturtle()
    turtle1.speed('fastest')

    penup_goto(turtle1, -675, -315)
    rectangle(turtle1, (1350, 100), 'green', 'black')
    turtle1.left(90)
    penup_forward(turtle1, 100)
    turtle1.right(90)
    rectangle(turtle1, (1350, 1350), '#87CEEB', 'black')

    penup_goto(turtle1, -250, 150)

    draw_cloud(turtle1, 'white', 'black')

    turtle1.right(100)

    main_picture(turtle1, 1, -150, 100, mode=mode)
    turtle1.right(90)
    main_picture(turtle1, 4, -40, -150, mode=mode)

    turtle.mainloop()


if __name__ == "__main__":
    main()

import turtle as t


def draw_fancy_s(scale_factor=1.0, color='white'):
    t.fillcolor(color)
    t.begin_fill()
    t.left(225)

    for _ in range(2):
        t.forward(100 / scale_factor)
        t.left(45)

    t.forward(100 / scale_factor)
    t.right(45)
    t.forward(100 / scale_factor)
    t.back(100 / scale_factor)
    t.right(90)
    t.forward(75 / scale_factor)
    t.left(90)
    t.forward(100 / scale_factor)
    t.left(45)
    t.forward(100 / scale_factor)

    t.left(90)

    for _ in range(2):
        t.forward(100 / scale_factor)
        t.left(45)

    t.forward(100 / scale_factor)
    t.right(45)
    t.forward(100 / scale_factor)
    t.back(100 / scale_factor)
    t.right(90)
    t.forward(75 / scale_factor)
    t.left(90)
    t.forward(100 / scale_factor)
    t.left(45)
    t.forward(100 / scale_factor)
    t.end_fill()


def penup_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


t.hideturtle()
t.speed('fastest')

penup_goto(-1500, 525)

start_x, start_y = t.pos()
current_x = start_x

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
    '#000000',
    '#00091a',
    '#001133',
    '#001a4d',
    '#002266',
    '#002b80',
    '#003399',
    '#003cb3',
    '#0044cc',
    '#004de6',
    '#0055ff',
    '#1a66ff',
    '#3377ff',
    '#4d88ff',
    '#6699ff',
    '#80aaff',
    '#99bbff',
    '#b3ccff',
    '#ccddff',
    '#e6eeff',
    '#ffffff',
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
    '#000000',
    '#1a0500',
    '#330a00',
    '#4d0f00',
    '#661400',
    '#801a00',
    '#991f00',
    '#b32400',
    '#cc2900',
    '#e62e00',
    '#ff3300',
    '#ff471a',
    '#ff5c33',
    '#ff704d',
    '#ff8566',
    '#ff9980',
    '#ffad99',
    '#ffc2b3',
    '#ffd6cc',
    '#ffebe6',
    '#ffffff',
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
    '#000000',
    '#1a0f00',
    '#331f00',
    '#4d2e00',
    '#663d00',
    '#804d00',
    '#995c00',
    '#b36b00',
    '#cc7a00',
    '#e68a00',
    '#ff9900',
    '#ffa31a',
    '#ffad33',
    '#ffb84d',
    '#ffc266',
    '#ffcc80',
    '#ffd699',
    '#ffe0b3',
    '#ffebcc',
    '#fff5e6',
    '#ffffff',
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
    '#000000',
    '#1a1a00',
    '#333300',
    '#4d4d00',
    '#666600',
    '#808000',
    '#999900',
    '#b3b300',
    '#cccc00',
    '#e6e600',
    '#ffff00',
    '#ffff1a',
    '#ffff33',
    '#ffff4d',
    '#ffff66',
    '#ffff80',
    '#ffff99',
    '#ffffb3',
    '#ffffcc',
    '#ffffe6',
    '#ffffff',
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
    '#000000',
    '#001a00',
    '#003300',
    '#004d00',
    '#006600',
    '#008000',
    '#009900',
    '#00b300',
    '#00cc00',
    '#00e600',
    '#00ff00',
    '#1aff1a',
    '#33ff33',
    '#4dff4d',
    '#66ff66',
    '#80ff80',
    '#99ff99',
    '#b3ffb3',
    '#ccffcc',
    '#e6ffe6',
    '#ffffff',
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
    '#000000',
    '#130613',
    '#260d26',
    '#391339',
    '#4d194d',
    '#602060',
    '#732673',
    '#862d86',
    '#993399',
    '#ac39ac',
    '#bf40bf',
    '#c653c6',
    '#cc66cc',
    '#d279d2',
    '#d98cd9',
    '#df9fdf',
    '#e6b3e6',
    '#ecc6ec',
    '#f2d9f2',
    '#f9ecf9',
    '#ffffff',
]

for color in blue_scale:
    draw_fancy_s(scale_factor=2, color=color)
    t.right(135)
    current_x += 70
    penup_goto(current_x, start_y)

start_y -= 174
start_x += 32.5
current_x = start_x
penup_goto(start_x, start_y)

for color in green_scale:
    draw_fancy_s(scale_factor=2, color=color)
    t.right(135)
    current_x += 70
    penup_goto(current_x, start_y)

start_y -= 174
start_x += 32.5
current_x = start_x
penup_goto(start_x, start_y)

for color in purple_scale:
    draw_fancy_s(scale_factor=2, color=color)
    t.right(135)
    current_x += 70
    penup_goto(current_x, start_y)

start_y -= 174
start_x += 32.5
current_x = start_x
penup_goto(start_x, start_y)

for color in red_scale:
    draw_fancy_s(scale_factor=2, color=color)
    t.right(135)
    current_x += 70
    penup_goto(current_x, start_y)

start_y -= 174
start_x += 32.5
current_x = start_x
penup_goto(start_x, start_y)

for color in orange_scale:
    draw_fancy_s(scale_factor=2, color=color)
    t.right(135)
    current_x += 70
    penup_goto(current_x, start_y)

start_y -= 174
start_x += 32.5
current_x = start_x
penup_goto(start_x, start_y)

for color in yellow_scale:
    draw_fancy_s(scale_factor=2, color=color)
    t.right(135)
    current_x += 70
    penup_goto(current_x, start_y)

t.mainloop()

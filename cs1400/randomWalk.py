"""
Project Name: Project 6 - Random Walk
Author: Joshua Kitchen
Due Date: 12/5/2020
Course: CS1400-005

Command Line: randomWalk.py [walkLengths] [trials] [type]
Example:
    $: randomWalk.py 100,1000 50 all
"""
import random
import math
import statistics as stat
import sys
import turtle as t


# calculates the distance between two points. Point args must be tuples of (x, y) values
def calc_distance(point1, point2):

    a = ((point2[0] - point1[0]) ** 2)
    b = ((point2[1] - point1[1]) ** 2)

    return math.sqrt((a + b))


def pa(walk_length, trials):
    distances = []
    coordinates = []
    directions = ['n', 'e', 's', 'w']
    for _ in range(trials):
        x = 0
        y = 0
        for _ in range(walk_length):
            heading = random.choice(directions)[0]
            if heading == 'n':
                y += 1
            elif heading == 'e':
                x += 1
            elif heading == 'w':
                x -= 1
            elif heading == 's':
                y -= 1
        coordinates.append((x, y))

    for coord in coordinates:
        distances.append(calc_distance((0, 0), coord))

    print(f"Pa random walk of {walk_length}\n"
          f"Mean {round(stat.fmean(distances), 1)} CV {round(stat.stdev(distances) / stat.fmean(distances), 1)}\n"
          f"Max {round(max(distances), 1)} Min {round(min(distances), 1)}")

    return coordinates


def ma(walk_length, trials):
    coordinates = []
    distances = []
    directions = ['n', 'e', 's', 's', 'w']
    for _ in range(trials):
        x = 0
        y = 0
        for _ in range(walk_length):
            heading = random.choice(directions)[0]
            if heading == 'n':
                y += 1
            elif heading == 'e':
                x += 1
            elif heading == 'w':
                x -= 1
            elif heading == 's':
                y -= 1
        coordinates.append((x, y))
    for coord in coordinates:
        distances.append(calc_distance((0, 0), coord))
    print(f"Mi-Ma random walk of {walk_length}\n"
          f"Mean {round(stat.fmean(distances), 1)} CV {round(stat.stdev(distances) / stat.fmean(distances), 1)}\n"
          f"Max {round(max(distances), 1)} Min {round(min(distances), 1)}")

    return coordinates


def reg(walk_length, trials):
    coordinates = []
    distances = []
    directions = ['e', 'w']
    for _ in range(trials):
        x = 0
        y = 0
        for _ in range(walk_length):
            heading = random.choice(directions)
            if heading == 'e':
                x += 1
            elif heading == 'w':
                x -= 1
        coordinates.append((x, y))
    for coord in coordinates:
        distances.append(calc_distance((0, 0), coord))

    print(f"Reg random walk of {walk_length}\n"
          f"Mean {round(stat.fmean(distances), 1)} CV {round(stat.stdev(distances) / stat.fmean(distances), 1)}\n"
          f"Max {round(max(distances), 1)} Min {round(min(distances), 1)}")

    return coordinates


# Scale arg makes plot larger and easier to visualize. Larger numbers make the plot larger
def map_on_turtles(pa_coords, ma_coords, reg_coords, scale):

    t.hideturtle()
    t.speed('fastest')
    dot_size = 2 * scale

    for coord in pa_coords:
        x = coord[0] * scale
        y = coord[1] * scale
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(dot_size, 'black')

    for coord in ma_coords:
        x = coord[0] * scale
        y = coord[1] * scale
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(dot_size, 'red')

    for coord in reg_coords:
        x = coord[0] * scale
        y = coord[1] * scale
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.dot(dot_size, 'green')
    t.mainloop()


def main():
    walk_lengths = []

    args = sys.argv
    args.pop(0)  # get rid of the 'randomWalk.py' value

    try:

        if ',' not in args[0]:
            print("Walk lengths must be a comma separated list. Example: 1,2,3,4")
            return

        walk_lengths_in = args[0].split(",")
        for walk_length in walk_lengths_in:
            walk_lengths.append(int(walk_length.strip(" ")))

    except ValueError:
        print("Walk lengths must be integers")
        return

    try:
        trials = int(args[1])
    except ValueError:
        print("Number of trials must be an integer")
        return

    walk_type = args[2]

    if walk_type == 'pa':
        pa(walk_lengths[0], trials)
        pa(walk_lengths[1], trials)
    elif walk_type == 'ma':
        ma(walk_lengths[0], trials)
        ma(walk_lengths[1], trials)
    elif walk_type == 'reg':
        reg(walk_lengths[0], trials)
        reg(walk_lengths[1], trials)
    elif walk_type == 'all':
        pa_coords = pa(walk_lengths[0], trials)
        pa(walk_lengths[1], trials)
        ma_coords = ma(walk_lengths[0], trials)
        ma(walk_lengths[1], trials)
        reg_coords = reg(walk_lengths[0], trials)
        reg(walk_lengths[1], trials)
        map_on_turtles(pa_coords, ma_coords, reg_coords, 4)
    else:
        print("Walk type must be \'pa\', \'ma\', \'reg\', or \'all\'")


if __name__ == '__main__':
    main()

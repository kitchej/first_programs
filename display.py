import os
import subprocess as sp
import time

"""
--------------------------------------------------
Display - V.1.0 - Written by Joshua Kitchen 5/21/2020
--------------------------------------------------
"""


class Display:
    def __init__(self, rows, columns, background=" "):
        self.columns = columns
        self.row_count = rows
        self.rows = [[] for _ in range(self.row_count)]
        self.x_movement = "right"
        self.y_movement = "up"
        self.offset_counter = 0
        self.background = background

        for i in range(self.columns):
            for row in self.rows:
                row.append(self.background)

    @staticmethod
    def clear_terminal():
        if os.name == 'nt':
            sp.call("cls", shell=True)
        else:
            sp.call("clear", shell=True)

    def draw(self, posy, posx, char):
        try:
            self.rows[posy][posx] = char
        except IndexError:
            print(f'Coordinates Y: {posy} X: {posx} are out of bounds.\n'
                  f'Display size is {len(self.rows)} X {self.columns}')
            return

    def clear_display(self):
        self.clear_terminal()
        self.rows = []
        self.rows = [[] for _ in range(self.row_count)]
        for i in range(self.columns):
            for row in self.rows:
                row.append(self.background)

    def show(self):
        for row in self.rows:
            print(*row)
            
    # Examples: animating text

    def up_and_down(self, text, speed, frames, justify='center'):
        if len(text) > self.columns:
            print(f"Selected String cannot fit in the current display size.\n"
                  f"Size of string: {len(text)}\n"
                  f"Size of display: 5 rows X {self.columns} columns")
            return
        
        self.clear_display()
        self.y_movement = "up"
        coords = []
        y = len(self.rows) / 2
        y = int(round(y, 1))
        if justify == 'left':
            x = 0
        elif justify == 'right':
            x = self.columns - len(text)
        elif justify == 'center':
            x = (self.columns - len(text)) / 2
            x = int(round(x, 1))
        else:
            print(f"Invalid argument: {justify}. Must be \'center\', \'left\' or \'right\'")
            return
        for char in text:
            self.draw(y, x, char)
            coords.append([y, x, char])
            x += 1

        self.show()

        count = 0
        while count < frames:
            time.sleep(speed)
            self.clear_display()
            if coords[0][0] == 0:
                self.y_movement = "down"
            elif coords[0][0] == self.row_count - 1:
                self.y_movement = "up"

            for i in range(len(coords)):
                if i > self.offset_counter:
                    pass
                else:
                    if self.y_movement == "up":
                        coords[i][0] = coords[i][0] - 1
                    elif self.y_movement == "down":
                        coords[i][0] = coords[i][0] + 1
                    self.draw(coords[i][0], coords[i][1], coords[i][2])
                self.offset_counter += 1
            self.show()
            count += 1

    def side_to_side(self, text, speed, frames, start_pos='center'):
        if len(text) > self.columns:
            print(f"Selected String cannot fit in the current display size.\n"
                  f"Size of string: {len(text)}\n"
                  f"Size of display: 5 rows X {self.columns} columns")
            return
        
        self.clear_display()
        self.x_movement = "left"
        coords = []
        if start_pos == 'top':
            y = 0
        elif start_pos == 'bottom':
            y = self.row_count - 1
        elif start_pos == 'center':
            y = len(self.rows) / 2
            y = int(round(y, 1))
        else:
            print(f"Invalid argument: {start_pos}. Must be \'center\', \'top\' or \'bottom\'")
            return
        x = (self.columns - len(text)) / 2
        x = int(round(x, 1))
        for char in text:
            self.draw(y, x, char)
            coords.append([y, x, char])
            x += 1
        self.show()

        count = 0
        while count < frames:
            time.sleep(speed)
            self.clear_display()
            if coords[0][1] == 0:
                self.x_movement = "right"
            elif coords[-1][1] == self.columns - 1:
                self.x_movement = "left"
            if self.x_movement == "right":
                for i in range(len(coords)):
                    coords[i][1] = coords[i][1] + 1
                    self.draw(coords[i][0], coords[i][1], coords[i][2])
            elif self.x_movement == "left":
                for i in range(len(coords)):
                    coords[i][1] = coords[i][1] - 1
                    self.draw(coords[i][0], coords[i][1], coords[i][2])
            self.show()
            count += 1

    def wavy_text(self, text, speed, frames):
        if len(text) > self.columns:
            print(f"Selected String cannot fit in the current display size.\n"
                  f"Size of string: {len(text)}\n"
                  f"Size of display: 5 rows X {self.columns} columns")
            return
        
        self.clear_display()
        self.offset_counter = 1
        coords = []
        y = len(self.rows) / 2
        y = int(round(y, 1))
        x = (self.columns - len(text)) / 2
        x = int(round(x, 1))
        for char in text:
            self.draw(y, x, char)
            coords.append([y, x, char, "up"])
            """                         ^   
                        direction of character (up or down"""
            x += 1
        self.show()

        count = 0
        while frames > count:
            time.sleep(speed)
            self.clear_display()
            for i in range(len(coords)):
                if i < self.offset_counter:
                    if coords[i][0] == 0:
                        coords[i][3] = "down"
                    elif coords[i][0] == self.row_count - 1:
                        coords[i][3] = "up"
                    if coords[i][3] == "up":
                        coords[i][0] = coords[i][0] - 1
                    elif coords[i][3] == "down":
                        coords[i][0] = coords[i][0] + 1
                else:
                    pass

                self.draw(coords[i][0], coords[i][1], coords[i][2])
            self.offset_counter += 1
            self.show()
            count += 1

    def scroll_in_horiz(self, text, speed, stop=None):
        if len(text) > self.columns:
            print(f"Selected String cannot fit in the current display size.\n"
                  f"Size of string: {len(text)}\n"
                  f"Size of display: 5 rows X {self.columns} columns")
            return
        
        self.clear_display()
        self.x_movement = "right"
        if stop is None:
            stop = self.columns - 1
        else:
            if stop > self.columns - 1:
                print(f'Stopping point: {stop} is greater than column count: {self.columns - 1}')
        coords = []
        y = len(self.rows) / 2
        y = int(round(y, 1))
        for char in text:
            coords.append([None, char])
            """           ^   
                        x_pos """
        self.offset_counter = -2
        self.show()
        while True:
            try:
                if coords[0][0] > stop:
                    break
            except TypeError:
                pass
            time.sleep(speed)
            self.clear_display()
            i = -1
            for _ in range(len(coords)):
                if i > self.offset_counter:
                    if coords[i][0] is None:
                        coords[i][0] = 0
                    else:
                        coords[i][0] += 1
                    if coords[i][0] >= self.columns:
                        pass
                    else:
                        self.draw(y, coords[i][0], coords[i][1])
                else:
                    pass
                i -= 1
            self.offset_counter -= 1
            self.show()

    def scroll_in_vert(self, text, speed, stop=None, justify='center'):
        if len(text) > self.columns:
            print(f"Selected String cannot fit in the current display size.\n"
                  f"Size of string: {len(text)}\n"
                  f"Size of display: 5 rows X {self.columns} columns")
            return
        
        self.clear_display()
        self.x_movement = "right"
        self.offset_counter = 0
        if stop is None:
            stop = self.row_count - 1
        coords = []
        if justify == 'left':
            x = 0
        elif justify == 'right':
            x = self.columns - len(text)
        elif justify == 'center':
            x = (self.columns - len(text)) / 2
            x = int(round(x, 1))
        else:
            print(f"Invalid argument: {justify}. Must be \'center\', \'left\' or \'right\'")
            return
        for char in text:
            coords.append([0, x, char])
            x += 1
        self.show()
        while True:
            if coords[0][0] == stop:
                break
            time.sleep(speed)
            
            self.clear_display()
            for i in range(len(coords)):
                coords[i][0] = coords[i][0] + 1
                self.draw(coords[i][0], coords[i][1], coords[i][2])
            self.show()


if __name__ == '__main__':
    screen = Display(7, 20)
    screen.scroll_in_horiz('Hello World', 0.1)
    screen.scroll_in_vert('Hello World', 0.1, 3)
    time.sleep(0.2)
    screen.side_to_side('Hello World', 0.1, 18)
    screen.up_and_down('Hello World', 0.1, 12)
    screen.wavy_text('Hello World', 0.1, 35)

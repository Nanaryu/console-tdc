from console_utils import colorize, slowprint
from secrets import randbelow
from random import shuffle
import msvcrt
from os import system



class Display:

    w = colorize("██", '#000')
    p = colorize("██", '#00f')
    e = "  "
    x = colorize("██", '#0f0')
    v = colorize("██", '#f00')

    def __init__(self):
        self.w = colorize("██", '#000')
        self.p = colorize("██", '#00f')
        self.e = "  "
        self.x = colorize("██", '#0f0')
        self.v = colorize("██", '#f00')

    def create_table(self, char):
        display = []
        for _ in range(25):
            dist = []
            for _ in range(49):
                dist.append(char)
            display.append(dist)
        return display

    def refresh(self, display):
        for row in display:
            for cell in row:
                print(cell, end="")
            print("")

    def generate_room(self):
        w = self.w
        p = self.p
        e = self.e
        x = self.x
        v = self.v
        room = []
        while len(room) != 15:
            row = []
            while len(row) != 15:
                r = randbelow(50)
                if len(room) == 0 or len(room) == 14:
                    if r == 0:
                        row.append([w, w, w, w, w, w, w, w, w, x, x, x, x, w])
                    elif r == 25:
                        row.append([w, x, x, x, x, w, w, w, w, w, w, w, w, w])
                    else:
                        row.append([w, w, w, w, w, x, x, x, x, w, w, w, w, w])
                else:
                    c = [e, w, v]
                    shuffle(c)
                    row.append([c[0], c[1], c[2], c[1], c[0], c[0], c[2], c[2], c[0], c[0], c[1], c[0], c[1], c[0]])    
            room.append(row)
        return room

    room1 = [
    [w, w, w, w, w, x, x, x, x, x, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]
    room2 = [
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, x, x, x, x, x, w, w, w, w, w]]

    roomlist = [room1, room2]

class Game:
    def __init__(self):
        self.w = colorize("██", '#000')
        self.p = colorize("██", '#00f')
        self.e = "  "
        self.x = colorize("██", '#0f0')
        self.v = colorize("██", '#f00')

    def reset(self, room):
        p = self.p
        v = self.v
        e = self.e
        for row in room:
            for element in row:
                if element == p or element == v:
                    room[room.index(row)][row.index(element)] = e
        room[7][7] = p
        return room

    

    def spawn_enemies(self, room):
        e = self.e
        v = self.v
        for row in room:
            for element in row:
                if element == e:
                    if randbelow(50) == 0:
                        room[room.index(row)][row.index(element)] = v
                    else:
                        pass
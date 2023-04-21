from os import system
import msvcrt
from time import sleep
import colorama
from colorama import Fore
from secrets import randbelow

colorama.init()

w = Fore.BLACK + "■ "
p = Fore.CYAN + "■ "
e = "  "
x = Fore.GREEN + "■ "
v = Fore.RED + "■ " 

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
    [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]
]

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
    [w, w, w, w, w, x, x, x, x, x, w, w, w, w, w]
]

roomlist = [room1, room2]

c_room = roomlist[0]
p_cpos = (7, 7)
px = p_cpos[0]
py = p_cpos[1]

def show_room(room):
    for row in room:
        for x in row:
            print(x, end='')
        print("")

def reset(room):
    global e
    global v
    for row in room:
        for element in row:
            if element == p or element == v:
                room[room.index(row)][row.index(element)] = e
    room[7][7] = p

def game_handler(room):
    global c_room
    global px
    global py
    global v
    global e
    if msvcrt.kbhit():
        key = msvcrt.getch() 
        if key == b'w':
            if px > 0 and c_room[px - 1][py] != w:
                c_room[px][py] = e
                c_room[px - 1][py] = p
                px -= 1
                if c_room[px - 1][py] == x:
                    reset(c_room)
                    c_room = roomlist[randbelow(len(roomlist) - 1)]
                    spawn_enemies(c_room)
                    px = 7
                    py = 7
                system('cls')
                show_room(c_room)

        elif key == b's':
            if px < 14 and c_room[px + 1][py] != w:
                c_room[px][py] = e
                c_room[px + 1][py] = p
                px += 1
                if c_room[px + 1][py] == x:
                    reset(c_room)
                    c_room = roomlist[randbelow(len(roomlist) - 1)]
                    spawn_enemies(c_room)
                    px = 7
                    py = 7
                system('cls')
                show_room(c_room)

        elif key == b'a':
            if py > 0 and c_room[px][py - 1] != w:
                c_room[px][py] = e
                c_room[px][py - 1] = p
                py -= 1
                if c_room[px][py - 1] == x:
                    reset(c_room)
                    c_room = roomlist[randbelow(len(roomlist) - 1)]
                    spawn_enemies(c_room)
                    px = 7
                    py = 7
                system('cls')
                show_room(c_room)

        elif key == b'd':
            if py < 14 and c_room[px][py + 1] != w:
                c_room[px][py] = e
                c_room[px][py + 1] = p
                py += 1
                if c_room[px][py + 1] == x:
                    reset(c_room)
                    c_room = roomlist[randbelow(len(roomlist) - 1)]
                    spawn_enemies(c_room)
                    px = 7
                    py = 7
                system('cls')
                show_room(c_room)
        for row in c_room:
            for element in row:
                if element == v:
                    if row.index(element) < py:
                        room[room.index(row)][row.index(element)] = e
                        room[room.index(row)][row.index(element) + 1] = v
                    elif row.index(element) > py:
                        room[room.index(row)][row.index(element)] = e
                        room[room.index(row)][row.index(element) - 1] = v

def spawn_enemies(room):
    global e
    global v
    for row in room:
        for element in row:
            if element == e:
                if randbelow(50) == 0:
                    room[room.index(row)][row.index(element)] = v
                else:
                    pass


c_room[px][py] = p
show_room(c_room)

while True: 
    game_handler(c_room)
    
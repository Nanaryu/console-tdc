from os import system
import msvcrt
from time import sleep
from console_utils import colorize, slowprint
from secrets import randbelow
from display import Display, Game



w = colorize("██", '#000')
p = colorize("██", '#00f')
e = "  "
x = colorize("██", '#0f0')
v = colorize("██", '#f00')

display = Display()
game = Game()

c_room = display.roomlist[0]
p_cpos = (7, 7)

px = p_cpos[0]
py = p_cpos[1]

def game_handler(room):
    global c_room
    global px
    global py
    reset = game.reset
    spawn_enemies = game.spawn_enemies
    show_room = display.refresh
    roomlist = display.roomlist

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


c_room[px][py] = p
display.refresh(c_room)

while True: 
    game_handler(c_room)
    
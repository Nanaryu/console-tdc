from os import system
import msvcrt
from time import sleep
import colorama
from colorama import Fore
colorama.init()

w = Fore.BLACK + "██"
p = Fore.CYAN + "██"
e = "  "
x = Fore.GREEN + "▒▒"

room1 = [
    [w, w, w, w, w, x, x, x, x, x, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, p, e, e, e, e, e, e, x],
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
    [x, e, e, e, e, e, e, p, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [x, e, e, e, e, e, e, e, e, e, e, e, e, e, x],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, e, e, e, e, e, w, w, w, w, w],
    [w, w, w, w, w, x, x, x, x, x, w, w, w, w, w]
]

c_room = room1

def show_room(room):
    for row in room:
        for x in row:
            print(x, end='')
        print("")

def load_room(room):
    current_room = room
    return current_room

def move_handle(room):
    '''
    if msvcrt.kbhit():
        key = msvcrt.getch() 
        if key == b'w': 
            for row in room:
                for element in row:
                    if element == p:
                        if room.index(row) - 1 == 0:
                            load_room(2)
                        else:
                            room[room.index(row) - 1][row.index(element)] = p
                            row[row.index(p)] = e
                    else:
                        pass
    '''
    pass

while True: 
    move_handle(c_room)
    if msvcrt.kbhit():
        key = msvcrt.getch() 
        if key == b'w': 
            for row in c_room:
                for element in row:
                    if element == p:
                        if c_room.index(row) - 1 == 0:
                            load_room(room2)
                        else:
                            c_room[c_room.index(row) - 1][row.index(element)] = p
                            row[row.index(p)] = e
                    else:
                        pass
    show_room(c_room)
    sleep(0.1)
    system('cls')
    

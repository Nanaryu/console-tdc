from console_utils import colorize, slowprint
from secrets import randbelow
from random import shuffle
from os import system

hori = colorize("═", '#adff09')
vert = colorize("║", '#adff09')
veri = colorize("╔", '#adff09')
hodo = colorize("╗", '#adff09')
doho = colorize("╝", '#adff09')
hove = colorize("╚", '#adff09')

def draw_box(text, color="#adff09", selected=False):
    print(veri + (hori*len(text)) + hodo)
    if selected == False:
        print(vert + colorize(text, color) + vert)
    else:
        print(vert + colorize(text, '#ffad09') + vert)
    print(hove + (hori*len(text)) + doho)

def draw_box2(text, text2, color="#adff09", selected=1):
    print(veri + (hori*len(text)) + hodo + "   " + veri + (hori*len(text2)) + hodo)
    if selected==1:
        print(vert + colorize(text,'#ffad09') + vert + "   " + vert + colorize(text2, color) + vert)
    elif selected==2:
        print(vert + colorize(text, color) + vert + "   " + vert + colorize(text2, '#ffad09') + vert)
    print(hove + (hori*len(text)) + doho + "   " + hove + (hori*len(text2)) + doho)

def draw_box3(text, text2, color1="#00ad00", color2="#ad0000"):
    print(veri + (hori*len(text)) + hodo + "   " + veri + (hori*len(text2)) + hodo)
    print(vert + colorize(text, color1) + vert + "   " + vert + colorize(text2, color2) + vert)
    print(hove + (hori*len(text)) + doho + "   " + hove + (hori*len(text2)) + doho)

def draw_box_for_stats(text, length, text2, length2):
    if len(length) > len(length2):
        print(veri + (hori*(len(length)+2)) + hodo)
        print(vert + colorize(text, '#ffffff') + vert)
        print(vert + colorize(text2, '#ffffff') + " "*(len(length)-len(length2)) + vert)
        print(hove + (hori*(len(length)+2)) + doho)
    else:
        print(veri + (hori*(len(length2)+2)) + hodo)
        print(vert + colorize(text, '#ffffff') + " "*(len(length2)-len(length)) + vert)
        print(vert + colorize(text2, '#ffffff') + vert)
        print(hove + (hori*(len(length2)+2)) + doho)


def attack(combatpower, edefense, ehealth):
    return (ehealth - (combatpower-edefense-randbelow(combatpower//10)))

def defend(defense, health):
    return (defense + (health//32))

def enemyattack(ecombatpower, health, defense):
    return (health - (ecombatpower-defense-randbelow(ecombatpower//5)+randbelow(ecombatpower//2)))

def enemydefend(edefense, ehealth):
    return (edefense + (ehealth//128))

def display(pokemon1, pokemon2, defense, combatpower, health, edefense, ecombatpower, ehealth, attack=0, defend=0, eattack=0, edefend=0, start=False, selected=1, change=False):
    system('cls')
    if start:
        draw_box3(f'  You choose {pokemon1}!  ', f'  A wild {pokemon2} appeared!  ')
    else:
        if not change:
            if attack != 0 and eattack != 0:
                draw_box3(f'  {pokemon1} attacked {pokemon2} for {attack} damage!  ', f' In exchange, {pokemon1} got hit by {eattack} damage from {pokemon2}!  ')
            elif attack != 0 and  edefend != 0:
                draw_box3(f'  {pokemon1} attacked {pokemon2} for {attack} damage!  ', f' Instead of attacking {pokemon1}, {pokemon2} boosted its defense by {edefend}!  ')
            elif defend != 0 and edefend != 0:
                draw_box3(f'  Instead of attacking {pokemon2}, {pokemon1} boosted its defense by {defend}!  ', f'  Instead of attacking {pokemon1}, {pokemon2} boosted his defense by {edefend}!  ')
            elif defend != 0 and eattack != 0:
                draw_box3(f'  Instead of attacking {pokemon2}, {pokemon1} boosted its defense by {defend}!  ', f' Because of this, {pokemon1} was struck by {eattack} damage from {pokemon2}!  ')
        else:
            draw_box3(f'  {pokemon1} prepares his move.  ', f'  {pokemon2} waits for your turn.  ')

    draw_box_for_stats(f'  {colorize(pokemon1, "#00af00")}:  Defense: {colorize(defense, "#3d9eff")}  Combat Power: {colorize(combatpower, "#ff3d3d")}  Health: {colorize(health, "#00af00")}  ',"  " + str(pokemon1) +  ":  Defense: " + str(defense) + " Combat Power: " + str(combatpower) + " Health: " + str(health) + "  ", f'  {colorize(pokemon2, "#ff3d3d")}:  Defense: {colorize(edefense, "#3d9eff")}  Combat Power: {colorize(ecombatpower, "#ff3d3d")}  Health: {colorize(ehealth, "#00af00")}  ',"  " + str(pokemon2) + ":  Defense: " + str(edefense) + " Combat Power: " + str(ecombatpower) + " Health: " + str(ehealth) + "  ")
    draw_box2("  Attack  ", "  Defend  ", "#adff09", selected)



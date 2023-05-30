from os import system
import msvcrt
from time import sleep
from console_utils import colorize, slowprint
from secrets import randbelow
from display import display, attack, defend, enemyattack, enemydefend, draw_box

pokemons = ["Bulbasaur", "Wartortle", "Charizard", "Dragonite", "Tyranitar", "Sableye", "Blissey", "Snorlax", "Cubchoo", "Squirtle", "Scizor"]
enemy = pokemons[randbelow(len(pokemons))]
edefense = randbelow(50)+50
ecombatpower = randbelow(200)+200
ehealth = randbelow(800)+800


pokemon = pokemons[randbelow(len(pokemons))]
defense = randbelow(50)+50
combatpower = randbelow(200)+200
health = randbelow(800)+800

selected = 1

dice = 0

display(pokemon, enemy, defense, combatpower, health, start=True, selected=1, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
while True:
    if health < 0:
        system('cls')
        draw_box("  Game over. You have lost.  ", "#ad0000")
        break
    if ehealth < 0:
        system('cls')
        draw_box("  Game over. You have won!  ", "#00ad00")
        break
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key==b'c':
            if selected == 1:
                ehealth = attack(combatpower, edefense, ehealth)
                sleep(1)
                dice = randbelow(2)
                if dice == 1:
                    health = enemyattack(ecombatpower, defense, health)
                    display(pokemon, enemy, defense, combatpower, health, attack=combatpower-edefense-randbelow(combatpower//10), eattack=ecombatpower-defense-randbelow(ecombatpower//5)+randbelow(ecombatpower//2), selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
                else:
                    edefense = enemydefend(edefense, ehealth)
                    display(pokemon, enemy, defense, combatpower, health, attack=combatpower-edefense-randbelow(combatpower//10), edefend=ehealth//128, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
            elif selected == 2:
                defense = defend(defense, health)
                sleep(1)
                dice = randbelow(2)
                if dice == 1:
                    health = enemyattack(ecombatpower, defense, health)
                    display(pokemon, enemy, defense, combatpower, health, defend=health//32, eattack=ecombatpower-defense-randbelow(ecombatpower//5)+randbelow(ecombatpower//2), selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
                else:
                    edefense = enemydefend(edefense, ehealth)
                    display(pokemon, enemy, defense, combatpower, health, defend=health//32, edefend=ehealth//128, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
        elif key==b'a':
            selected = 1
            display(pokemon, enemy, defense, combatpower, health, change=True, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
        elif key==b'd':
            selected = 2 
            display(pokemon, enemy, defense, combatpower, health, change=True, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
            

       
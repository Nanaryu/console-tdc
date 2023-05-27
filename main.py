from os import system
import msvcrt
from time import sleep
from console_utils import colorize, slowprint
from secrets import randbelow
from display import display, attack, defend

pokemons = ["Bulbasaur", "Wartortle", "Charizard", "Dragonite", "Tyranitar", "Sableye", "Blissey", "Snorlax"]
enemy = pokemons[randbelow(len(pokemons))]
edefense = 100
ecombatpower = 150
ehealth = 350


pokemon = "Charizard"
defense = 50
combatpower = 200
health = 300

selected = 1

display(pokemon, enemy, defense, combatpower, health, start=True, selected=1, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key==b'c':
            if selected == 1:
                ehealth = attack(combatpower, edefense, ehealth)
                display(pokemon, enemy, defense, combatpower, health, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
            elif selected == 2:
                defense = defend(defense, health)
                display(pokemon, enemy, defense, combatpower, health, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
        elif key==b'a':
            selected = 1
            display(pokemon, enemy, defense, combatpower, health, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
        elif key==b'd':
            selected = 2 
            display(pokemon, enemy, defense, combatpower, health, selected=selected, edefense=edefense, ecombatpower=ecombatpower, ehealth=ehealth)
            
       
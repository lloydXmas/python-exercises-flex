#!/usr/bin/env python

import random
class Character:
    def __init__(self):
        self.name = None
        self.health = health
        self.power = power
        self.coins = coins

    def alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.dmg_received(self.power)

    def dmg_received(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

    def print_status(self):
        print("{} has {} health and {} power.".format(self.name, self.health, self.power))

class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 0

    def attack(self, enemy):
        if random.randint(1, 5) == 1: #1 in 5 (20%) chance to double dmg
            self.power *= 2
            print("Hero deals double damage!")
            enemy.dmg_received(self.power)
        else:
            print("{} attacks {}".format(self.name, enemy.name))
            enemy.dmg_received(self.power)
        if enemy.health <= 0:
            self.coins += enemy.coins
            print("You received {} coins.".format(enemy.coins))

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2
        self.coins = 5

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 10
        self.power = 3
        self.coins = 8

    def dmg_received(self, points):
        print("{} received {} damage, but the zombie is unkillable.".format(self.name, points))

class Medic(Character):
    def __init__(self):
        self.name = 'medic'
        self.health = 11
        self.power = 2
        self.coins = 7

    def dmg_received(self, points):
        self.health -= points
        print("{} received {} damage.".format(self.name, points))
        if random.randint(1, 5) == 1: #1 in 5 (20%) chance to heal
            self.health += 2
            if self.health > 0:
                print("The medic heals himself!")
        if self.health <= 0:
            print("{} is dead.".format(self.name))


class Shadow(Character):
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 3
        self.coins = 8

    def dmg_received(self, points):
        if random.randint(1, 10) == 1: #1 in 10 chance to be hit
            self.health -= self.points
            print("{} received {} damage.".format(self.name, points))
        else:
            print("{} evades the attack.".format(self.name))
        if self.health <= 0:
            print("{} is dead.".format(self.name))

class Giant(Character): #Giant has 50% chance to deal 2x - 3x dmg
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 3
        self.coins = 10

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        if random.randint(1, 2) == 1:
            self.power *= random.randint(2, 3)
            print("{} attacks {} with crushing power.".format(self.name, enemy.name))
            enemy.dmg_received(self.power)
        else:
            print("{} attacks {}".format(self.name, enemy.name))
            enemy.dmg_received(self.power)

class Rogue(Character): #Rogue has 20% chance to land an additional attack
    def __init__(self):
        self.name = 'shadow'
        self.health = 1
        self.power = 3
        self.coins = 8

    def attack(self, enemy):
        if random.randint(1, 5) == 1:
            self.power *= 2
            print("{} double attacks {}.".format(self.name, enemy.name))
            enemy.dmg_received(self.power)
        else:
            print("{} attacks {}".format(self.name, enemy.name))
            enemy.dmg_received(self.power)

def display_menu():
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. fight zombie")
    print("3. fight medic")
    print("4. fight shadow")
    print("5. fight giant")
    print("6. fight rogue")
    print("7. do nothing")
    print("8. flee")
    print("> ", end=' ')
    raw_input = input()
    return raw_input

def main():
    goblin_fight = False
    zombie_fight = False
    medic_fight = False
    shadow_fight = False
    giant_fight = False
    rogue_fight = False

    hero = Hero()
    goblin = Goblin()
    zombie = Zombie()
    medic = Medic()
    shadow = Shadow()
    giant = Giant()
    rogue = Rogue()

    while hero.alive() and goblin.alive() and zombie.alive() and medic.alive() and shadow.alive() and giant.alive() and rogue.alive():
        print("The hero has {} health and {} power.".format(hero.health, hero.power))
        print()
        print("The goblin has {} health and {} power.".format(
            goblin.health, goblin.power))
        print("The zombie has {} health and {} power.".format(
            zombie.health, zombie.power))
        print("The medic has {} health and {} power.".format(
            medic.health, medic.power))
        print("The shadow has {} health and {} power.".format(
            shadow.health, shadow.power))
        print("The giant has {} health and {} power.".format(
            shadow.health, shadow.power))
        print("The rogue has {} health and {} power.".format(
            shadow.health, shadow.power))

        action = display_menu()

        if action == "1":
            # Hero attacks goblin
            goblin_fight = True
            hero.attack(goblin)
            if goblin.alive():
                goblin.print_status()
        elif action == "2":
            # Hero attacks zombie
            zombie_fight = True
            hero.attack(zombie)
        elif action == "3":
            # Hero attacks medic
            medic_fight = True
            hero.attack(medic)
            if medic.alive():
                medic.print_status()
        elif action == "4":
            # Hero attacks shadow
            shadow_fight = True
            hero.attack(shadow)
            if shadow.alive():
                shadow.print_status()
        elif action == "5":
            # Hero attacks giant
            giant_fight = True
            hero.attack(giant)
            if giant.alive():
                giant.print_status()
        elif action == "6":
            # Hero attacks rogue
            rogue_fight = True
            hero.attack(rogue)
            if rogue.alive():
                rogue.print_status()
        elif action == "7":
            pass
        elif action == "8":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(action))

        if goblin.health > 0 and goblin_fight:
            # Goblin is fighting hero
            goblin.attack(hero)
            hero.print_status()
        elif zombie.health > 0 and zombie_fight:
            # Zombie fighting hero
            zombie.attack(hero)
            hero.print_status()
        elif medic.health > 0 and medic_fight:
            # Medic fighting hero
            medic.attack(hero)
            hero.print_status()
        elif shadow.health > 0 and shadow_fight:
            # Shadow fighting hero
            shadow.attack(hero)
            hero.print_status()
        elif giant.health > 0 and giant_fight:
            # Giant fighting hero
            giant.attack(hero)
            hero.print_status()
        elif rogue.health > 0 and rogue_fight:
            # Rogue fighting hero
            rogue.attack(hero)
            hero.print_status()

main()

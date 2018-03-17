#!/usr/bin/env python3

import random
import time

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.coins = 20

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("{} attacks {}".format(self.name, enemy.name))
        enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
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
        self.coins = 20
        self.armor = 0
        self.evade = 0
        self.crit = 0
        self.magic = 0

    def restore(self):
        self.health = 10
        print("Hero's heath is restored to {}!".format(self.health))
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)

    def receive_damage(self, points):
        if self.evade >= 10:
            self.evade = 10
        hit_chance = random.randint(self.evade, 12)
        if hit_chance == 12:
            print("{} evades damage!".format(self.name))
        else:

            if points > self.armor: #received more dmg than armor
                points -= self.armor
                print("{} received {} damage, armor mitigated {} points ".format(self.name, points, self.armor))
                self.health -= points
                self.armor = 0
            else:  #received less dmg than armor
                self.armor -= points
                print("{} received {} damage, armor points remaining: {} ".format(self.name, points, self.armor))

            if self.health <= 0:
                print("{} is dead.".format(self.name))

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 6
        self.power = 2

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("{} swaps power with {} during attack".format(self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Battle(object):
    def do_battle(self, hero, enemy):
        print("=====================")
        print("Hero faces the {}".format(enemy.name))
        print("=====================")
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight {}".format(enemy.name))
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            keyinput = int(input())
            if keyinput == 1:
                hero.attack(enemy)
            elif keyinput == 2:
                pass
            elif keyinput == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input {}".format(input))
                continue
            enemy.attack(hero)
        if hero.alive():
            print("You defeated the {}".format(enemy.name))
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("{}'s health increased to {}.".format(character.name, character.health))

class SuperTonic(object):
    cost = 14
    name = 'super tonic'
    def apply(self, character):
        character.health = 10
        print("{}'s health is restored to {}.".format(character.name, character.health))

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print("{}'s power increased to {}.".format(hero.name, hero.power))

class Armor(object):
    cost = 5
    name = 'armor'
    def apply(self, hero):
        hero.armor += 2
        print("{}'s armor increased to {}.".format(hero.name, hero.armor))

class Evade(object):
    cost = 5
    name = 'evade'
    def apply(self, hero):
        hero.evade += 2
        print("{}'s evade increased to {}.".format(hero.name, hero.evade))

class MagicScroll(object):
    cost = 10
    name = 'magic'
    def apply(self, hero):
        ability = random.choice(['none', hero.health, hero.armor, hero.power])
        if ability == 'none':
            print("Magic Scroll was empty.")
        else:
            ability += random.randint(4,10)
            print("{}'s evade increased to {}.".format(hero.name, ability))

class Axe(object):
    cost = 20
    name = 'axe'
    def apply(self, hero):
        hero.power += random.randint(2,10)
        print("{}'s power increased to {}.".format(hero.name, hero.power))


class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, Sword, Armor, Evade, Axe, MagicScroll]
    def do_shopping(self, hero):
        while hero.coins > 0:
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have {} coins.".format(hero.coins))
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("{}. buy {} ({})".format(i + 1, item.name, item.cost))
            print("10. leave")
            print("> ", end=' ')
            shopinput = int(input())
            if shopinput == 10:
                break
            else:
                ItemToBuy = Store.items[shopinput - 1]
                item = ItemToBuy()
                hero.buy(item)

if __name__ == "__main__":
    hero = Hero()
    enemies = [Goblin(), Wizard()]
    battle_engine = Battle()
    shopping_engine = Store()

    for enemy in enemies:
        hero_won = battle_engine.do_battle(hero, enemy)
        if not hero_won:
            print("YOU LOSE!")
            exit(0)
        shopping_engine.do_shopping(hero)

    print("YOU WIN!")

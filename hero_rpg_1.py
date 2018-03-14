#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
  def __init__ (self, name, health, power):
    self.name = name
    self.health = health
    self.power = power
    
  def alive(self):
    if self.health > 0:
      return True
    else:
      return False
  
  def attack (self, enemy):
    if self.name == 'hero' and enemy.name == 'goblin':
      print("You do {} damage to the goblin.".format(self.power))
    
    if self.name == 'hero' and enemy.name == 'zombie':
      print("You do {} damage to the zombie.".format(self.power))

    elif self.name == 'goblin':
      print("The goblin does {} damage to you.".format(self.power))
  
  def print_status(self):
    if self.health <= 0 and self.name == 'hero':
      print("You are dead.")
    elif self.health <= 0 and self.name == 'goblin':
      print("The goblin is dead.")

    
class Hero(Character):
  pass

    
class Goblin(Character):
  pass


class Zombie(Character):
  pass


def main():
    goblin_fight = False
    zombie_fight = False
    hero = Hero(name='hero', health=10, power=5)
    goblin = Goblin(name='goblin', health=6, power=2)
    zombie = Zombie(name='zombie', health=19, power=3)
    while ((goblin.alive() and hero.alive()) and (zombie.alive() and hero.alive())):
        print("You have {} health and {} power.".format(hero.health, hero.power))
        print("The goblin has {} health and {} power.".format(goblin.health, goblin.power))
        print("The zombie has {} health and {} power.".format(zombie.health, zombie.power))

        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zombie")
        print("3. do nothing")
        print("4. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            goblin_fight = True
            hero.attack(goblin)
            goblin.health -= hero.power
            goblin.print_status()
        
        elif raw_input == "2":
            # Hero attacks zombie
            zombie_fight = True
            hero.attack(zombie)
            zombie.health = zombie.power
            zombie.print_status()

        elif raw_input == "3":
            pass
        elif raw_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

        if goblin.health > 0 and goblin_fight:
            # Goblin attacks hero
            goblin.attack(hero)
            hero.health -= goblin.power
            hero.print_status()
        elif zombie.health > 0 and zombie_fight:
            zombie.attack(hero)
            hero.health -= zombie.power
            hero.print_status()


main()

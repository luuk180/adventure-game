import random

import player


class Mob:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def fight(self):
        fighting = True
        while fighting:
            print("You are in combat, you can either attack or block.")
            print("1. Attack")
            print("2. Run away")
            choice = input()
            if choice == "1":
                print("You chose to attack!")
                self.health = self.health - player.attack_damage
            elif choice == "2":
                rng = random.random()
                if rng > 0.5:
                    print("You successfully ran away!")
                    fighting = False
                else:
                    print("You failed to run away!")
        else:
            return

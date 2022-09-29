import random

import player


class Mob:
    def __init__(self, name, health, weapon, attack_damage):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_damage = attack_damage

    def fight(self, attacker: player.Player):
        fighting = True
        while fighting:
            print("You are in combat, you can either attack or try to run away.")
            print("1. Attack")
            print("2. Run away")
            choice = input()
            if choice == "1":
                print("You chose to attack!")
                self.health = self.health - attacker.attack_damage
                print(self.name, "attacks you and does", self.attack_damage, "damage!")
                if attacker.health <= 0:
                    print("You died!")
                    fighting = False
            elif choice == "2":
                rng = random.random()
                if rng > 0.5:
                    print("You successfully ran away!")
                    fighting = False
                else:
                    print("You failed to run away!")
        else:
            return

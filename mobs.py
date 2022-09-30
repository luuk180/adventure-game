import random

import player
import location_scripts


class Mob:
    def __init__(self, name, health, weapon, attack_damage, dead):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.attack_damage = attack_damage
        self.dead = dead

    def fight(self, attacker: player.Player):
        fighting = True
        starting_health = attacker.health
        if "Longsword" in attacker.inventory:
            attacker.attack_damage = 3
        elif "One handed axe" in attacker.inventory:
            attacker.attack_damage = 2
        elif "War Hammer" in attacker.inventory:
            attacker.attack_damage = 3
        else:
            print("It's not too smart to go in with just your fists...")
            attacker.attack_damage = 1
        if "Blessing of the Goblin God" in attacker.inventory:
            attacker.attack_damage += 3
        attacker.attack_damage += attacker.base_damage
        while fighting:
            if attacker.health <= 0:
                fighting = False
                attacker.death(starting_health)
            if self.health <= 0:
                self.dead = True
                fighting = False
            print("You are in combat, you can either attack or try to run away.")
            print("1. Attack")
            print("2. Run away")
            choice = input()
            if choice == "1":
                print("You chose to attack!")
                self.health = self.health - attacker.attack_damage
                print("You do", attacker.attack_damage, "damage!")
                print(self.name, "attacks you and does", self.attack_damage, "damage!")

            elif choice == "2":
                rng = random.random()
                if rng > 0.5:
                    print("You successfully ran away!")
                    return "return"
                else:
                    print("You failed to run away!")
                    print(self.name, "attacks you and does", self.attack_damage, "damage!")
            if attacker.health <= 0:
                location_scripts.death_scene()
        return

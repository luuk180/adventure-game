import global_objs
import location_scripts


class Player:
    def __init__(self, name, health, inventory, attack_damage, base_damage):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.attack_damage = attack_damage
        self.base_damage = base_damage

    def death(self, starting_health):
        print("You died!")
        if self.name == "Hobgoblins":
            self.health = starting_health
            global_objs.player.inventory.append("Blessing of the Goblin God")
            location_scripts.town_square()
        else:
            self.health = 20
            location_scripts.ad_guild()

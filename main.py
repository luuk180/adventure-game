# Load the map and the player information.
from player import Player
from mobs import Mob
from utils import print_inventory


def init(name):
    player = Player(name, 20, ["Hat"])

    return player


def run_game():
    player = intro()
    print_inventory(player.inventory)

    return


# Intro to the game
def intro():
    print("Welcome weary adventurer to the hold of duke John")
    print("Let's start with your name: ")
    name = input()
    player = init(name)
    print("Good luck, " + name + ".")

    return player


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

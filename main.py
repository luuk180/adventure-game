import player
from mobs import Mob
import location_scripts
from utils import print_inventory


def init(name):
    global player
    player = player.Player(name, 20, ["Hat"])

    return


def run_game():
    intro()
    location_scripts.intro_scene()

    print_inventory(player.inventory)

    return


# Intro to the game
def intro():
    print("Welcome weary adventurer to the hold of duke John")
    print("Let's start with your name: ")
    name = input()
    init(name)
    print("Good luck, " + player.name + ".")

    return player


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

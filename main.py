# Load the map and the player information.
from player import Player
from utils import print_inventory


def init():
    player = Player("Henry", 20, ["Hat", "Sword"])

    return player


def run_game():
    player = init()
    print(print_inventory(player.inventory))

    return


# Intro to the game
def intro():
    print("Welcome to the hold of duke John!")
    print("Your adventure starts here.")

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os

import global_objs
import location_scripts
import player


def init(name):
    global_objs.player = player.Player(name, 20, ["Hat"], 0, 2)

    return


def run_game():
    intro()

    location_scripts.intro_scene()


# Intro to the game
def intro():
    print("Welcome weary adventurer to the hold of duke John")
    name = input("Let's start with your name: ")
    init(name)
    print("Good luck, " + global_objs.player.name + ".")

    return


def save_game():
    if os.path.exists("./save-game"):
        print("Loading save game...")
    else:
        print("No save game exists")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

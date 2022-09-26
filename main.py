import json


# Load the map and the player information.
def init():
    save = open("inventory.json")
    if save == "":
        return "new player"
    player_stats = json.load(save.read())

    return player_stats


def run_game():
    player_stats = init()
    if player_stats == "new player":
        # Create new player
        print()


def intro():
    print("Welcome to the hold of duke John!")
    print("Your adventure starts here.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

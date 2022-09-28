import player


def print_inventory(inventory):
    for i in range(len(inventory)):
        print(inventory[i])


def global_options():
    print("i to show inventory")
    option = input()
    if option == "i":
        print_inventory(player.inventory)
        return True
    else:
        return False

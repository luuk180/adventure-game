if __name__ == "__main__":
    while True:
        print("Welcome weary adventurer to the hold of duke John")
        print("Let's start with your name: ")
        name = input()
        print("Good luck, " + name + ".")
        introScene()


def introScene():
    print(
        "You are standing in the great hall of Duke John of Castonath. The walls of the hall are decked with portraits ")


def mtBase():
    directions = ["1", "2"]
    print(
        "You are currently standing at the base of the mountain. \n To your east lies the adventurer guild \n To your north lies the mountain village of Castanor \n Where will you head? \n 1. Adventurer guild \n 2. Mountain village")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            adGuild()
        elif uinput == '2':
            print("You walk through the city gates")
            twnSquare()
        else:
            print("Please enter a valid option")


def adGuild():
    directions = ["1", "2"]
    print(
        "Welcome to the adventurer guild, here you can speak to the few members of the guild\n 1. Speak with Rondine the Trader\n 2. Leave to the mountain base")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            tradeTalk()
        elif uinput == '2':
            mtBase()
        else:
            print("Please enter a valid option")


def twnSquare():
    directions = ["1", "2", "3", "4"]
    print(
        "Ahead of you lies the town square, there are a few market stalls selling their goods to the local populace and you can see the town elder from here. From the town square you can go to two directions \n 1. Head to the hold of duke John of Castonath \n 2. Go to the local blacksmith \n 3. Speak with the town elder \n 4. Return down the mountain path")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2 or 3")
        uinput = input()
        if uinput == '1':
            dukeHold()
        elif uinput == '2':
            mtBase()
        elif uinput == '3':
            tlkElder()
        elif uinput == '4:':
            mtBase()
        else:
            print("Please enter a valid option")

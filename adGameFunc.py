if __name__ == "__main__":
  while True:
    print("Welcome weary adventurer to the hold of duke John")
    print("Let's start with your name: ")
    name = input()
    print("Good luck, " +name+ ".")
    introScene()


def mtBase():
    directions = ["1","2"]
    print("You are currently standing at the base of the mountain. \n To your east lies the adventurer guild \n To your north lies the mountain village of Castanor \n Where will you head? \n 1. Adventurer guild \n 2. Mountain village")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            adGuild()
        elif uinput == '2':
            vilSquare()
        else:
            print("Please enter a valid option")

def adGuild():
    directions = ["1","2"]
    print("Welcome to the adventurer guild, here you can speak to the few members of the guild\n 1. Speak with Rondine the Trader\n 2. Leave to the mountain base")
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
    directions = ["1","2","3"]
    



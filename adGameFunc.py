def intro_scene():
    print("You are standing in the great hall of Duke John of Castonath. The walls of the hall are decked with portraits which you assume are the ancestors of the current Duke. \n"
          "A courtier approaches you as you are admiring the portrait with the most astonishing beard you have ever seen and says to you: His lordship the duke will now addres you \n"
          "You follow the courtier to the Duke as you approach the old Duke finally comes into your view.\n"
          "'Welcome,", name, "I've been looking forward to meeting you ever since I posted the quest over at the adventurer's guild \n"
          "But let's get straight to the point, I require your skills to retrieve an ancient artifact for me \n"
          "My book keeper has been obsessed with the Dwarven ruins that are close to the city of Castonath ever since his birth and he has told me about an artifact that could be infused with magic which wi-' He's interrupted by the courtier giving a loud cough \n"
          "'Right, sorry, the details shouldn't matter', he continues: 'I've been told that the cave can be quite dangerous so we have prepared a permit for you so that you may go to Hamon the Blacksmith to pick up a weapon for this journey \n"
          "While you're still here you should go and talk to Luchika, he's my book keeper he might have some useful information for you\n"
          "Now go, we will eagerly abide your return. Safe travels", name, "!")
    duke_hold()

def mountain_base():
    directions = ["1", "2"]
    print("You are currently standing at the base of the mountain. \n"
          "To your east lies the adventurer guild \n"
          "To your north lies the mountain village of Castanor \n"
          "Where will you head? \n"
          "1. Adventurer guild \n 2. Mountain village")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            ad_guild()
        elif uinput == '2':
            # vilSquare()
        else:
            print("Please enter a valid option")

def ad_guild():
    directions = ["1","2"]
    print("Welcome to the adventurer guild, here you can speak to the few members of the guild\n "
          "1. Speak with Rondine the Trader\n "
          "2. Leave to the mountain base")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            # tradeTalk()
        elif uinput == '2':
            mountain_base()
        else:
            print("Please enter a valid option")

def town_square():
    directions = ["1", "2", "3", "4"]
    print(
        "Ahead of you lies the town square, there are a few market stalls selling their goods to the local populace and you can see the town elder from here. From the town square you can go to two directions \n "
        "1. Head to the hold of duke John of Castonath \n "
        "2. Go to the local blacksmith \n "
        "3. Speak with the town elder \n "
        "4. Return down the mountain path")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2 or 3")
        uinput = input()
        if uinput == '1':
            # dukeHold()
        elif uinput == '2':
            # blacksmith()
        elif uinput == '3':
            # tlkElder()
        elif uinput == '4:':
            mountain_base()
        else:
            print("Please enter a valid option")

def duke_hold():
    directions = ["1", "2"]
    print("You are currently standing in the main hall of Duke John of Castonath, from here you can either go to the town's square or go to the study of Loremaster Luchika\n"
          "1. Exit the hold and proceed to the town square\n"
          "2. Go the Loremaster Luchika's study")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            town_square()
        elif uinput == '2':
            keep_study()
        else:
            print("Please enter a valid option")

def keep_study():
        print("You walk into Loremaster Luchika's study \n"
          "The first thing you note is that all the walls are completely lined with bookshelves wich are just bursting at the seems\n"
          "It almost seems that beside all the books and scrolls the is empty so you say shout:'Hello? Luchika are you in here?'\n"
          "You hear a loud thud behind some books followed by a 'Yes, I'm here. I'll be out in a second' \n"
          "'Greetings! You must be",name,"Duke John has told me about your arrival\n"
          "I suppose you want to learn some more about the Dwarven hold? Here I'll let you in some of their secrets\n"
          #here he tells you about the puzzle and some other things that are irrelevant
          "You interrupt him now since he's been rambling on about more and more irrelevant stuff \n"
          "'Oh sorry I tend to do that sometimes, I'm just so fascinated by their entire excistence. Well anyways you best be off now best of luck!'")
        duke_hold()





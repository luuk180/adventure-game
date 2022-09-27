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
            town_square()
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
            # hier moet nog een trade option komen met iets van een speciale paddestoel ofzo die je uit 8 udg_river() haalt voor explosieven zodat je 6 abandoned_hold in kan
        elif uinput == '2':
            mountain_base()
        else:
            print("Please enter a valid option")

def town_square():
    directions = ["1", "2", "3", "4", "5"]
    print(
        "Ahead of you lies the town square, there are a few market stalls selling their goods to the local populace and you can see the town elder from here. From the town square you can go to two directions \n "
        "1. Head to the hold of duke John of Castonath \n "
        "2. Go to the local blacksmith \n "
        "3. Speak with the town elder \n "
        "4. Return down the mountain path"
        "5. Move towards the cave entrance")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2 or 3")
        uinput = input()
        if uinput == '1':
            duke_hold()
        elif uinput == '2':
            blacksmith()
        elif uinput == '3':
            # tlkElder()
        elif uinput == '4:':
            mountain_base()
        elif uinput == '5':
            # def mt_path_comb(): hier heb je eerste combat met highwaymen daarna ga je door naar cave
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
        directions = ["1"]
        print("You walk into Loremaster Luchika's study \n"
          "The first thing you note is that all the walls are completely lined with bookshelves wich are just bursting at the seems\n"
          "It almost seems that beside all the books and scrolls the is empty so you say shout:'Hello? Luchika are you in here?'\n"
          "You hear a loud thud behind some books followed by a 'Yes, I'm here. I'll be out in a second' \n"
          "'Greetings! You must be",name,"Duke John has told me about your arrival\n"
          "I suppose you want to learn some more about the Dwarven hold? Here I'll let you in some of their secrets\n"
          #here he tells you about the puzzle and some other things that are irrelevant
          "You interrupt him now since he's been rambling on about more and more irrelevant stuff \n"
          "'Oh sorry I tend to do that sometimes, I'm just so fascinated by their entire excistence. Well anyways you best be off now best of luck!'")
        uinput = ""
        while uinput not in directions:
            print("Press 1 to return to the main hall")
            uinput = input()
            if uinput == '1':
                duke_hold()
            else:
                print("Please enter a valid option")

def blacksmith():
    wep_choice = ["1", "2", "3"]
    print("As you head to the smithy you are greeted by Hamon the blacksmith\n"
          "'Hail, I've yet to see your face around here, you must be a traveler'\n"
          "You explain the story and hand Hamon the permit given to you by Duke John\n"
          "'Ah I see, well as per this permit I will allow you choice of weapon so tell me what would you'd like. Just one restriction I can't go and make something custom for you right now because the permit says that it would take too long, but follow me I'll show you my stock\n"
          "You follow Hamon inside and he shows you his wares\n"
          "1. Longsword\n"
          "2. One handed axe\n"
          "3. Warhammer")
    while uinput not in wep_choice:
        print("Please input 1, 2 or 3")
        uinput = input()
        if uinput == '1':
                #add weapon longsword to inv
            elif uinput == '2':
                #add weapon axe to inv
            elif uinput == '3':
                #add weapon whammer to inv
            else:
                print("Please enter a valid option")
    print("'Ah, excellent choice, I am very proud of that one\n"
          "Before you leave make sure to test your weapon and skills on the dummy that's just to our left, best make sure you can handle it well\n"
          "Best of luck out there!")
    # dummy_train() dit moet een combat function zijn denk ik? maar weet niet hoe je het wil implementen dus doe het maar ff zo 'dummy_train()' moet je ook wel terug plaatsen in de town_square()

def cave_entrance():
    directions  = ["1", "2", "3", "4"]
    print("You approach the cave entrance that will lead to the abandoned dwarven hold\n"
          "Once you have entered the cave you see a bridge made from cut stone that leads to what you assume will be the gate to the hold\n"
          "Below the bridge you see a small river flowing down the mountain, you asses that you should be able to descend to the river and follow it if you so chose\n"
          "1. Move along the bridge to the gate\n"
          "2. Descend down the wall of the mountain and follow the river\n"
          "3. Return to Castanor\n"
          "4. Go back to the base of the mountain")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2, 3 or 4")
        uinput = input()
        if uinput == '1':
            #hold_bridge()
        elif uinput == '2':
            print("You scale down the wall to the river")
            #cave_river()
        elif uinput == '3':
            town_square()
        elif uinput == '4:':
            mountain_base()
        else:
            print("Please enter a valid option")

def cave_river():
    directions = ["1", "2", "3"]
    print("You are now standing at the river bank\n"
          "From here you vaguely see a lake that the river flows to, you also see a feint blue light emanating from the lake\n"
          "1. Move towards the lake\n"
          "2. Return to the cave entrance\n"
          "3. Use some of the rope you have to climb up to the bridge that connects the cave entrance to the hold")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2, or 3")
        uinput = input()
        if uinput == '1':
            #cave_river()
        elif uinput == '2':
            print("You scale down the wall to the river")
            cave_entrance()
        elif uinput == '3':
            #hold_bridge()
        else:
            print("Please enter a valid option")

def cave_lake():
    directions = ["1"]
    print("As you keep heading towards what you assume to be the river you can see that the blue light is growing ever more bright\n"
          "Now that you have entered the room where the lake resides in you see that on a few edges around the lake are inhabited by some large mushrooms which appear to bee the source of the blue hue\n"
          "You feintly remember one of the guild members talking about mushrooms that somewhat fit the description of the ones that grow around here, so you decide to collect some for them\n"
          "1. Return to where you started following the river"
    # mushrooms toevoegen aan de player inv zodat ze in ad_guild met guy kunnne praten voor explosives om deur open te maken
    uinput = ""
    while uinput not in directions:
        print("Please input 1")
        uinput = input()
        if uinput == '1':
            cave_river()
        else:
            print("Please enter a valid option")


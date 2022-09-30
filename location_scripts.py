import global_objs


def intro_scene():
    directions = ["1"]
    print(
        "You are standing in the great hall of Duke John of Castonath. The walls of the hall are decked with portraits which you assume are the ancestors of the current Duke. \n"
        "A courtier approaches you as you are admiring the portrait with the most astonishing beard you have ever seen and says to you: His lordship the duke will now addres you \n"
        "You follow the courtier to the Duke as you approach the old Duke finally comes into your view.\n"
        "'Welcome,", global_objs.player.name,
        "I've been looking forward to meeting you ever since I put up the quest over at the adventurer guild \n"
        "But let's get straight to the point, I require your skills to retrieve an ancient artifact for me \n"
        "My book keeper has been obsessed with the Dwarven ruins that are close to the city of Castonath ever since his birth and he has told me about an artifact that could be infused with magic which wi-' He's interrupted by the courtier giving a loud cough \n"
        "'Right, sorry, the details shouldn't matter', he continues: 'I've been told that the cave can be quite dangerous so we have prepared a permit for you so that you may go to Hamon the Blacksmith to pick up a weapon for this journey \n"
        "While you're still here you should go and talk to Luchika, he's my book keeper he might have some useful information for you\n"
        "Now go, we will eagerly abide your return. Safe travels", global_objs.player.name, "!\n")
    uinput = ''
    while uinput not in directions:
        print("Please input 1")
        uinput = input()
        if uinput == '1':
            print("You turn around an walk towards the main hall\n")
            duke_hold()
        else:
            print("Please enter a valid option\n")
            continue


def mountain_base():
    directions = ["1", "2"]
    print("You are currently standing at the base of the mountain. \n"
          "To your east lies the adventurer guild \n"
          "To your north lies the mountain village of Castanor \n"
          "Where will you head? \n"
          "1. Adventurer guild \n"
          "2. Mountain village\n")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            print("You move to the all so familiar adventurer guild\n")
            ad_guild()
        elif uinput == '2':
            print("You walk past the city gates and into the town square of Castanor\n")
            town_square()
        else:
            print("Please enter a valid option\n")
            continue


def ad_guild():
    directions = ["1", "2"]
    print("Welcome to the adventurer guild, here you can speak to the few members of the guild\n "
          "1. Speak with master Arlow\n "
          "2. Leave to the mountain base\n")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            print("You approach Arlow\n")
            trade_talk()
        elif uinput == '2':
            print("You walk out of the door towards the mountain base\n")
            mountain_base()
        else:
            print("Please enter a valid option\n")


def town_square():
    directions = ["1", "2", "3", "4", "5"]
    print(
        "Ahead of you lies the town square, there are a few market stalls selling their goods to the local populace and you can see the town elder from here. From the town square you can go to two directions \n "
        "1. Head to the hold of duke John of Castonath \n "
        "2. Go to the local blacksmith \n "
        "3. Speak with the town elder \n "
        "4. Return down the mountain path\n"
        "5. Move towards the cave entrance\n")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2, 3, 4 or 5")
        uinput = input()
        if uinput == '1':
            print("You walk past all the stall and climb up the stairs that lead to the duke's hold\n")
            duke_hold()
        elif uinput == '2':
            print("You decide to go and see the local blacksmith\n")
            blacksmith()
        elif uinput == '3':
            print("Maybe this old man can give you some advice\n")
            talk_elder()
        elif uinput == '4':
            print("You exit the town and walk down the path to the base of the mountain\n")
            mountain_base()
        elif uinput == '5':
            if not global_objs.highwaymen.dead:
                print("You start moving towards the cave entrance\n"
                      "As you walk through a quite shallow valley you hear some murmuring coming from the top\n"
                      "The whispers came from a small group of highwaymen!\n"
                      "Prepare for combat!\n")
                global_objs.highwaymen.fight(global_objs.player)
                cave_entrance()
            else:
                print("You exit the town and walk to the cave entrance")
                cave_entrance()
        else:
            print("Please enter a valid option\n")
            continue


def duke_hold():
    if "Artifact" in global_objs.player.inventory:
        directions = ["1", "2", "3"]
        print(
            "You are currently standing in the main hall of Duke John of Castonath, from here you can either go to the town's square or go to the study of Loremaster Luchika\n"
            "1. Exit the hold and proceed to the town square\n"
            "2. Go the Loremaster Luchika's study\n"
            "3. Present the artifact to duke John")
        uinput = ''
        while uinput not in directions:
            print("Please input 1, 2 or 3")
            uinput = input()
            if uinput == '1':
                print("You leave the dukes hold and walk down the stairs to the town square")
                town_square()
            elif uinput == '2':
                print("You open the door to the loremaster's study")
                keep_study()
            elif uinput == '3':
                print("You approach the duke sitting in his study")
                outro_scene()
            else:
                print("Please enter a valid option\n")
                continue
    else:
        directions = ["1", "2"]
        print(
            "You are currently standing in the main hall of Duke John of Castonath, from here you can either go to the town's square or go to the study of Loremaster Luchika\n"
            "1. Exit the hold and proceed to the town square\n"
            "2. Go the Loremaster Luchika's study\n")
        uinput = ""
        while uinput not in directions:
            print("Please input 1 or 2")
            uinput = input()
            if uinput == '1':
                print("You leave the dukes hold and walk down the stairs to the town square")
                town_square()
            elif uinput == '2':
                print("You open the door to the loremaster's study")
                keep_study()
            else:
                print("Please enter a valid option\n")
                continue


def keep_study():
    directions = ["1"]
    print("You walk into Loremaster Luchika's study \n"
          "The first thing you note is that all the walls are completely lined with bookshelves wich are just "
          "bursting at the seems\n "
          "It almost seems that beside all the books and scrolls the is empty so you say shout:'Hello? Luchika are "
          "you in here?'\n "
          "You hear a loud thud behind some books followed by a 'Yes, I'm here. I'll be out in a second' \n"
          "'Greetings! You must be", global_objs.player.name, "Duke John has told me about your arrival\n"
                                                              "I suppose you want to learn some more about the "
                                                              "Dwarven hold? Here I'll let you in some of their "
                                                              "secrets\n "
                                                              "Dwarves are really religious when it comes to whether you are left or right handed\n"
                                                              "So much so that everyone who is let handed is shunned by the local community and cast into exile\n"
                                                              "Here I have something for you\n")
    global_objs.player.inventory.append("Loremaster Luchika's Book")
    if "Loremaster Luchika's Book" in global_objs.player.inventory:
        print("He hands you one of his books...")
        global_objs.player.inventory.append("Loremaster Luchika's Book")
        choice = input("Do you read the book? ")
        if choice == "yes":
            print("Good choice! You learn how to do more damage.")
            global_objs.player.base_damage += 2
        elif choice == "no":
            print("You passed up a good opportunity...")
    print("You interrupt him now since he's been rambling on "
          "about more and more irrelevant stuff \n "
          "'Oh sorry I tend to do that sometimes, I'm just so "
          "fascinated by their entire existence. Well anyways you "
          "best be off now best of luck!'\n")
    uinput = ""
    while uinput not in directions:
        print("Press 1 to return to the main hall")
        uinput = input()
        if uinput == '1':
            print("You exit the study through the door back into the hold\n")
            duke_hold()
        else:
            print("Please enter a valid option\n")
            continue


def blacksmith():
    wep_choice = ["1", "2", "3"]
    print("As you head to the smithy you are greeted by Hamon the blacksmith\n"
          "'Hail, I've yet to see your face around here, you must be a traveler'\n"
          "You explain the story and hand Hamon the permit given to you by Duke John\n"
          "'Ah I see, well as per this permit I will allow you choice of weapon so tell me what would you'd like. "
          "Just one restriction I can't go and make something custom for you right now because the permit says that "
          "it would take too long, but follow me I'll show you my stock\n "
          "You follow Hamon inside and he shows you his wares\n"
          "1. Longsword\n"
          "2. One handed axe\n"
          "3. War Hammer")
    uinput = ''
    while uinput not in wep_choice:
        print("Please input 1, 2 or 3")
        uinput = input()
        if uinput == '1':
            global_objs.player.inventory.append("Longsword")
        elif uinput == '2':
            global_objs.player.inventory.append("1hAxe")
        elif uinput == '3':
            global_objs.player.inventory.append("War Hammer")
        else:
            print("Please enter a valid option\n")
            continue
    print("'Ah, excellent choice, I am very proud of that one\n"
          "Before you leave make sure to test your weapon and skills on the dummy that's just to our left, best make sure you can handle it well\n"
          "Whenever you are done with just swinging your weapon feel free to leave, I'd say it's quite unlikely you can keep going until it's nothing but firewood\n"
          "Oh before I forget, I've heard that there could be goblins somewhere in the cave\n"
          "They are a very crafty race and I would really like to hold and use some if their contraptions. If you can bring me any I'll give you something in return from my collection\n"
          "Best of luck out there!\n")

    if not global_objs.ragdoll.dead:
        if global_objs.ragdoll.fight(global_objs.player) == "return":
            blacksmith()
    town_square()


def cave_entrance():
    directions = ["1", "2", "3", "4"]

    print(
        "Once you have entered the cave you see a bridge made from cut stone that leads to what you assume will be the gate to the hold\n"
        "There is a steep wall that leads to a lower area of the cave where you can hear what you assume to be a river, you asses that you can scale down the wall if you have some rope\n"
        "1. Move along the bridge to the gate\n"
        "2. Descend down the wall of the mountain and follow the river\n"
        "3. Return to Castanor\n"
        "4. Go back to the base of the mountain")
    uinput = ""
    while uinput not in directions:
        print("Please input 1, 2, 3 or 4")
        uinput = input()
        if uinput == '1':
            bridge_hold()
        elif uinput == '2':
            if "Rope" in global_objs.player.inventory:
                print("You descend slowly down to the river")
                cave_river()
            else:
                print(
                    "You stare down into the darkness, going down this wall without anything to slow yourself down would be suicide")
                cave_entrance()
        elif uinput == '3':
            print("You decide to head back to the town")
            town_square()
        elif uinput == '4':
            print("You decide to return to the base of the mountain")
            mountain_base()
        else:
            print("Please enter a valid option\n")
            continue


def cave_river():
    directions = ["1", "2"]
    print("You are now standing at the river bank\n"
          "From here you vaguely see a lake that the river flows to, you also see a faint blue light emanating from "
          "the lake\n "
          "1. Move towards the lake\n"
          "2. Return to the cave entrance")
    uinput = ""
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            print("You walk along the river towards the source of light\n")
            cave_lake()
        elif uinput == '2':
            print("You climb up the wall to the cave entrance using the rope that you also used for you descent\n")
            cave_entrance()
        else:
            print("Please enter a valid option\n")
            continue


def cave_lake():
    directions = ["1", "2"]
    if "Mushrooms" not in global_objs.player.inventory:
        print(
            "As you keep heading towards what you assume to be the river you can see that the blue light is growing ever more bright\n"
            "Now that you have entered the room where the lake resides in you see that on a few edges around the lake are inhabited by some large mushrooms which appear to bee the source of the blue hue\n"
            "You feintly remember one of the guild members talking about mushrooms that somewhat fit the description of the ones that grow around here\n"
            "1. Return to where you started following the river\n"
            "2. Collect mushrooms")
        uinput = ""
        while uinput not in directions:
            print("Please input 1 or 2")
            uinput = input()
            if uinput == '1':
                print("You leave the lake and return to where you went down to the river initially\n")
                cave_river()
            elif uinput == '2':
                print("You pick most of the mushrooms and place them in you backpack\n")
                global_objs.player.inventory.append("Mushrooms")
                cave_lake()
            else:
                print("Please enter a valid option\n")
                continue
    else:
        print("You are standing on the furthest edge of the river bank, where you collected the mushrooms earlier\n"
              "There doesn't seem to be anything of interest here left\n"
              "1. Walk back along the river")
        uinput = ''
        while uinput not in directions:
            print("Please input 1")
            uinput = input()
            if uinput == '1':
                cave_river()
            else:
                print("Please provide a valid option\n")
                continue


def bridge_hold():
    if not global_objs.bridge_open_door:
        directions = ["1", "2"]
        print(
            "You walk over the bridge towards the gate of the dwarven hold, as you walk the gate appears to be getting larger and larger until you are standing in front of it\n"
            "The gate must be at least 25 meters tall and is looming over you quite menacingly\n"
            "Opening this thing with just your own strength will be impossible, but age appears to have taken a toll on this entrance and it seems very plausible that you can blast open the door with a controlled explosion\n"
            "1. Proceed into the hold\n"
            "2. Walk back to the cave's entrance over the bridge")
        uinput = ""
        while uinput not in directions:
            print("Please input 1 or 2")
            uinput = input()
            if uinput == '1':
                if "Explosives" in global_objs.player.inventory:
                    print("You blow a house sized hole into the door and proceed into the abandoned dwarven hold\n")
                    global_objs.bridge_open_door = True
                    mountain_hold()
                else:
                    print(
                        "The door won't budge a bit, it seems you will need something with a lot of force to convince the door to open\n")
                    bridge_hold()
            elif uinput == '2':
                print("You walk over the bridge back to the entrace of the cave\n")
                cave_entrance()
            else:
                print("Please enter a valid option\n")
                continue
    else:
        directions = ["1", "2"]
        print(
            "You walk over the bridge towards the gate of the dwarven hold, as you walk the gate appears to be getting larger and larger until you are standing in front of it\n"
            "The large hole in the gate is still there, would be weird if it were repaired so sudden\n"
            "1. Proceed into the hold\n"
            "2. Walk back to the cave's entrance over the bridge")
        uinput = ""
        while uinput not in directions:
            print("Please input 1 or 2")
            uinput = input()
            if uinput == '1':
                print("You walk through the destruction that you have cause into the hold\n")
                mountain_hold()
            elif uinput == '2':
                print("You walk over the bridge back to the entrace of the cave\n")
                cave_entrance()
            else:
                print("Please enter a valid option\n")
                continue


def mountain_hold():
    directions = ["1", "2"]
    if not global_objs.goblin_boss.dead:
        print(
            "You are now standing in the middle of the abandoned hold, it appears this used to be a small village with a small houses scattered around the main square of the hold\n"
            "It appears though that this hold is not as abandoned as you first thought! Goblins have taken up residence in the vacant houses and the explosions have not only awakened them but also greatly angered them\n"
            "Prepare for combat!")
        global_objs.goblin_boss.fight(global_objs.player)
        print(
            "After defeating a few of the goblins the others flee the scene into small tunnels in the wall, chasing them would be pointless and impossible since the holes are nowhere near big enough for you to fit through\n"
            "It does look like in their hurry the goblins left some things lying around")
    if not global_objs.lift_on:
        print(
            "After some looking around you find something that looks like a lifting contraption that should take you to the temple that lies on the summit of this mountain"
            "Do you pull the lever on the left or on the right?\n"
            "1. The one on the left."
            "2. The one on the right.")
        uinput = ''
        while uinput not in directions:
            print("Please input 1 or 2")
            uinput = input()
            if uinput == "1":
                print("A trapdoor under you opens and you fall...")
                global_objs.player.death()
            elif uinput == "2":
                print("The lift starts to come to life...")
    print(
        "Now that you have the lifting platform working you can go to the temple or you can chose to return through the gate to the bridge\n"
        "1. Go up the elevator contraption to summit temple\n"
        "2. Return to the bridge")
    uinput = ''
    while uinput not in directions:
        print("Please input 1 or 2")
        uinput = input()
        if uinput == '1':
            print("You use the lifting platform and ascend to the top of the hold\n")
            summit_temple()
        elif uinput == '2':
            print("You exit the hold through the battered gate\n")
            bridge_hold()
        else:
            print("Please enter a valid option\n")
            continue


def summit_temple():
    directions = ["1", "2"]
    if not global_objs.hobgoblins.dead:
        print(
            "The elevator has finished it's climb towards the top and you are now standing in the middle of a relatively small room compared to the rest of the hold\n"
            "Before you have more time to inspect your surrounding you see some movement in the corner of your eye however\n"
            "It appears that a bunch of bigger and more ruthless goblins, hobgoblins are squatting in the temple of the dwarves\n"
            "Prepare for combat!")
        global_objs.hobgoblins.fight(global_objs.player)
        print(
            "These hobgoblins are a lot stronger then their smaller goblin counterpart, but having finally defeated them all you can finally explore the rest of the room\n"
            "Eventually you stumble upon a chest that has some markings on the top, you recognize these markings as the ones that Loremaster Luchika has told you about, this should be the chest that contain the artifact you have been tasked to retrieve")
    if "Skeleton Key" in global_objs.player.inventory and not global_objs.skeleton_chest_opened:
        print("The lock pops open after a satisfying click and drops to the ground\n"
              "You open the chest and there lies the artifact you have been looking for\n"
              "It's a silver necklace attached to a weird stone that changes colour depending on the angle that you look at\n"
              "You can now return to duke John and receive your reward\n"
              "You also find that you can scale down the mountain side with some rope so that you can get yourself very close to the town square\n"
              "1. Go down the mountainside and return to the town square\n"
              "2. Go down the elevator to the dwarven hold")
    elif "Skeleton Key" in global_objs.player.inventory and global_objs.skeleton_chest_opened:
        print("Welcome back to the summit temple!"
              "It's a little quiet here without the hobgoblins...")
    else:
        print("You can't yet open the chest...")
        print("You need to look for the Skeleton Key")

        uinput = ''
        while uinput not in directions:
            print("please input 1 or 2")
            uinput = input()
            if uinput == '1':
                town_square()
            elif uinput == '2':
                mountain_hold()
            else:
                print("Please enter a valid option\n")
                continue


def trade_talk():
    directions = ["1"]
    if "Mushrooms" in global_objs.player.inventory:
        print(
            "'Ah you have some of the Nitroshrooms that I wanted, I hope you didn't eat any because these little buggers are what we use to make explosives with\n"
            "Here, since you have brought me these I'll show you how to turn them into a shaped charge that you can use whenever something doesn't feel like moving out of your way'\n"
            "Explosives added to your inventory\n"
            "1. Exit the guild and return to the base of the mountain")
        global_objs.player.inventory.append("Explosives")
    else:
        print("'Hey,", global_objs.player.name,
              "I'm Arlow the adventurer guild's demolitionist, with an expertise in explosives\n"
              "I've heard that you're heading into the cave that's a bit further up the mountain\n"
              "I wanted to head there myself to scavenge for some Nitroshrooms but haven't had the time since grandmaster Galleus left for some meeting of the adventurer union\n"
              "Tell you what, if you bring me some I'll show you how to make some explosives out of the 'shrooms'\n"
              "1. Exit the guild and return to the base of the mountain")
    uinput = ''
    while uinput not in directions:
        print("Please input 1")
        uinput = input()
        if uinput == '1':
            mountain_base()
        else:
            print("Please enter a valid option")
            continue


def talk_elder():
    directions = ["1"]
    if "Rope" not in global_objs.player.inventory:
        print("'Hello, I don't think I've seen your face here before, you must be from out of town\n"
              "I've heard that you are gonna go into the cave so let me give you a word of advice\n"
              "Things can get quite perilous in there so I recommend you bring some rope with you, luckily for you I have some spare rope lying about that you can bring with you\n"
              "These old hands have no use for this anymore so you can just keep them\n"
              "Stay safe traveller'\n"
              "1. Return to the town square")
        global_objs.player.inventory.append("Rope")

    else:
        print("It appears that the elder has left, maybe it was time for him to take a nap, he is quite old after all\n"
              "1. Return to the town square")
    uinput = ''
    while uinput not in directions:
        print("Please input 1")
        uinput = input()
        if uinput == '1':
            town_square()
        else:
            print("Please enter a valid option")
            continue


def death_scene():
    print("No health left...")
    print("You spawn back at the adventurers guild...")
    ad_guild()


def outro_scene():
    print("'Ah", global_objs.player.name, "you've returned, tell me do you have the artifact?'\n"
                                          "You nod your head and grab a small pouch from your backpack and hand it over to duke John\n"
                                          "He eagerly accepts the pouch and opens it up immediately\n"
                                          "'I've never told you what this artifact does right?'\n"
                                          "You shake your head\n"
                                          "'Right, maybe it's time to let you in on a little secret, this artifact is something that I will be using as a Phylactery\n"
                                          "Now I know what you're thinking 'what is a Phylactery?', well the answer is quite simple.\n"
                                          "They are used to bind something with magical qualities to something of the physical realm\n"
                                          "The dwarves were always known for their craftsmanship and ability to make things that could last for centuries\n"
                                          "To put it bluntly, I needed something that I could use to bind my soul into and ascend into lichdom, and you my dear",
          global_objs.player.name, "have provided me with just that\n"
                                   "Since you have been so valuable to me in this life, I want to offer you some advice. Leave the kingdom, Things are gonna be a bit different around here\n"
                                   "I have decided that I want to rule for a bit longer then the meager amount of years that me predecessors could and I don't want you to get involved in all this mess that comes with my ascension\n"
                                   "So, farewell my dearest adventurer, may we meet again in this life or the next!'\n"
                                   "You decide it's best to heed his advice for now and leave\n"
                                   "But you decide that there is no way that the Magisterium won't hear of this, a new lich rising could be disastrous for everyone who lives here and the next two kingdoms over")
    exit()

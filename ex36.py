from sys import exit

def kitchen():
    print "You are in the kitchen."
    print "It's full of candy and fruit. Which do you eat?"

    next = raw_input("> ")
    if "fruit" in next:
        print "Good choice, you win!"
        exit(0)

    if "candy" in next:
        print "Candy is poison, you are dead."

def ballroom():
    print "You are in the ballroom."
    print "You see a pig and a duck."
    print "Who do you dance with?"

    next = raw_input("> ")

    if "duck" in next:
        print "Duck likes you, lays magic egg with key it it, move on."
        kitchen()
    elif "pig" in next:
        dead("You only want me for my bacon, pig runs off.")
    else:
        print "You have to chose one."

def dead(why):
    print why, "Idiot."
    exit(0)



def start():
    print "You are in a hallway."
    print "There is a tiny door and a huge door."
    print "Which door do you open?"

    next = raw_input("> ")

    if next == "tiny":
        ballroom()
    elif "huge" in next:
        kitchen()
    else:
        dead("Someone who hates procrastinators stabbed you in the face.")

start()

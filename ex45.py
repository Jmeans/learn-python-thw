from sys import exit
class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
class Death(Scene):

    quips = [
        "You have fluff for brains."
        "I'm glad you died, you are retarded."
    ]

    def enter(self):
        print Death.quips
        exit(1)
class FleshEatingRoom(Scene):

    def enter(self):
        print "Your old college roommate blames you for stealing his girlfriend."
        print "He went off the deep end and secretly became an evil scientist. He sent"
        print "a limo to pick you up with an invitation for a lovely dinner at his mansion. When you"
        print "arrive at the door and ring the bell, the welcome mat falls through the floor"
        print "taking you and the chauffeur with it."


        print "You are now standing in a small, pink, slimy room. The walls are gently moving in and out,"
        print "as if breathing. The chauffeur, determined to get paid for his services today starts across"
        print "the room. He immediately looses his balance, as the floor has the stability of a water bed."
        print "Falling flat on his face, he presses his arms to the floor to try to get up, but the floor"
        print "keeps giving and sloshing under him. He screams and you realize that the room is quickly"
        print "digesting him. What do you do?"

        action = raw_input("> ")

        if action == "make a run for it":
            print "Horrified, you think you can make a run for it. Maybe if you keep high knees you will"
            print "make it across before your skeleton starts to show through your skin. But after only two"
            print "steps, you too fall on your face. You struggle and sink deeper into the flesh eating"
            print "floor and get digested. Lovely."
            return 'death'

        elif action == "edge along the walls":
            print "You decide to make your way along the wall, hoping to avoid getting sucked"
            print "into the floor. As soon as you press up against the wall, the wall pushes back,"
            print "shoving you face first into the floor. You desperately try to flip and flop,"
            print "hoping to get back on your feet, but it's useless. You hold your hand in front"
            print "of your face, watching the flesh fall off of it, and then your face melts off."
            print "Did you actually think that was going to work?"
            return 'death'

        elif action == "jump on to the chauffeur":
            print "You decide to use the chauffeur as a bridge while he still has some meat on his bones."
            print "You feel bad for a second, but he's already dead anyway. You take a huge leap and land on his"
            print "his calves. You fall to your knees and steady yourself. A couple of steps up the back and"
            print "you take another leap, crashing through the fleshy door into the next room. Bravo!"
            return 'dinosaur_room'

        else:
            print "Nope!"
            return 'flesh_eating_room'
class DinosaurRoom(Scene):

    def enter(self):
        print "After crashing through the door, your fall is broken by soft grass and small"
        print "bushes. The air is hot, humid and full of strange sounds. You brush yourself off and"
        print " get on your feet, only to fall back down as the ground shakes beneath you. Earthquake?"
        print "No, there is a slow steady rhythm of crashes, getting stronger and louder. They suddenly"
        print "quicken and you realize they are coming from behind you. You whip around, and see a gigantic"
        print "creature bolting straight at you. It looks like a T-Rex but has two heads, and huge strong arms"
        print "that shift it's weight forward, and it runs like a massive gorilla. Gorilla-Rex? G-Rex? Glancing"
        print "around you see a door in the face of a cliff about a hundred yards to your right. What do"
        print "you do?"

        action = raw_input("> ")

        if action == "run to door":
            print "You jump into action, and sprint for the door. The G-Rex quickly changes directions and catches"
            print "you with you in a matter of seconds. It swings one of it's scaly arms and slams it down on top"
            print "of you. He then picks up your remains that now resemble a pancake, sniffs you and drops you"
            print "down his throat. Did you really think you could out run him?"
            return 'death'

        elif action == "curl up into a ball":
            print "Terrified, your natural reaction is to curl up into a ball on the ground, eyes closed tightly."
            print "You brace yourself for pain and death, as the G-Rex passes right by you. He was after something"
            print "in the forest behind you and hardly noticed you. After he passes, you stand up and head for"
            print "the door."
            return 'under_water'

        else:
            print "Nope!"
            return 'dinosaur_room'


class UnderWater(Scene):

    def enter(self):
        print "You step through the door and immediately fall 2 stories down into a water filled room."
        print "You tread water and look around for another door. You see two side by side about 20 feet below"
        print "water level on the opposite wall. You also see an enormous open mouth, almost the width of the room"
        print "rising from below. You have to make a decision fast. Do you take the door on the left or the door"
        print "on the right?"

        action = raw_input("> ")

        if action == "left":
            print "You take a breath and swim down as quickly as you can. The gaping mouth is getting closer as you"
            print "pull open the door on the left. Behind it you find only the wall. It doesn't go anywhere."
            print "Before you can reach for the other knob, you are swallowed by the mouth and chewed up."
            print "DUN DUN DUNNNNNN"
            return 'death'

        elif action == "right":
            print "The huge mouth is rapidly approaching as you swim down for the door on the right. You always"
            print "favored things on the right for no apparent reason. You are hoping your life long OCD was"
            print "preparing you for this moment. You yank the handle and are immediately sucked out as the water"
            print "pours into the next room."
            return 'show_down'

        else:
            print "Nope!"
            return 'under_water'


class ShowDown(Scene):

    def enter(self):
        print "Some how you manage to get the door close and look around at your"
        print "next challenge. The room looks like a dimly lit warehouse. Nothing too intimidating."
        print "HELLO LOSER! a voice booms from above. Your old roommate descends on a floating platform."
        print "You think it's very evil scientist of him and roll your eyes. He stops his descent a few feet"
        print "above your heard and rambles on about how you intentionally ruined his life, driving him"
        print "to his evils ways. He says he has hated you for so long but in this moment realizes that you"
        print "have made him the genius he is and wishes to immortalize you by dipping you in a chemical"
        print "that will kill you, but preserve your body for all time. You will then be put on display in his"
        print "entry way."

        print "You look around for a weapon, there is a whip and a crow bar in sight. Which do you choose?"

        action = raw_input("> ")

        if action == "crow bar":
            print "You lunge for the crow bar and hold it out, ready to swing. Your roommate laughs like "
            print "an idiot and tells you it's useless trying to defeat him. He powers is floating platform"
            print "towards you, you swing the crow bar. He jumps out of the way, and off his platform. He"
            print "falls to the ground and lands on his head and dies. He never was very coordinated. You win!"
            print "You take over his crazy mansion and throw bomb parties every weekend. Good job!"

            return 'finished'

        elif action == "whip":
            print "You grab the whip and try to crack it in his direction. You end up hitting yourself in the face."
            print "You have never used a whip, you don't know why you thought you could defeat someone with this"
            print "thing. While you are grabbing at the would on your face, your opponent flies at you on his"
            print "floating platform and knocks you in the head with the corner, killing you instantly. You are then"
            print "dipped in the preservation chemical, dressed in a servant's suit and posed like one of those"
            print "dog butlers in his entry way. You lose."

            return 'finished'
class Map(object):

    scenes = {
        'flesh_eating_room': FleshEatingRoom(),
        'dinosaur_room': DinosaurRoom(),
        'under_water': UnderWater(),
        'show_down':ShowDown(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
a_map = Map('flesh_eating_room')
a_game = Engine(a_map)
a_game.play()
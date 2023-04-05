''' contains function calls for game'''

import random as r

###################################### intro, race result, and exit text #########################

def intro_ponies(ponies):

    for poney in ponies:

        print("")
        poney.say_name()
        poney.say_location()
        poney.say_speed()
        print("")


def give_result(ponies):

    ponies.sort(key = lambda x: x.location, reverse = True)

    placing = [
                "First Place goes to:",
                "Second Place goes to:",
                "Third Place goes to:"
                ]

    placing_index = 0

    for poney in ponies:

        print("")
        print(placing[placing_index])
        print(poney.say_name())
        print(poney.say_location())

        placing_index += 1

############################### manage racing macanics ##########################################

def move_ponies(ponies):

    for poney in ponies:

        poney.move()
        print("")
        print(poney.say_name())
        print(poney.say_speed())
        print(poney.say_location())
        
    print("***************************************************************************")

def speed_boost(ponies):

    boosted = r.choice(ponies)
    boost = r.randint(1,5)

    boosted.change_speed(boost)

    return boost, boosted


def normalize_speed(boost, boosted):

    un_boost = boost * -1
    
    boosted.change_speed(un_boost)


def race_finished(ponies):

    for poney in ponies:

        if poney.location >= 100:

            return True


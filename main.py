''' main file for racing simulator'''

from ponies import Poney
import functions as f

# makin ponies putin them in variables
a = Poney("Shamrock", speed = 1)

b = Poney("Constantine", speed = 1)

c = Poney("StarScream", speed = 1)

# stableling ponies inside a list
ponies = [a, b, c]

# introduces the ponies
f.intro_ponies(ponies)

# is a poney going faster 
going_faster = False

# main game loop
while True:

    # increase the speed of a random poney and save that poney to a variabel
    boost, boosted = f.speed_boost(ponies)

    # moves ponies location and prints results
    f. move_ponies(ponies)

    # return boosted poney to normal speed
    f.normalize_speed(boost, boosted)

    # checks for end of race
    if f.race_finished(ponies):

        break

# prints results of race
f.give_result(ponies)

print("")
print("That is all thak you for playing!")




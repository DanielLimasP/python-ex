#Python the hard way: excercise 31
# This one comes with a tittle... 

## Making decisions...

print("You enter a dark room with two doors. Do you go through door #1 or door #2?")
door = input("> ")

if door == "1":
    print("There's a giant bear eating a human corpse. What do you do?")
    print("1 - Punch the bear in the nuts, show him who is the boss...")
    print("2 - Scream and try to run towards the exit...")

    bear = input("> ")
    if bear == 1:
        print("The bear eats your face. Good Job!")
    elif bear == "2":
        print("The bear eats your face. Good Job!")
    else:
        print("Well, doing %s is probably better. Bear runs away..." % bear)
    
elif door == "2":
    print("You stare into the endless abyss of Cthulhu's void. What do you see?")
    print("1 - Blueberries")
    print("2 - Two bears high fiving")
    print("3 - The secrets of the universe...")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives the intense pain that staring right into Cthulhu's void brings")
    else:
        print("The insanity rots your eyes into a pool of smuck and turns your brain into a pile of mush...")

else:
    print("You stumble upon around and fall into the void or something... and you deceased... end... ?...")
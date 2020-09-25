#Python the hard way: excercise 35
from sys import exit

def dead(why):
    print(why, "Good job!!!")
    exit(0)

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, you're not greedy, you winner")
    if how_much < 50:
        print("Nice, your'e not greedy. You win")
        exit(0)
    else:
        dead("You greedy fucker")
    
def bear_room():
    print("There is a bear in here...")
    print("The bear has a bunch of honey...")
    print("The fat stupid bear is blocking the access to another room")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")
        if choice == "Take the honey and run...":
            dead("The bear looks at you and proceeds to slap your face off... good!")
        elif choice == "Taunt bear" and not bear_moved:
            print("The bear has moved from the door. Now you can go through it...")
        elif choice == "Taunt bear" and bear_moved:
            print("The bear gets pissed off and kills you almost instantly... Good!")
        elif choice == "Open door" and bear_moved:
            gold_room()
        else:
            print("I don't know what %s is..." %choice)

def cthulhu_room():
    print("Here you see the greatest of the evils... Cthulhu...")
    print("He... it... stares back at you and you go insane...")
    print("Do you flee for your life or try to fight the insanity back?")
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "Fight back!" in choice:
        dead("Well... your insanity tastes damn good...")
    
def start():
    print("You're in a dark room...")
    print("There is a door to your right and another one to your left...")
    print("Which one do you take?")
    choice = input()

    if choice == "Left":
        bear_room()
    elif choice == "Right":
        cthulhu_room()
    else:
        dead("You stumble upon the great void of something... and die... maybe...")

start()
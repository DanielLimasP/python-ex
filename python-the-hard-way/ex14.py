#Python the hard way: Ejercicio 14
from sys import argv

script, userName, quiz = argv
prompt = '---> '

if quiz == 'yes':
    print("Hi %s, I'm the %s script. " %(userName, script))
    print("I'd like to ask you a few questions.")
    print("Do you like me, %s?" % userName)
    likes = input(prompt)
    print("Where do you live %s?" % userName)
    lives = input(prompt)
    print("What kind of computer do you have")
    computer = input(prompt)

    print('''
    Alright, so you said %r about liking me and
    you live in %r. Not sure were that is, though.
    And finally, you have a %r computer. Noice.
    ''' %(likes, lives, computer))
elif quiz == 'no':
    print("You, %r, did not want to take the quiz" %userName)
else:
    print("I'm no magician, you either say yes or no to the quiz")

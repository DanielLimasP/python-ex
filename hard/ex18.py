#Python the hard way: Ejercicio 18

#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("ar1: %r, arg2: %r" %(arg1, arg2))
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))
def print_one(arg1):
    print("arg1: %r" %arg1)
def print_none():
    print("I've got nothing")

print_two("Daniel", "God")
print_two_again("Jacky", "Jacky")
print_one("Noice")
print_none()

#Python the hard way: Ejercicio 16

from sys import argv

script, filename = argv

print("We're going to erase %r" %filename)
print("If you don't want that, hit CTRL + C")
print("If you do want that, Hit RETURN")
input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Good bye boi")
target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file")

target.write("%r \n %r \n %r \n" %(line1, line2, line3))

print("And now we close the file")
target.close()

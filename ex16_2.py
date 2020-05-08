#Python the hard way: Ejercicio 16_2

from sys import argv

script, filename, username = argv

print("Hello and welcome to the little text editor %r" %username)
print("We're going to erase %r" %filename)
print("If you don't want that, hit CTRL + C")
print("If you do want that, Hit RETURN")
input("?")

print("Opening the file... %r" %filename)
target = open(filename, 'w')

print("Truncating the file %r" %filename)
target.truncate()

print("Now I'm going to ask you for three lines")
line1 = input("Line 1:")
line2 = input("Line 2:")
line3 = input("Line 3:")

print("I'm going to write these to the file")

target.write('''
Nombre del archivo: %r

%r
%r
%r


Firma: %r
''' %(filename, line1, line2, line3, username))

print("And now we close the file")
target.close()

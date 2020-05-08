#Python the hard way: Ejercicio 20

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file: \n")
print_all(current_file)
print("It's rewind time")
rewind(current_file)

print("Lets print three lines \n")
current_line = 1

print_a_line(current_line, current_file)
print_a_line(current_line + 1, current_file)
print_a_line(current_line + 2, current_file)

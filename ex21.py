#Python the hard way ex21
def add(a, b):
    print("ADDING %d + %d" %(a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" %(a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" %(a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" %(a, b))
    return a / b

print("Let's do math with some functions \n")
age = add(20, 1)
height = subtract(200, 26)
weight = multiply(60, 2)
iq = divide(200, 1)

print('''
Age: %d
Height: %d
Weight: %d
IQ: %d
''' %(age, height, weight, iq))

print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes. " , what , "Can you do it by hand?")

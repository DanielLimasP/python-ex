#Python the hard way: excercise 32

# Finally something interesting...

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print("This is count %d" %number)

for fruit in fruits:
    print("Current fruit is %s" %fruit)

for i in change:
    print("I got %r" %i)

elements = []

for i in  range(0, 6):
    print("adding element %d to elements" %i)
    elements.append(i)

for i in elements:
    print("Current element: %d" %i)



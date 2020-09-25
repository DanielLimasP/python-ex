#Python the hard way: Ejercicio 19

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses" % cheese_count)
    print("You have %d boxes of crackers" % boxes_of_crackers)
    print("Man, that's enough for a party")
    print("Now, get a blanket")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or, we can use the variables from")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside of it")

cheese_and_crackers(1 + 2, 3 + 4)

print("And even combine variables and math")

cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 5)

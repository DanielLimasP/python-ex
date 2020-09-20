#Python the hard way: excercise 33
def addNumbersToList(cond):
    numbers = [] 
    i = 0
    while i < cond:
        print("At the top i is %d" %i)
        numbers.append(i)   
        i += 1
    return numbers

def addNumbersAlt(cond):
    numbers = []
    for i in range(cond):
        numbers.append(i)
    return numbers

print(addNumbersToList(10))
print(addNumbersAlt(10))
#Python the hard way: Aproximando el valor de la constante e
cont = 0.000
def factorial(num):
    if num >= 1:
        return num * factorial(num - 1)
    else:
        return 1
def euler(cont):
    if(cont <= 100):
        e = 1.0 / factorial(cont)
        return e + euler(cont + 1)
    else:
        return 0.0
print(euler(cont))
#print(factorial(4))

#Python the hard way: Ejercicio 13
from sys import argv

script, a1 = argv

print("The name of the script is: " , script)
print("And you can change the value of a1, which is: " , a1)
a1 = input("Ingresa un nuevo valor para a1:")
print("El nuevo valor de a1 es %r" % a1)

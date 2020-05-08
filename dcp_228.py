#Coding Challenge 228: Given an array of numbers,
    #arrange them in a way that yields the largest value.
    #For example, if the given numbers are {54, 546, 548, 60},
    #the arrangement 6054854654 gives the largest value. And if
    #the given numbers are {1, 34, 3, 98, 9, 76, 45, 4},
    #then the arrangement 998764543431 gives the largest value.
#---------------------------------------------------------------------
#De la librería itertools (herramientas iterativas)
#sacamos la utilería de permutaciones para obtener
#todas las permutaciones posibles con los elementos de una lista

from itertools import permutations
def organizater(list):
    lst = []
    #para cada permutación en una lista de longitud 'n'
    for i in permutations(list, len(list)):
        #Agregamos esa permutación a la nueva lista
        #El join va uniendo los números en cada permutación
        #El map es una función que ejecuta una función sobre cada
        #valor iterado. En este caso, str sobre cada i
        lst.append("".join(map(str,i)))
    #Al final, regresamos el valor más alto de la lista
    return max(lst)

print(
'''
El entero más alto que puedes obtener
al combinar los valores de la lista
[10, 7, 76, 415] es %r
''' %organizater([10, 7, 76, 415]))

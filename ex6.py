#Python the hard way: Ejercicio 6

#Pos el vato quiere que haga lo mismo, de poner un comentario
#sobre cada línea de código

x = "There are %d types of people" % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)

print(x)
print(y)

print("I said: %r" % x)
print("I also said: '%s'" % y)

hilarious = True
joke_evaluation = "Isn't that joke funny? %r"

#Aquí 'joke_evaluation' lleva el formato '%r' que sirve
#para imprimir básicamente cualquier cosa, sin embargo,
#le pasamos la variable a imprimir una vez que vamos a
#imprimir toda la cadena
print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)

#Python text remover or something
searchfile = open('ejerciciosListas.txt', 'r')
for line in searchfile:
    if "/*------------------------------------------------------------------*/" in line: 

        print(line)
searchfile.close()

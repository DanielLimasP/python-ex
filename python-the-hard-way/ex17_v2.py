#Python the hard way: Ejercicio 17_v2
from sys import argv; import os.path
script, from_file, to_file = argv
in_file = open(from_file).read()
out_file = open(to_file, "w").write(in_file)
print("Done")

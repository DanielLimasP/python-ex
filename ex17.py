#Python the hard way: Ejercicio 17

from sys import argv
import os.path

script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))
in_file = open(from_file)
in_data = in_file.read()

print("The input is %d bytes long" % len(in_data))
print("Does the output file exists? %r" % os.path.exists(to_file))
print("READY. Hit RETURN to continue, CTRL-C to abort")
input()
out_file = open(to_file, "w")
out_file.write(in_data)

print("Alright, done")

out_file.close()
in_file.close()

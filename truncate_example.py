# We open the file

file_open = open('test2.txt', 'r+')
print("Name of the file: " , file_open.name)

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = file_open.readline()

print("Read Line: %s" %line)

# And now we truncate the remaining file
file_open.truncate()

# We read the file again
line = file_open.readline()
print("Read Line: %s" %line)

# And we close the open file

file_open.close()

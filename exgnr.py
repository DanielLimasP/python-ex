def exrgnr():
    for i in range(30):
        excercise = open('ex' + str(i + 22) + '.py', 'w+')
        excercise.write("#Python the hard way: excercise %s" % str(i + 22))
exrgnr()

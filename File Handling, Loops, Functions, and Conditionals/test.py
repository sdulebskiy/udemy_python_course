temperatures = [10, -20, -289, 100]

def c_to_f(c):
    f = c* 9/5 + 32
    return float(f)

def writer(temps, fileName):
    with open(fileName, 'w') as fileToWrite:
        for t in temps:
            if t > -273.15:
                print("Writing result of convertion for temperature %s" % (t))
                fileToWrite.write(str(c_to_f(t))+'\n')
            else:
                print ("Temperature %s is lower than allowed" % (t))

writer(temperatures, 'fileToWrite.txt')





#with open('fileToWrite', 'w') as fileToWrite:
#    fileToWrite.write('some text')
#    fileToWrite.close()

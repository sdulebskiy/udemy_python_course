listOfNumbers = [1,2,3]

fileToWrite = open('filetowrite.txt', 'w')

for element in listOfNumbers:
    fileToWrite.write(str(element)+'\n')

fileToWrite.close()

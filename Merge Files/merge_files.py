from datetime import datetime, date

def writeToFile(fileToWriteHandler, fileFromPath):
    with open (fileFromPath, 'r') as fileToReadFrom:
        lines = fileToReadFrom.readlines()
        for line in lines:
            fileToWriteHandler.write(str(line)+'\n')

fileName = datetime.now()
fileName = fileName.strftime("%y-%m-%d-%H-%M-%S-%f")

with open (str(fileName), 'w') as mergedFile:
    writeToFile(mergedFile, 'file1.txt')
    writeToFile(mergedFile, 'file2.txt')
    writeToFile(mergedFile, 'file3.txt')


#mergedFile.close()

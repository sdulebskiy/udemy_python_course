from datetime import datetime, date
from glob2 import glob

def writeToFile(fileToWriteHandler, fileFromPath):
    with open (fileFromPath, 'r') as fileToReadFrom:
        fileToWriteHandler.write(fileToReadFrom.read()+'\n')


def mergeTXTFiles():
    fileName = datetime.now().strftime("%y-%m-%d-%H-%M-%S-%f")
    with open (fileName, 'w') as mergedFile:
        for fileToRead in glob('*.txt'):
            writeToFile(mergedFile, fileToRead)

mergeTXTFiles()

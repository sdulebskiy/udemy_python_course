fileOpen = open('fruits.txt', 'r')

#fileContent = fileOpen.read()
#fileContent = fileOpen.list()
#print fileContent

# Read line
#print (fileOpen.readline())

#readlines

#print (fileOpen.readlines())

fileLines = fileOpen.readlines()
#fileContent = fileOpen.read()
for line in fileLines:
    print len(line.strip('\n'))

fileOpen.close()

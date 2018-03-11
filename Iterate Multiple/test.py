a = [1,2,3]
b = ['a','s','c']

zipped = zip (a,b)
print zipped
unzipped = zip(*zipped)
print unzipped[0][1]

for c,d in zip(a,b):
    print ("%s is %s" % (c,d))

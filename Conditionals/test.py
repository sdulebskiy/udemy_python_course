def string_length(mystring):
    if type(mystring) == int:
        #print ("Sorry, integers don't have length")
        return "Sorry, integers don't have length"
    elif type(mystring) == float:
        return "Sorry, floats don't have length"
    else:
        return len(mystring)


#print(string_length(10))
#print(string_length(10.6))
#print(string_length('Length'))

def cel_to_fahr(c):
    if c >= -273.15:
        return c * 9/5 + 32
    else:
        return 'Value should be greate than -273.15'


print(cel_to_fahr(10))
print(cel_to_fahr(-274))

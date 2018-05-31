from compare_function import compareFunction

someInputValue = input('Please enter a number: ')

try:
    inputNumber = int(someInputValue)
except Exception as e:
    try:
        float(someInputValue)
    except Exception as e:
        print ("You've entered a string. Expecting NUMBER")
    else:
        print ("You've entered a float. Expecting NUMBER")
else:
    compareFunction(inputNumber)

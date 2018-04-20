import json
import difflib

dictJson = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in dictJson:
        return dictJson[word]
    elif word.capitalize() in dictJson:
        return dictJson[word.capitalize()]
    elif len(difflib.get_close_matches(word, dictJson.keys())) != 0:
        print ("Cannot find any definition foDelphir word %s. Did you mean %s? Y/N" %(word, difflib.get_close_matches(word, dictJson.keys(), 1)))
        answer = raw_input()
        if answer == 'Y':
            return dictJson[difflib.get_close_matches(word, dictJson.keys(), 1)[0]]
        elif answer == 'N':
            return "Sorry. Entered word does not exist in dictionary"
        else:
            return "We didn't understand your entering"
    else:
        return "Sorry. Entered word does not exist in dictionary"


wordToTranslate = raw_input("Enter a word: ")

result = translate(wordToTranslate)

if type(result) == 'list':
    for item in result:
        print item
else:
    print result

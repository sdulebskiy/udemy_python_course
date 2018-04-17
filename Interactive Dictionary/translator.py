import json
import difflib

dictJson = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in dictJson:
        return dictJson[word]
    elif len(difflib.get_close_matches(word, dictJson.keys())) != 0:
        print ("Cannot find any definition for word %s. Did you mean %s? Y/N" %(word, difflib.get_close_matches(word, dictJson.keys(), 1)))
        answer = raw_input()
        if answer == 'Y':
            return dictJson[difflib.get_close_matches(word, dictJson.keys(), 1)[0]]
        else:
            return "Sorry. Entered word does not exist in dictionary"
    else:
        return "Sorry. Entered word does not exist in dictionary"


wordToTranslate = raw_input("Enter a word: ")

print (translate(wordToTranslate))

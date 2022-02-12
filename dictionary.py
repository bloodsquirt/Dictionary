import json
from difflib import get_close_matches

dict = json.load(open("dict.json"))

def meaning(word):
    word = word.lower()
    if word in dict:
        return dict[word]
    elif word.title() in dict:
        return dict[word.title()]
    elif word.upper() in dict:
        return dict[word.upper()]
    elif len(get_close_matches(word,dict.keys())) > 0:
        yn=input("Did u mean % s instead? Press Y for yes or press N for no: "%get_close_matches(word,dict.keys())[0])
        yn=yn.lower()
        if yn=="y":
            return dict[get_close_matches(word,dict.keys())[0]]
        elif yn=="n":
            return "This word dosen't exist, please try again."
        else:
            return "Invalid entry"
    else:
        print ("This word dosen't exist, please try again.")



word =input("Please Enter the word: ")

output=meaning(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)

import json #module required to load json file
from difflib import get_close_matches

#loading data
dictionaryData = json.load(open("dictionarydata.json"))

#function to search for word from dictionaryData
def SearchDictionary(searchKey):
    if searchKey.lower() in dictionaryData:
        return dictionaryData[searchKey.lower()]
    elif searchKey.title() in dictionaryData:
        return dictionaryData[searchKey.title()]
    elif searchKey.upper() in dictionaryData:
        return dictionaryData[searchKey.upper()]
    else:
        closeMatch = get_close_matches(searchKey.lower(),dictionaryData.keys())
        if len(closeMatch) > 0:
            print("We could not find %s. The closest match was '%s' with the following meaning:" \
            %(searchKey, closeMatch[0]))
            return dictionaryData[closeMatch[0]]
        else:
            return ["This word does not exist in the dictionary"]

#interaction with user
searchKey = input('Enter the word you wish to search for:\n')
print("\n".join(SearchDictionary(searchKey)))

#currently lacking a while loop to keep prompting user for input 
